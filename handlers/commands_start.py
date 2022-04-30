from aiogram import types
from misc import dp,bot
from .sqlit import reg_user,cheak_traf,obnova_status,obnova_status_all,cheak_chat_id
import asyncio
content = -1001646847340


reg_user(1)

url = 'https://oplata.qiwi.com/create?'
key = 'publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPsZPmVFjj6M3Tgts8VLcUi2mAp14a2BbyqbQAsx5oYX7KmzANtyXsc853KAFhgtGmMcvGJkGaEA5YFtDMfKm1fnvE7jDavw7FYw93xXJhM'
markup = types.InlineKeyboardMarkup()
price = f'&amount=200'
finish_url = url + key + price
bat_pay = types.InlineKeyboardButton(text='🎫ОПЛАТИТЬ 200 РУБ', url=finish_url)
markup.add(bat_pay)


@dp.chat_join_request_handler()
async def join(update: types.ChatJoinRequest):
    reg_user(update.from_user.id)

    await asyncio.sleep(10)  # 10
    await bot.copy_message(from_chat_id=content, chat_id=update.from_user.id, message_id=4, caption="""Собрали весь платный контент у конкурентов, и загрузили всё в один канал 😳

🔥Цена смешная - 200₽

<b>✅Счет на оплату сформирован. Доступ будет открыт в автоматическом режиме после оплаты</b>""",reply_markup=markup)

    await asyncio.sleep(10)

    await bot.send_message(chat_id=update.from_user.id, text="""Огромные, надёжные архивы. Конфиденциальность превыше всего, ни за что не переживайте 💕

📌 Постоянное пополнение материала. Все старые видео в плохом качестве были удалены, на смену им добавлены новые, в наилучшем качестве 💕

📌 Самые адекватные цены. Без ерунды и кидалова. Материал собран профессионально, материал без повторений. В нашем БОТЕ вы платите за настоящий материал лучшего качества 💕

<b>✅Счет на оплату сформирован. Доступ будет открыт в автоматическом режиме после оплаты</b>""",reply_markup=markup)
    await asyncio.sleep(600)

    try:
        await update.approve()
    except:
        pass