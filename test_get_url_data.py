import pytest
from get_url_data import get_url_data


@pytest.mark.parametrize(
    "url", ["https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"]
)
def test_get_url_data(url):
    iris_data = get_url_data(url)
    assert len(iris_data) == 150
