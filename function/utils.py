import os

from googleapiclient.discovery import build

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)

import json

# channel_id = 'UCMCgOm8GZkHp8zJ6l7_hIuA'  # вДудь
channel_id = 'UC1eFXmJNkjITxPFWTy6RsWg'    # Редакция

channel = youtube.channels().list(id=channel_id, part='snippet,statistics').execute()

print(json.dumps(channel, indent=2, ensure_ascii=False))