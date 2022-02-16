import time


import requests


from pprint import pprint


class VKPhoto:

    def profile_photo():
        user_id = ''
        token = ''
        URL = 'http://api.vk.com/method/photos.get'
        params = {
            'owner_id': user_id,
            'access_token': token,
            'v': '5.131',
            'album_id': 'profile',
            'extended': '1',
            'photo_sizes': '1',
            'count': '200'
        }
        photos = {'height': '0', 'width': '0'}
        every_photo = []
        likes_list = []
        res = requests.get(URL, params=params).json()
        albums = res['response']['items']
        for photo in albums:
            photos['name'] = photo['likes']['count']

            for likes in likes_list:
                if photo['likes']['count'] == likes:
                    photos['name'] = photo['date']
                    break
            likes_list.append(photo['likes']['count'])
            for size in photo['sizes']:
                if (int(size['height']) + int(size['width'])) >= (int(photos['height']) + int(photos['width'])):
                    photos['height'] = size['height']
                    photos['width'] = size['width']
                    photos['url'] = size['url']
            every_photo.append(photos)
            photos = {'height': '0', 'width': '0'}
        return every_photo






pprint(VKPhoto.profile_photo())

