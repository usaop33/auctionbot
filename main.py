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
LOG_CHANNEL = os.environ.get('LOG_CHANNEL', None)
POST_CHANNEL = os.environ.get('POST_CHANNEL', None)

api_id = API_ID
api_hash = API_HASH
bot_token = TOKEN
log_channel = LOG_CHANNEL
post_channel = POST_CHANNEL
log_channel = int(log_channel)
post_channel = int(post_channel)

client = TelegramClient('konek', api_id, api_hash).start(bot_token=bot_token) #i dont really understand it lol but without this bot wont work

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', #copy pasted from telethon docs lol..... so usually it logs error
                    level=logging.WARNING)

xmods = 1037179104, 1174476949, 1786637879, 790824807, 5058417875, 1720329781, 1749188073, 1094810637, 1094810637, 5174776869


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

@client.on(events.NewMessage(pattern='/sell'))
async def sell(event):
    sender = await event.get_sender()
    if sender.username:
        await client.send_message(event.sender_id, "Hello @"+sender.username+"!\n\nWould you like to sell something in auction"
            ,
            buttons=[
            [
                Button.inline('Yes', 'yes')
            ],
            [
                Button.inline('No', 'No')
            ]
          ]
        )
    else:
        await client.send_message(event.sender_id, "Hello!\n\nWould you like to sell something in auction"
            ,
            buttons=[
            [
                Button.inline('Yes', 'yes')
            ],
            [
                Button.inline('No', 'No')
            ]
          ]
        )

@client.on(events.CallbackQuery(data='No'))
async def nocb(event):
    await client.edit_message(event.sender_id, event.message_id, "Ok! I understand", buttons=Button.clear())

@client.on(events.CallbackQuery(data='yes'))
async def yescb(event):
    await client.edit_message(event.sender_id, event.message_id, "So what would you like to sell?"
        ,
        buttons=[
        [
            Button.inline('LEGENDARY', 'legendary')
        ],
        [
            Button.inline('0L/Non Legendary', 'nonlegendary')
        ],
        [
            Button.inline('SHINY', 'shiny')
        ],
        [
            Button.inline('TMS', 'tms')
        ]
     ]
    )

@client.on(events.CallbackQuery(data='legendary'))
async def legendarycb(event):
    await client.edit_message(event.sender_id, event.message_id, 'OK! Legendary', buttons=Button.clear())
    sender = await event.get_sender()
    user_id = event.sender_id
    sheesh = str(user_id)
    if sender.username:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ligma'] = name
                    user_cache[user_id]['name'] = {user_cache[user_id]['ligma'] : {}}
                    user_cache[user_id]['name'][user_cache[user_id]['ligma']]['ID'] = user_id
                    user_cache[user_id]['name'][user_cache[user_id]['ligma']]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Legendary\nUser id - "+sheesh+"\nUsername : @"+sender.username+"\n\nAbout Pokemon:- \n"+name+"\n\nEvs and Ivs:-\n"+lol+"\n\nMoveset:- \n"+lmao+"\n\nBase - "+ccc
                        user_cache[user_id]['name'][user_cache[user_id]['ligma']]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please send the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please send the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please send the pic with nature too. If the pic isnt present error will happen again")
    else:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ligma'] = name
                    user_cache[user_id]['name'] = {user_cache[user_id]['ligma'] : {}}
                    user_cache[user_id]['name'][user_cache[user_id]['ligma']]['ID'] = user_id
                    user_cache[user_id]['name'][user_cache[user_id]['ligma']]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Legendary\nUser id - "+sheesh+"\n\nAbout Pokemon:- \n"+name+"\n\nEvs and Ivs:-\n"+lol+"\n\nMoveset:- \n"+lmao+"\n\nBase - "+ccc
                        user_cache[user_id]['name'][user_cache[user_id]['ligma']]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please send the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please send the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please send the pic with nature too. If the pic isnt present error will happen again")



