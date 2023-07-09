import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        """Метод загружает файлы по списку file_list на яндекс диск"""
        # Тут ваша логика
        # Функция может ничего не возвращать
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        params = {'path': '/picture.jpg'}
        headers = {"Authorization": "OAuth " + token}
        response = requests.get(url, headers=headers, params=params)

        # print(response.status_code)

        data = response.json()

        # print("json: ", data)

        url = data["href"]
        with open("picture.jpg", "rb") as f:
            requests.put(url, files={"file": f})


if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    token = open("token").read()
    path_to_file = 'picture.jpg'
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)


    # with open('picture.jpg', 'rb') as f:
    #     # path_to_file = os.path.abspath("C:\Users\ПК\Documents\Обучение\Нетодология\4. ООП и API\5.requests,http\2.YandexDisk\pythonProject\picture.jpg")
    #     token = open("token").read()
    #     path_to_file = f
    #     uploader = YaUploader(token)
    #     result = uploader.upload(path_to_file)