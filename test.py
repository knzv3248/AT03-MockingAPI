
import pytest
from main import cat_images_with_api


def test_cat_images_with_api_success(mocker):
    mock_get = mocker.patch("main.requests.get")
    mock_get.return_value.status_code = 200
    mock_get.return_value.json.return_value = [{"id":"bmp",
                                                "url":"https://cdn2.thecatapi.com/images/bmp.jpg",
                                                "width":500,
                                                "height":337}]
    cat_data = cat_images_with_api()
    assert cat_data == [{"id":"bmp",
                         "url":"https://cdn2.thecatapi.com/images/bmp.jpg",
                         "width":500,
                         "height":337}]

    return cat_data[0]["url"]


def test_cat_images_with_api_failure(mocker):
    mock_get = mocker.patch("main.requests.get")
    mock_get.return_value.status_code = 404
    mock_get.return_value.json.return_value = None
    cat_data = cat_images_with_api()
    assert cat_data is None
    return None