@client.on(events.CallbackQuery(data='submit'))
async def submitcb(event):
    await client.edit_message(event.sender_id, event.message_id, user_cache[event.sender_id]['name'][user_cache[user_id]['ligma']]['text']+"\n\nSUBMITED\nCheck @pendingauctionpokemon to see status of your pokemon", buttons=Button.clear())
    await client.send_file(log_channel, user_cache[event.sender_id]['name'][user_cache[user_id]['ligma']]['image'], caption = user_cache[event.sender_id]['name'][user_cache[user_id]['ligma']]['text']
        ,
        buttons=[
        [
            Button.inline('APPROVE', 'approve'),
            Button.inline('REJECT', 'reject')
        ],
        [
            Button.inline('REJECT - INCOMPLETE DETAILS', 'rejectinco')
        ],
        [
            Button.inline('REJECT - TRASH POKEMON', 'rejt')
        ],
        [
            Button.inline('REPORT AS SCAMMER', 'scammer')
        ]
      ]
    )

@client.on(events.CallbackQuery(data='delete'))
async def deletecb(event):
    await client.edit_message(event.sender_id, event.message_id, "RESPONSE DELETED", buttons=Button.clear())

@client.on(events.CallbackQuery(data='approve'))
async def approvecb(event):
    user_id = event.sender_id
    if user_id in xmods:
        sender = await event.get_sender()
        await client.edit_message(log_channel, event.message_id, user_cache[event.sender_id]['name'][user_cache[user_id]['ligma']]['text']+"\n\nApproved", buttons=Button.clear())
        await client.send_file(post_channel, user_cache[event.sender_id]['name'][user_cache[user_id]['ligma']]['image'], caption = user_cache[event.sender_id]['name'][user_cache[user_id]['ligma']]['text'])
        await client.send_file(user_cache[event.sender_id]['name'][user_cache[user_id]['ligma']]['ID'], user_cache[event.sender_id]['name'][user_cache[user_id]['ligma']]['image'], caption = user_cache[event.sender_id]['name'][user_cache[user_id]['ligma']]['text']+"\n\nApproved by")
    else:
        await event.answer('You are not the auctioneer', alert=True)


@client.on(events.CallbackQuery(data= 'reject'))
async def rejectcb(event):
    user_id = event.sender_id
    if user_id in xmods:
        sender = await event.get_sender()
        if sender.username:
            await client.edit_message(log_channel, event.message_id, user_cache[event.sender_id]['text']+"\n\n#REJECTED \nRejected by @"+sender.username+"  (`"+str(user_id)+"`)", buttons=Button.clear())
            await client.send_file(user_cache[event.sender_id]['ID'], user_cache[event.sender_id]['image'], caption = "\n\nIt was Rejected\n\n"+user_cache[event.sender_id]['text']+"\nRejected by @"+sender.username+"  (`"+str(user_id)+"`)\n\n#REJECTED")
        else:
            await client.edit_message(log_channel, event.message_id, user_cache[event.sender_id]['text']+"\n\n#REJECTED \nRejected by "+sender.first_name+"  (`"+str(user_id)+"`)", buttons=Button.clear())
            await client.send_file(user_cache[event.sender_id]['ID'], user_cache[event.sender_id]['image'], caption = "\n\nIt was Rejected\n\n"+user_cache[event.sender_id]['text']+"\nRejected by "+sender.first_name+"  (`"+str(user_id)+"`)\n\n#REJECTED")
    else:
        await event.answer('You are not the auctioneer', alert=True)

@client.on(events.CallbackQuery(data= 'rejectinco'))
async def rejectcb(event):
    user_id = event.sender_id
    if user_id in xmods:
        sender = await event.get_sender()
        if sender.username:
            await client.edit_message(log_channel, event.message_id, user_cache[event.sender_id]['text']+"\n\n#REJECTED_INCOMPLETE_DETAILS \nRejected by @"+sender.username+"  (`"+str(user_id)+"`)", buttons=Button.clear())
            await client.send_file(user_cache[event.sender_id]['ID'], user_cache[event.sender_id]['image'], caption = "\n\nIt was Rejected\n\n"+user_cache[event.sender_id]['text']+"\nRejected by @"+sender.username+"  (`"+str(user_id)+"`)\n\n#REJECTED_INCOMPLETE_DETAILS")
        else:
            await client.edit_message(log_channel, event.message_id, user_cache[event.sender_id]['text']+"\n\n#REJECTED_INCOMPLETE_DETAILS \nRejected by "+sender.first_name+"  (`"+str(user_id)+"`)", buttons=Button.clear())
            await client.send_file(user_cache[event.sender_id]['ID'], user_cache[event.sender_id]['image'], caption = "\n\nIt was Rejected\n\n"+user_cache[event.sender_id]['text']+"\nRejected by "+sender.first_name+"  (`"+str(user_id)+"`)\n\n#REJECTED_INCOMPLETE_DETAILS")
    else:
        await event.answer('You are not the auctioneer', alert=True)

