import json
class Channel ():
    """"Класс канала"""
    # all =[]
    # pay_rate = 1

    def __init__(self, youtube, channel_id):
        self.channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

        self.kind = self.channel.get ('kind') # kind
        self.etag = self.channel.get ("etag") # etag
        self.pageInfo = self.channel.get ("pageInfo") # pageInfo
        self.items = self.channel.get("items")  # items
    pass

    def print_info (self):
        """Метод вывода данных о канале"""
        self.channel_statistic = json.dumps(self.channel, indent=2, ensure_ascii=False)
        print(self.channel_statistic )
        return



