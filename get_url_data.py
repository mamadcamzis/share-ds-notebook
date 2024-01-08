import pandas as pd


def get_url_data(url):
    # Define the column names
    col_names = [
        "sepal_length_in_cm",
        "sepal_width_in_cm",
        "petal_length_in_cm",
        "petal_width_in_cm",
        "class",
    ]

    # Read data from URL
    iris_data = pd.read_csv(url, names=col_names)
    return iris_data


if __name__ == "__main__":
    # Webpage URL
    # url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    get_url_data(
        "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
    )