@client.on(events.CallbackQuery(data= 'rejt'))
async def rejectcb(event):
    user_id = event.sender_id
    if user_id in xmods:
        sender = await event.get_sender()
        if sender.username:
            await client.edit_message(log_channel, event.message_id, user_cache[event.sender_id]['text']+"\n\n#REJECTED_TRASH \nRejected by @"+sender.username+"  (`"+str(user_id)+"`)", buttons=Button.clear())
            await client.send_file(user_cache[event.sender_id]['ID'], user_cache[event.sender_id]['image'], caption = "\n\nIt was Rejected\n\n"+user_cache[event.sender_id]['text']+"\nRejected by @"+sender.username+"  (`"+str(user_id)+"`)\n\n#REJECTED_TRASH")
        else:
            await client.edit_message(log_channel, event.message_id, user_cache[event.sender_id]['text']+"\n\n#REJECTED_TRASH \nRejected by "+sender.first_name+"  (`"+str(user_id)+"`)", buttons=Button.clear())
            await client.send_file(user_cache[event.sender_id]['ID'], user_cache[event.sender_id]['image'], caption = "\n\nIt was Rejected\n\n"+user_cache[event.sender_id]['text']+"\nRejected by "+sender.first_name+"  (`"+str(user_id)+"`)\n\n#REJECTED_TRASH")
    else:
        await event.answer('You are not the auctioneer', alert=True)
        
@client.on(events.CallbackQuery(data= 'scammer'))
async def rejectcb(event):
    user_id = event.sender_id
    if user_id in xmods:
        await client.edit_message(log_channel, event.message_id, user_cache[event.sender_id]['text']+"\n\n#REPORTED_AS_SCAMMER", buttons=Button.clear())
        await client.send_file(user_cache[event.sender_id]['ID'], user_cache[event.sender_id]['image'], caption = "Reported as scammer\n\n"+user_cache[event.sender_id]['text']+"\n\n#SCAMMER")
        await client.send_file(-1001536273639, user_cache[event.sender_id]['image'], caption = "Reported as scammer\n\n"+user_cache[event.sender_id]['text']+"\n\n#SCAMMER")
    else:
        await event.answer('You are not the auctioneer', alert=True)


@client.on(events.CallbackQuery(data='nonlegendary'))
async def legendarycb(event):
    await client.edit_message(event.sender_id, event.message_id, 'OK! Non-Legendary', buttons=Button.clear())
    sender = await event.get_sender()
    user_id = event.sender_id
    sheesh = str(user_id)
    if sender.username:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ID'] = user_id
                    user_cache[user_id]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Non_Legendary\nUser id - "+sheesh+"\nUsername : @"+sender.username+"\n\nAbout Pokemon:- \n"+name+"\n\nEvs and Ivs:-\n"+lol+"\n\nMoveset:- \n"+lmao+"\n\nBase - "+ccc
                        user_cache[user_id]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please send the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please send the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please send the pic with nature too. If the pic isnt present error will happen again")
    else:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ID'] = user_id
                    user_cache[user_id]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Non_Legendary\nUser id - "+sheesh+"\n\nAbout Pokemon:- \n"+name+"\n\nEvs and Ivs:-\n"+lol+"\n\nMoveset:- \n"+lmao+"\n\nBase - "+ccc
                        user_cache[user_id]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please send the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please send the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please send the pic with nature too. If the pic isnt present error will happen again")

