install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_get_url_data.py

format:
	black *.py

run:
	jupyter nbconvert --execute --to notebook --inplace my_collab_notebook.ipynb &&\
	python get_url_data.py &&\
	python dask_kmeans.py


lint:
	pylint --disable=R,C get_url_data.py

all: install format lint test run
