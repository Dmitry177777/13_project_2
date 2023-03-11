
from data.class_chanell import Channel

channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
vdud =Channel(channel_id)

# получаем значения атрибутов
print(vdud.title)
# вДудь
print(vdud.video_count)
# 163
print(vdud.url)
# https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA

# менять не можем
# vdud.channel_id= 'Новое название'
# AttributeError: property 'channel_id' of 'Channel' object has no setter

# можем получить объект для работы с API вне класса
print(Channel.get_service())
# <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

print(vdud.print_info())

# создать файл 'vdud.json' в данными по каналу
# vdud.to_json('vdud.json')




#channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь

# channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'    # Редакция
#
# channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()
#
# print(json.dumps(channel, indent=2, ensure_ascii=False))