from telethon.sync import TelegramClient
api_id = 1772559
api_hash = '0c7244423d05e7e4c48b937763d2fd62'

with TelegramClient(input("Session Adi Ne : "), api_id, api_hash) as client:
    client.send_message('me', 'BOT AYARLAMALARI TAMAMLANDI')
    print("Ayarlama Tamamlandi")
    quit()
    client.run_until_disconnected()
