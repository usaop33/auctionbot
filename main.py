import os
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
from telethon.tl.types import MessageEntityCode
from telethon import TelegramClient, events, Button
import telethon.sync #lol copied from docs
import asyncio
import logging #lol copied from docs

API_ID = os.environ.get('API_ID', None)
API_HASH = os.environ.get('API_HASH', None)
TOKEN = os.environ.get('TOKEN', None)
TRADE_CHANNEL = os.environ.get('TRADE_CHANNEL', None)
BETRAYED_CHANNEL = os.environ.get('BETRAYED_CHANNEL', None)
SCAMMER_CHANNEL = os.environ.get('SCAMMER_CHANNEL', None)


api_id = API_ID
api_hash = API_HASH
bot_token = TOKEN
trade_channel = int(TRADE_CHANNEL)
betrayed_channel = int(BETRAYED_CHANNEL)
scammer_channel = int(SCAMMER_CHANNEL)


client = TelegramClient('konekgub', api_id, api_hash).start(bot_token=bot_token) #i dont really understand it lol but without this bot wont work

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', #copy pasted from telethon docs lol..... so usually it logs error
                    level=logging.WARNING)

xmods = 1037179104, 1174476949, 1786637879, 790824807, 5058417875, 1720329781, 1749188073, 1094810637, 1094810637, 5174776869
dxgays = 5152846377, 1316627940, 1027970627, 1196082322, 1814501074, 378738602, 5348701255, 1244265924, 1895916617, 2060752501, 5174776869, 1267367441


@client.on(events.NewMessage(pattern='/start'))
async def start(event):
    sender = await event.get_sender()
    await client.send_file(event.sender_id, 'https://telegra.ph/file/4f6e6f84b0b51714ac46a.jpg', caption = "Hello\n\nI am auction bot.\n\nMade by @BAJIKEISUKE_KUN\n\nI am powered by X MOD"
        ,
        buttons=[
        [
            Button.inline('AUCTION', 'auction'),
            Button.inline('{ x ɱօԃ }', 'xmod')
        ],
        [
            Button.url('OWNER', 'https://t.me/bajikeisukekun')
        ]
     ]
    )

@client.on(events.CallbackQuery(data='auction'))
async def auctioncb(event):
    await client.edit_message(event.sender_id, event.message_id,
        'Here are the things about auction',
        buttons=[
        [
            Button.url('AUCTION GROUP', "https://t.me/hexaauction")
        ],
        [
            Button.url('AUCTION CHANNEL', "https://t.me/shinyhub_official")
        ],
        [
            Button.url('TRADE AUCTION', "https://t.me/+nxKfcTbxLJ4zNTdl")
        ],
        [
            Button.url('AUCTION RULES', 'http://t.me/officerjennyprobot?start=-1001763955719')
        ],
        [
            Button.inline('Back', 'back')
        ]
      ]
    )

@client.on(events.CallbackQuery(data='xmod'))
async def xmodcb(event):
    await client.edit_message(event.sender_id, event.message_id,
        'Here are the things about TEAM { x ɱօԃ }',
        buttons=[
        [
            Button.url('{ x ɱօԃ } OWNER', 'https://t.me/BAJIKEISUKEKUN')
        ],
        [
            Button.url('{ x ɱօԃ } BOT', 'https://t.me/officerjennyprobot')
        ],
        [
            Button.url('{ x ɱօԃ } NEWS', 'http://t.me/XMODNEWS')
        ],
        [
            Button.url('{ x ɱօԃ } BANS', 'http://t.me/XMODBANS')
        ],
        [
            Button.inline('Back', 'back')
        ]
      ]
    )

@client.on(events.CallbackQuery(data='back'))
async def backcb(event):
    await client.edit_message(event.sender_id, event.message_id,
        'Hello\n\nI am auction bot.\nMade by @BAJIKEISUKE_KUN\nI am powered by X MOD\n\n\nIf you want to sell stuff in auction use /sell'
        ,
        buttons=[
        [
            Button.inline('AUCTION', 'auction'),
            Button.inline('{ x ɱօԃ }', 'xmod')
        ],
        [
            Button.url('OWNER', 'https://t.me/bajikeisukekun')
        ]
     ]
    )



user_cache = {}