@client.on(events.CallbackQuery(data='shiny'))
async def legendarycb(event):
    await client.edit_message(event.sender_id, event.message_id, 'OK! Shiny', buttons=Button.clear())
    sender = await event.get_sender()
    user_id = event.sender_id
    sheesh = str(user_id)
    if sender.username:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ID'] = user_id
                    user_cache[user_id]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Shiny\nUser id - "+sheesh+"\nUsername : @"+sender.username+"\n\nAbout Pokemon:- \n"+name+"\n\nEvs and Ivs:-\n"+lol+"\n\nMoveset:- \n"+lmao+"\n\nBase - "+ccc
                        user_cache[user_id]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please send the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please send the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please send the pic with nature too. If the pic isnt present error will happen again")
    else:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Nature Pic of pokemon')
            response = await conv.get_response(timeout = 90000)
            if response.media:
                name = response.text
                await conv.send_message('Forward Evs Pic of pokemon')
                respo =  await conv.get_response(timeout = 90000)
                if respo.media:
                    lol = respo.text
                    huh = respo.media
                    user_cache[user_id] = {}
                    user_cache[user_id]['ID'] = user_id
                    user_cache[user_id]['image'] = huh
                    await conv.send_message('Forward moveset pic of pokemon')
                    x = await conv.get_response(timeout = 90000)
                    if x.media:
                        lmao = x.text
                        await conv.send_message('Set base')
                        bbb = await conv.get_response(timeout = 90000)
                        ccc = bbb.text
                        hmm = "#Shiny\nUser id - "+sheesh+"\n\nAbout Pokemon:- \n"+name+"\n\nEvs and Ivs:-\n"+lol+"\n\nMoveset:- \n"+lmao+"\n\nBase - "+ccc
                        user_cache[user_id]['text'] = hmm
                        await client.send_file(event.sender_id, file = huh, caption = hmm
                            ,
                            buttons=[
                            [
                                Button.inline('SUBMIT', 'submit')
                            ],
                            [
                                Button.inline('Delete', 'delete')
                            ]
                          ]
                        )
                    else:
                        await client.send_message(user_id, "A error occured please restart the process. Please send the pic with moveset too. If the pic isnt present error will happen again")
                else:
                    await client.send_message(user_id, "A error occured please restart the process. Please send the pic with evs and ivs too. If the pic isnt present error will happen again")
            else:
                await client.send_message(user_id, "A error occured please restart the process. Please send the pic with nature too. If the pic isnt present error will happen again")

@client.on(events.CallbackQuery(data='tms'))
async def tmscb(event):
    await client.edit_message(event.sender_id, event.message_id, 'OK! TMS', buttons=Button.clear())
    sender = await event.get_sender()
    user_id = event.sender_id
    sheesh = str(user_id)
    if sender.username:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Tm from hexa')
            response = await conv.get_response(timeout = 90000)
            name = response.text
            await conv.send_message('Set base')
            respo =  await conv.get_response(timeout = 90000)
            lol = respo.text
            huh = 'https://img.rankedboost.com/wp-content/uploads/2018/11/Pokemon-Lets-Go-TMs-300x200.png'
            user_cache[user_id] = {}
            user_cache[user_id]['ID'] = user_id
            user_cache[user_id]['image'] = huh
            hmm = "#TM\nUser id - "+sheesh+"\nUsername : @"+sender.username+"\n\nTM:- \n"+name+"\n\nBase - "+lol
            user_cache[user_id]['text'] = hmm
            await client.send_file(event.sender_id, file = huh, caption = hmm
                ,
                buttons=[
                [
                    Button.inline('SUBMIT', 'submit')
                ],
                [
                    Button.inline('Delete', 'delete')
                ]
              ]
            )
    else:
        async with client.conversation(user_id) as conv:
            await conv.send_message('Forward Tm from hexa')
            response = await conv.get_response(timeout = 90000)
            name = response.text
            await conv.send_message('Set base')
            respo =  await conv.get_response(timeout = 90000)
            lol = respo.text
            huh = 'https://img.rankedboost.com/wp-content/uploads/2018/11/Pokemon-Lets-Go-TMs-300x200.png'
            user_cache[user_id] = {}
            user_cache[user_id]['ID'] = user_id
            user_cache[user_id]['image'] = huh
            hmm = "#TM\nUser id - "+sheesh+"\n\nTM:- \n"+name+"\n\nBase - "+lol
            user_cache[user_id]['text'] = hmm
            await client.send_file(event.sender_id, file = huh, caption = hmm
                ,
                buttons=[
                [
                    Button.inline('SUBMIT', 'submit')
                ],
                [
                    Button.inline('Delete', 'delete')
                ]
              ]
            )









client.start()
client.run_until_disconnected()
