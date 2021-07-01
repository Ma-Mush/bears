from telethon import events, TelegramClient 
from work import archive
from time import time 

client = TelegramClient("bear", "3493018",
    "f1d6ec6b2ae7f436997c16bc24e0983a").start(bot_token="1815891726:AAG1vM0Bas7DV9YiMkiy152TFdxtoxxw0_0")
client.parse_mode = 'html'

def command(*args):
    return '|'.join([i for i in [rf'^\/({i})+(\@BearFindBot\w*(_\w+)*)?([ \f\n\r\t\v\u00A0\u2028\u2029].*)?$' for i in args
    ]])

@client.on(events.NewMessage(pattern=command("start")))
async def start(event):
    await client.send_message(event.chat.id, "Привет! Этот бот создан для поиска белых мишек по фото. Для этого просто отправь архив (рекомендуется расширение .zip) с фотографиями")

@client.on(events.NewMessage())
async def working(event):
    if event.message.media != None:
        t = time()
        m = await client.send_message(event.chat.id, "Скачиваю...")
        await client.download_file(event.message, f"{event.chat.id}.zip")
        await m.edit("Обработка...")
        resp = archive(f"{event.chat_id}.zip")
        if resp[0]:
            await client.send_file(event.chat.id, resp[2], caption=f"Найдено медведей {resp[1]}")
        else:
            await client.send_message(event.chat.id, resp[1])
        await m.edit(f"Затрачено времени - {time() - t} секунд")

client.run_until_disconnected()