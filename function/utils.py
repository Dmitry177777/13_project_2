
from data.class_chanell import Channel

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
print(ch2)
#Youtube-канал: Редакция

#ch1 > ch2
#True

#ch1 < ch2
#False

ch1 + ch2
#1030000076


