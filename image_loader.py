import requests


def download_image(image_url):
    try:
        response = requests.get(image_url)
        response.raise_for_status()  # Проверка на наличие ошибок
        return response.content  # Возвращаем данные изображения
    except requests.exceptions.RequestException as e:
        print(f"Error downloading image: {e}")
        return None