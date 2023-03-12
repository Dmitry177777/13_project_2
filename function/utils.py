
from data.class_chanell import Channel
from data.class_chanell import PLVideo
from data.class_chanell import Video


channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'
vdud = Channel(channel_id)

# получаем значения атрибутов
print(vdud.title)
# вДудь
print(vdud.video_count)
# 163
print(vdud.url)
# https://www.youtube.com/channel/UCMCgOm8GZkHp8zJ6l7_hIuA

# менять не можем
vdud.channel_id = 'Новое название'
# AttributeError: property 'channel_id' of 'Channel' object has no setter

# можем получить объект для работы с API вне класса
print(Channel.get_service())
# <googleapiclient.discovery.Resource object at 0x000002B1E54F9750>

print(vdud.print_info())

# создать файл 'vdud.json' в данными по каналу
vdud.to_json('vdud.json')

ch1=Channel('UCMCgOm8GZkHp8zJ6l7_hIuA')
ch2=Channel('UCXD8fPuwMfizCmgMtc9KAqQ')



print(ch1)
#Youtube-канал: вДудь
print(repr(ch1))

print(ch2)
#Youtube-канал: Редакция
print(repr(ch2))


ch1 > ch2
#True

ch1 < ch2
#False

ch1 + ch2
#1030000076

# https://www.youtube.com/watch?v=9lO06Zxhu88
video1 = Video('9lO06Zxhu88')  # '9lO06Zxhu88' - это id видео из ютуб "etag": "GQNNYQsMXoegKlWQYVAogTvQdXM"

print(video1.print_info())

video2 = PLVideo('BBotskuyw_M', 'PL7Ntiz7eTKwrqmApjln9u4ItzhDLRtPuD')
#https://www.youtube.com/watch?v=BBotskuyw_M
#print(video1)
#Как устроена IT-столица мира / Russian Silicon Valley (English subs)
print(video2)
#Пушкин: наше все? (Литература)
# шаблон: 'название_видео (название_плейлиста)