@client.on(events.NewMessage(pattern='/new'))
async def sell(event):
    sender = await event.get_sender()
    user_id = event.sender_id
    if user_id in dxgays:
        await client.send_message(event.sender_id, "Ho Ho Ho\n\nIf you want to sell something in auction how about you sell your mom to xmods. Altough your moms are already free WHORE whose price is free for a year to use by anyone and they have such loose pussy.\n\n"+sender.first_name+" mom has got best whore award, "+sender.first_name+" is trying to find about his real dad, when "+sender.first_name+" fill any form in father section he writes xmods and 3.97 billion other." )
    elif user_id in xmods:
        async with client.conversation(user_id) as conv:
            await conv.send_message('FORWARD THE SOLD POKEMON DETAILS')
            miku = await conv.get_response(timeout = 90000)
            if miku.media:
                nino = miku.media
                yotsuba = miku.text
                await conv.send_message('Forward SOLD MESSAGE')
                ichika =  await conv.get_response(timeout = 90000)
                shikimori = ichika.text
                user_cache[user_id] = {}
                user_cache[user_id]['ID'] = user_id
                user_cache[user_id]['image'] = nino
                nakano = yotsuba+"\n\n"+shikimori
                user_cache[user_id]['text'] = nakano
                await client.send_file(event.sender_id, file = nino, caption = nakano
                    ,
                    buttons=[
                    [
                        Button.inline('SEND', 'send')
                    ],
                    [
                        Button.inline('Delete', 'delete')
                    ]
                  ]
                )
            else:
                await client.send_message(event.sender_id, "SEND PHOTO")
    else:
        await client.send_message(event.sender_id, "ONLY X MODS CAN USE THIS COMMAND")

@client.on(events.CallbackQuery(data='send'))
async def submitcb(event):
    await client.edit_message(event.sender_id, event.message_id, buttons=Button.clear())
    await client.send_file(trade_channel, user_cache[event.sender_id]['image'], caption = user_cache[event.sender_id]['text']
        ,
        buttons=[
        [
            Button.inline('COMPLETED', 'completed')
        ],
        [
            Button.inline('SELLER REFUSED', 'seller')
        ],
        [
            Button.inline('BUYER REFUSED', 'buyer')
        ],
        [
            Button.inline('SELLER SCAMMED', 'scamseller')
        ],
        [
            Button.inline('BUYER SCAMMED', 'buyerscam')
        ]
       ]
      )

@client.on(events.CallbackQuery(data='delete'))
async def deletecb(event):
    await client.edit_message(event.sender_id, event.message_id, "RESPONSE DELETED", buttons=Button.clear())

@client.on(events.CallbackQuery(data='completed'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(trade_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(completed_channel, event.message_id, trade_channel)
        await client.send_message(completed_channel, "Marked as completed by @"+fucker.username)
        await client.delete_messages(trade_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)

@client.on(events.CallbackQuery(data='seller'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(trade_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(betrayed_channel, event.message_id, trade_channel)
        await client.send_message(betrayed_channel, "Seller betrayed to give pokemon. Marked as by @"+fucker.username+"\n\n+1 warn to seller. (4 warns = ban from auction grp)")
        await client.delete_messages(trade_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)

@client.on(events.CallbackQuery(data='scamseller'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(trade_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(betrayed_channel, event.message_id, trade_channel)
        await client.send_message(betrayed_channel, "Seller betrayed to give pokemon. Marked by @"+fucker.username+"\n\n+1 warn to seller. (4 warns = ban from auction grp)")
        await client.delete_messages(trade_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)

@client.on(events.CallbackQuery(data='buyerscam'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(trade_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(scammer_channel, event.message_id, trade_channel)
        await client.send_message(scammer_channel, "SELLER scammed buyer . Marked by @"+fucker.username+"\n\nTIME TO GBAN MUHAHAHAHA")
        await client.delete_messages(trade_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)

@client.on(events.CallbackQuery(data='buyer'))
async def approvecb(event):
    fuck = event.sender_id
    user_id = event.sender_id
    fucker = await event.get_sender()
    if user_id in xmods:
        noyou = await event.get_sender()
        sender = await event.get_sender()
        await client.edit_message(trade_channel, event.message_id, buttons=Button.clear())
        await client.forward_messages(scammer_channel, event.message_id, log_channel)
        await client.send_message(scammer_channel, "BUYER scammed buyer. Marked by @"+fucker.username+"\n\nTIME TO GBAN MUHAHAHAHA")
        await client.delete_messages(trade_channel, event.message_id)
    else:
        await event.answer('You are not the auctioneer', alert=True)


client.start()
client.run_until_disconnected()
