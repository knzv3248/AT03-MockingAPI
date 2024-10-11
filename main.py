import requests

def cat_images_with_api():
    url = "https://api.thecatapi.com/v1/images/search"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# cat_data = cat_images_with_api()
# print(cat_data)
# print(cat_data[0]["url"])
