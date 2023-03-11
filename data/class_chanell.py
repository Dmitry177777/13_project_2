import json
import os
from googleapiclient.discovery import build
class Channel ():
    """"Класс канала"""
    # all =[]
    # pay_rate = 1

    def __init__(self,  channel_id):
        youtube = Channel.get_service()
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        self.kind = self.channel.get ('kind') # kind
        self.url = self.channel.get ("etag") # etag
        self.pageInfo = self.channel.get ("pageInfo") # pageInfo
        self.items = self.channel.get("items")  # items

        self.channel_id =   channel_id # - id канала
        self.title = self.channel.get('items',{})[0].get('snippet',{}).get('title')  # - название канала
        self.description = self.channel.get('items',{})[0].get('snippet',{}).get('description') # - описание канала
        self.url = f'https://www.youtube.com/channel/{channel_id}'   # - ссылка на канал
        self.subscriberCount = self.channel.get('items',{})[0].get('statistics',{}).get('subscriberCount')  # - количество подписчиков
        self.video_count =  self.channel.get('items',{})[0].get('statistics',{}).get('videoCount') # - количество видео
        self.viewCount = self.channel.get('items',{})[0].get('statistics',{}).get('viewCount')  # - общее количество просмотров



        pass

    def print_info (self):
        """Метод вывода данных о канале"""
        self.channel_statistic = json.dumps(self.channel, indent=2, ensure_ascii=False)

        return self.channel_statistic
    @staticmethod
    def get_service():
        # API_KEY скопирован из гугла и вставлен в переменные окружения
        api_key: str = os.getenv('API_KEY')

        # создать специальный объект для работы с API
        youtube = build('youtube', 'v3', developerKey=api_key)
        return youtube


# Модифицируйте метод `__init__`, чтобы при создании экземпляра класса происходила инициализация следующих атрибутов класса:
#
# - id канала
# - название канала
# - описание канала
# - ссылка на канал
# - количество подписчиков
# - количество видео
# - общее количество просмотров
#
# Сделайте так, чтобы можно было получить id канала, но нельзя было его изменять/удалять.
#
# Реализуйте метод класса, который возвращает объект для работы с API ютуба. Используйте этот метод в классе, чтобы избежать дублирования кода.
#
# Реализуйте метод, который сохраняет информацию по каналу, хранящуюся в атрибутах экземпляра класса `Channel`, в json-файл. Продумайте самостоятельно формат записи в файл.