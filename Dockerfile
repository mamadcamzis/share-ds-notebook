# Stage 1: Build stage
FROM python:3.10 AS builder

# Set the working directory
WORKDIR /app

# Copy the source code and requirements.txt
COPY get_url_data.py /app
COPY test_get_url_data.py /app
COPY Makefile /app
COPY requirements.txt /app
COPY my_collab_notebook.ipynb /app

# Install dependencies
RUN make all

# Stage 2: Final image
FROM python:3.10-slim



# Copy only the necessary files from the builder stage
COPY --from=builder /usr/local/lib/python3.10/site-packages /usr/local/lib/python3.10/site-packages
COPY --from=builder /app /app

# Expose any necessary ports
#EXPOSE 8000

# Set environment variables if needed
# ENV MY_VAR=value

# Run your application
# Set the working directory
CMD ["python", "get_url_data.py"]
