import requests

class YandexDisk:

    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)

        }

    def new_folder(self):
        upload_url = "https://cloud-api.yandex.net/v1/disk/resources"
        headers = self.get_headers()
        params = {"path": 'vk'}
        response = requests.put(upload_url, headers=headers, params=params)

if __name__ == '__main__':
    token = ''

    newf = YandexDisk(token)
    result = newf.new_folder()