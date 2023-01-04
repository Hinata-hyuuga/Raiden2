

from datetime import datetime
import random
from pyrogram import filters
from pyrogram.types import Message

from config import BANNED_USERS, MUSIC_BOT_NAME, PING_IMG_URL
from strings import get_command
from YukkiMusic import app
from YukkiMusic.core.call import Yukki
from YukkiMusic.utils import bot_sys_stats
from YukkiMusic.utils.decorators.language import language

### Commands
PING_COMMAND = get_command("PING_COMMAND")


@app.on_message(
    filters.command(PING_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@language
async def ping_com(client, message: Message, _):
    response = await message.reply_photo(
        photo=PING_IMG_URL,
        caption=_["ping_1"],
    )
    start = datetime.now()
    pytgping = await Yukki.ping()
    UP, CPU, RAM, DISK = await bot_sys_stats()
    resp = (datetime.now() - start).microseconds / 1000
    await response.edit_text(
        _["ping_2"].format(
            MUSIC_BOT_NAME, resp, UP, DISK, CPU, RAM, pytgping
        )
    )

EI = [
    "CAACAgUAAx0CYT7QSgACAWdjs6JCPX6g0GIVDzUuPQN7W1SbpQAC6wYAAg2doVW9r2IhGX8ObR4E",
    "CAACAgUAAx0CYT7QSgACAVljs575DPn8wAudBHyKIvQJ9i37ewACwgcAAu1toFVc4k6UwHRHGh4E",
    "CAACAgUAAx0CYT7QSgACAUFjs523ZopgURCxIzB75MzMrznH3wACFggAAtXHmVUGXajOdHGZLR4E",
    "CAACAgUAAx0CYT7QSgACAURjs53cI8jWyNTVNSdiRq_V4RyokgACyAcAAhEXoVUJG35KePb_gh4E",
    "CAACAgUAAx0CYT7QSgACAUdjs54GLpYce6D2Gq9pxnS5eV2guAACUQcAArkPoFXJXBR6Ys_aAAEeBA",
    "CAACAgUAAx0CYT7QSgACAUpjs54_RlOzTrFxfnakNubgCR24kQACbQcAAu8tmVW8eMqus0XyKh4E",
    "CAACAgUAAx0CYT7QSgACAVljs575DPn8wAudBHyKIvQJ9i37ewACwgcAAu1toFVc4k6UwHRHGh4E",
    "CAACAgUAAx0CYT7QSgACAU1js55TudHfmsra3gfO1jDbTkTchQACaAYAAqEvoFX3R12juKv_wB4E",
    "CAACAgUAAx0CYT7QSgACAVBjs57B0rYfB8VwA30WLY5hqsdiHwACogYAArh1oFXQJF4rPxsv1R4E",
    "CAACAgUAAx0CYT7QSgACAVNjs57UASg8FgQQ1r_9U07Iq4DWigAC_wcAAi8MoVWTm5efm0LC7x4E",
    "CAACAgUAAx0CYT7QSgACAVZjs57mk-2m-ro13sFdznqFl4aJ1wAC-ggAAqxpmVU6GVmq7JMYjh4E",
    "CAACAgUAAx0CYT7QSgACAVljs575DPn8wAudBHyKIvQJ9i37ewACwgcAAu1toFVc4k6UwHRHGh4E",
    "CAACAgUAAx0CYT7QSgACAWdjs6JCPX6g0GIVDzUuPQN7W1SbpQAC6wYAAg2doVW9r2IhGX8ObR4E",
]


@app.on_message(filters.command("playforce"))
async def fp_com(client, message: Message, _):
    await message.reply_sticker(sticker=random.choice(EI))

