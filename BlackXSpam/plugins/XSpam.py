async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
import random
import telethon.utils
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from BlackXSpam import Bla, Bla2, Bla3, Bla4, Bla5 , Bla6, Bla7, Bla8, Bla9, Bla10, Bla11, Bla12, Bla13, Bla14, Bla15, Bla16, Bla17, Bla18, Bla19, Bla20, Bla21, Bla22, Bla23, Bla24, Bla25, Bla26, Bla27, Bla28, Bla29, Bla30, Bla31, Bla32, Bla33, Bla34, Bla35, Bla36, Bla37, Bla38, Bla39, Bla40, SUDO_USERS
from .. import CMD_HNDLR as hl
from resources.data import BlackX, GROUP, PORMS

# spam

@Bla.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla11.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla12.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla13.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla14.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla15.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla16.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla17.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla18.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla19.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@Bla20.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        Black = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Black) == 2:
            message = str(Black[1])
            counter = int(Black[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(Black[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Black[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


#bigspam

@Bla.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla11.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla12.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla13.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla14.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla15.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla16.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla17.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla18.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla19.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@Bla20.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        Black = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(Black) == 2:
            message = str(Black[1])
            counter = int(Black[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(Black[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Black[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

#delayspam

@Bla.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla11.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla12.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla13.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla14.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla15.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla16.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla17.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla18.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla19.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@Bla20.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        Black = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        Blacksexy = Black[1:]
        if len(Blacksexy) == 2:
            message = str(Blacksexy[1])
            counter = int(Blacksexy[0])
            sleeptime = float(Black[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(Blacksexy[0])
            sleeptime = float(Black[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(Blacksexy[0])
            sleeptime = float(Black[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

#abuse

@Bla.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla2.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla3.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla4.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla5.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla6.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla7.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla8.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla9.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla10.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla11.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla12.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla13.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla14.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla15.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@bla16.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla17.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla18.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla19.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@Bla20.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **DM Spam**\n\nCommand:\n\n.dmspam <count> <username> <message to spam>\n\n.dmspam <count> <username> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        black = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 2)
        Blacksexy = black[1:]
        smex = await e.get_reply_message()
        if len(Blacksexy) == 2:
            user = str(Blacksexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in BlackX:
                text = f"I can't Dm To BlackX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(Blacksexy[1])
                counter = int(Black[0])
                await e.reply("😈 Dm Spam Started 😈")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:
            user = str(Blacksexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in BlackX:
                text = f"I can't Dm To BlackX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:           
                 counter = int(Black[0])
                 await e.reply("😈 Dm Spam Started 😈")
                 for _ in range(counter):
                     async with e.client.action(g, "document"):
                        smex = await e.client.send_file(g, smex, caption=smex.text)
                        await gifspam(e, smex) 
                        await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            user = str(Blacksexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in BlackX:
                text = f"I can't Dm To BlackX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(black[0])
                await e.reply("😈 Dm Spam Started 😈")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )       

# LΣGΣΠD | @ITZ_SUKHI

@Bla.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla2.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla3.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla4.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla5.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla6.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla7.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla8.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla9.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla10.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla11.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla12.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla13.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla14.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla15.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla16.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla17.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla18.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla19.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla20.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla21.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla22.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla23.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla24.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla25.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla26.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla27.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla28.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla29.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla30.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla31.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla32.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla33.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla34.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla35.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla36.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla37.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla38.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla39.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
@Bla40.on(events.NewMessage(incoming=True, pattern=r"\%spornspam(?: |$)(.*)" % hl))
async def pspam(e):
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        black = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(black) == 1:
            counter = int(black
                          [0])
            if int(e.chat_id) in GROUP:
                text = f"Sorry !! Bhosdike Jis Bande Ka bot Tu Use kar raha uska group hai ye bc sala chutiya sorry boss @ITZ_SUKHI. 🌚"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                 porrn = random.choice(PORMS)
                 for _ in range(counter):
                     async with e.client.action(e.chat_id, "document"):
                         smex = await e.client.send_file(e.chat_id, porrn)
                         await gifspam(e, smex) 
                     await asyncio.sleep(0.4)
        else:
            usage = f"**MODULE NAME : PORN SPAM** \n\n command: `{hl}pornspam <count>`"
            await e.reply(usage)

# By - LΣGΣΠD | @ITZ_SUKHIH
# For BlackXSpam | @BlackXSpam
# Keep Credits BlackXIDSpam !!

@Bla.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla2.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla3.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla4.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla5.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla6.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla7.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla8.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla9.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla10.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla11.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla12.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla13.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla14.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla15.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla16.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla17.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla18.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla19.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla20.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla21.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla22.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla23.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla24.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla25.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla26.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla27.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla28.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla29.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla30.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla31.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla32.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla33.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla34.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla35.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla36.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla37.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla38.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla39.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
@Bla40.on(events.NewMessage(incoming=True, pattern=r"\%sppspam(?: |$)(.*)" % hl))
async def ppspam(e):
    usage = f"**MODULE NAME : PRIVATELY PORM SPAM** \n\ncommand: {hl}ppspam <count> <group or account's username>\n\n**Note :** if Spamming In Group - Accounts Should Be in Both Chats (Obviously)"
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage)
        Black = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        if len(Black) == 2:
            user_chat = str(Black[1])
            uc = await e.client.get_peer_id(user_chat)
            if int(uc) in BlackX:
                legend = f"Sorry, I Can't Spam BlackX's Owner"
                await e.reply(legend, parse_mode=None, link_preview=None )
            elif int(uc) in GROUP:
                legend = f"Sorry, I Can't Spam There !! 🌚"
                await e.reply(legend, parse_mode=None, link_preview=None )
            else:
                counter = int(Black[0])
                await e.reply("Starting PormSpam !! 😈")
                for _ in range(counter):
                    p0rn = random.choice(PORMS)
                    async with e.client.action(uc, "document"):
                        await e.client.send_file(uc, p0rn)
                        await asyncio.sleep(0.4)
        else:
            await e.reply(usage)
