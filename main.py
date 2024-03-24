from telethon import TelegramClient, events
from config import *

client = TelegramClient("session", api_id, api_hash)
client.start()

@client.on(events.NewMessage(chats=source))
async def forward_message(event):
    await event.forward_to(target)

client.start()
client.run_until_disconnected()
