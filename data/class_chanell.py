import json
import os
import datetime
from googleapiclient.discovery import build
class Channel ():
    """"Класс канала"""
    # all =[]
    # pay_rate = 1

    def __init__(self,  channel_id):
        youtube = Channel.get_service()
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        self.kind = self.channel.get ('kind') # kind
        #self.url = self.channel.get ("etag") # etag
        self.pageInfo = self.channel.get ("pageInfo") # pageInfo
        self.items = self.channel.get("items")  # items

        self.channel_id = channel_id # - id канала
        self.title = self.channel.get('items',{})[0].get('snippet',{}).get('title')  # - название канала
        self.description = self.channel.get('items',{})[0].get('snippet',{}).get('description') # - описание канала
        self.url = f'https://www.youtube.com/channel/{channel_id}'   # - ссылка на канал
        self.subscriberCount = self.channel.get('items',{})[0].get('statistics',{}).get('subscriberCount')  # - количество подписчиков
        self.video_count = self.channel.get('items',{})[0].get('statistics',{}).get('videoCount') # - количество видео
        self.viewCount = self.channel.get('items',{})[0].get('statistics',{}).get('viewCount')  # - общее количество просмотров

        # Channel.to_json(self)

    def __repr__(self):
        return f'Channel({self.title}, {self.video_count},{self.viewCount},{self.subscriberCount})'

    def __str__(self):
        return f'Youtube-канал: {self.title}'

    def __add__(self, other):
        count = self.subscriberCount + other.subscriberCount
        return print(f'{count}')

    def __gt__(self, other):
        A = int(self.subscriberCount)
        B = int(other.subscriberCount)

        return print(f'{(A > B)}')

    def __lt__(self, other):
        A = int(self.subscriberCount)
        B = int(other.subscriberCount)

        return print(f'{(A < B)}')


    @property
    def channel_id(self):
        pass
    @channel_id.setter
    def channel_id(self, new_id):
        return print(f"AttributeError: property 'channel_id' of 'Channel' object has no setter")

    def to_json(self, file):
        """Метод переноса атрибутов класса в файл json"""

        to_json = {
            'kind': self.kind,
            #'url': access_template,
            'pageInfo': self.pageInfo,
            'items': self.items,
            'channel_id': self.channel_id,
            'title': self.title,
            'description': self.description,
            'url': self.url,
            'subscriberCount': self.subscriberCount,
            'video_count': self.video_count,
            'viewCount': self.viewCount
            }

        with open(file, 'w') as f:
            f.write(json.dumps(to_json))

        pass



    def print_info (self):
        """Метод вывода данных о канале"""
        self.log = json.dumps(self.channel, indent=2, ensure_ascii=False)

        return self.log
    @staticmethod
    def get_service():
        # API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('API_KEY')

        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


class Video(Channel):
    def __init__(self, video_id):
        self.video_id = video_id
        youtube = Video.get_service()
        self.video = youtube.videos().list(id=video_id, part='snippet, recordingDetails, statistics').execute()

        self.title = self.video.get('items', {})[0].get('snippet', {}).get('title')  # - название канала
        self.subscriberCount = self.video.get('items', {})[0].get('statistics', {}).get('subscriberCount')  #!!!!!! - количество подписчиков
        self.video_count = self.video.get('items', {})[0].get('statistics', {}).get('videoCount')  #!!!!! - количество видео
        self.viewCount = self.video.get('items', {})[0].get('statistics', {}).get('viewCount')  # - общее количество просмотров


    def print_info(self):
        """Метод вывода данных о канале"""
        self.log = json.dumps(self.video, indent=2, ensure_ascii=False)

        return self.log

    def __repr__(self):
        return f'Video({self.title}, {self.video_count},{self.viewCount},{self.subscriberCount})'

    def __str__(self):
        return f'Video: {self.title}'
class PLVideo (Video):
    def __init__(self, video_id, plv_id):
        self.plv_id = plv_id
        self.video_id = video_id



        youtube = PLVideo.get_service()
        self.plv_item = youtube.playlistItems().list(playlistId = plv_id, part='id,snippet').execute()
        self.plv_=youtube.playlists().list(id = plv_id,  part='id,snippet').execute()
        for plv1 in self.plv_item.get('items'):
            if plv1.get('snippet', {}).get('resourceId', {}).get('videoId')  == self.video_id:

                self.title = plv1.get('snippet', {}).get('title')  # - название видео
        self.plv =self.plv_.get('items',{})[0].get('snippet', {}).get('title')


    def print_info(self):
        """Метод вывода данных о канале"""
        self.log1 = json.dumps(self.plv_item, indent=2, ensure_ascii=False)
        self.log2 = json.dumps(self.plv_, indent=2, ensure_ascii=False)
        return self.log1 + self.log2

    def __repr__(self):
        return f'PLVideo({self.title}, {self.video_count},{self.viewCount},{self.subscriberCount})'

    def __str__(self):
        return f'{self.title} ({self.plv})'


class PlayList (PLVideo):
    def __init__(self, plv_id):
        super().__init__(self, plv_id)
        self.url = f'https://www.youtube.com/playlist?list=/{plv_id}'  # - ссылка на плейлист

    def total_duration (self):
        self.total_duration = self.plv_.get('items', {})[0].get('snippet', {}).get('publishedAt')
        return print(f'{self.total_duration}')

    def show_best_video (self):
        self.video_id =
        pass

    def __repr__(self):
        return f'PlayList({self.plv},)'