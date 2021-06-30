from telethon import events, TelegramClient 
import zipfile
import cv2
import os

client = TelegramClient("1660159", "6e583efbc76417b8bbcfe215d7462126").start("1815891726:AAG1vM0Bas7DV9YiMkiy152TFdxtoxxw0_0")

def command(*args):
    return '|'.join([i for i in [rf'^\/({i})+(\@echoall2bot\w*(_\w+)*)?([ \f\n\r\t\v\u00A0\u2028\u2029].*)?$' for i in args
    ]])

@client.on(events.NewMessage (pattern=command("/start")))
async def start(event):
    await client.send_message(event.chat.id, "Привет! Этот бот создан для поиска белых мишек по фото. Для этого просто отправь архив (рекомендуется расширение .zip) с фотографиями")

def archive(name):
    fzip = zipfile.ZipFile(name)
    fzip.extractall(archive_name)
    fzip.close()
    for file in [i for i in os.walk(f"./{name}/")][0][2]:
        pass #обработка файлов тут

@client.on(events.NewMessage ())
async def work(event):
    if event.message.media != None:
        await client.download_file(event.message, f"{event.chat.id}.zip")
        resp = archive()
        await client.send_message(event.chat.id, "тут результат")