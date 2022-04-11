# MAMBA KA SPAM - Spam Userbots 
# @BlackXSpam | Keep Credits @MAMBA_NETWORK !!
 
import os
import sys
from BlackXSpam import Bla, Bla2, Bla3, Bla4, Bla5 , Bla6, Bla7, Bla8, Bla9, Bla10, Bla11, Bla12, Bla13, Bla14, Bla15, Bla16, Bla17, Bla18, Bla19, Bla20, Bla21, Bla22, Bla23, Bla24, Bla25, Bla26, Bla27, Bla28, Bla29, Bla30, Bla31, Bla32, Bla33, Bla34, Bla35, Bla36, Bla37, Bla38, Bla39, Bla40, SUDO_USERS, OWNER_ID
from BlackXSpam import ALIVE_NAME, ALIVE_PIC, ALIVE_TEXT, mightyversion
from .. import CMD_HNDLR as hl
from telethon import events, version
from telethon.tl.functions.users import GetFullUserRequest
from time import time
from datetime import datetime
 
mention = f"[{ALIVE_NAME}](tg://user?id={OWNER_ID})"
 
def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
 
    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)
 
    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
 
    time_list.reverse()
    ping_time += ":".join(time_list)
 
    return ping_time
 
@Bla.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla2.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla3.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla4.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla5.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla6.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla7.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla8.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla9.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla10.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla11.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla12.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla13.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla14.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla15.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla16.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla17.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla18.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla19.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla20.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla21.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla22.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla23.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla24.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla25.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla26.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla27.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla28.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla29.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla30.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla31.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla32.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla33.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla34.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla35.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla36.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla37.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla38.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla39.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
@Bla40.on(events.NewMessage(incoming=True, pattern=r"\%sping(?: |$)(.*)" % hl))
async def ping(e):
    if e.sender_id in SUDO_USERS:
            start = datetime.now()
            check = await e.reply("𝙋𝙤𝙣𝙜!")
            end = datetime.now()
            ms = (end-start).microseconds / 1000
            user = await e.client(GetFullUserRequest(e.sender_id))
            firstname = user.user.first_name
            userid = user.user.id
    if userid == OWNER_ID:
        await check.edit(f"█▀█ █▀█ █▄░█ █▀▀\n█▀▀ █▄█ █░▀█ █▄█\n\n    ⚡ 𝐁𝐥𝐚𝐜𝐤 𝐗 𝐒𝐩𝐚𝐦⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐎𝐰𝐧𝐞𝐫 : [{firstname}](tg://user?id={userid})")
    else:
        await check.edit(f"█▀█ █▀█ █▄░█ █▀▀\n█▀▀ █▄█ █░▀█ █▄█\n\n    ⚡ 𝐁𝐥𝐚𝐜𝐤 𝐗 𝐒𝐩𝐚𝐦⚡\n\n𝐏𝐢𝐧𝐠 : `{ms}` ᴍs\n𝐒𝐮𝐝𝐨 𝐔𝐬𝐞𝐫 : [{firstname}](tg://user?id={userid})")
 
# ALIVE
 
BLA_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/95e5058bdc80e0fea8626.jpg"
 
BLA_TEXT = ALIVE_TEXT if ALIVE_TEXT else "╚»★ 𝗕𝗹𝗮𝗰𝗸𝗫𝗦𝗽𝗮𝗺 𝗶𝘀 𝗛𝗲𝗿𝗲 ★«╝"
 
 
 
   
@Bla.on(events.NewMessage(incoming=True, pattern=r"\%salive" % hl))
async def alive(event):
    if event.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "𝘊𝘩𝘦𝘤𝘬𝘪𝘯𝘨..."
        check = await event.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await check.delete()
        await Bla.send_file(event.chat_id, MIG_PIC, caption=f"{Bla_TEXT}\n\n════════════════════\n⚡ 𝐏𝐢𝐧𝐠 : {ms}ᵐˢ\n⚡ 𝐎𝐰𝐧𝐞𝐫 : {mention}\n⚡ 𝐁𝐥𝐚𝐜𝐤 𝐗 𝐒𝐩𝐚𝐦 : `{blackversion}`\n⚡ 𝐏𝐲𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `3.9.6`\n⚡ 𝐓𝐞𝐥𝐞𝐭𝐡𝐨𝐧 𝐕𝐞𝐫𝐬𝐢𝐨𝐧 : `{version.__version__}`\n⚡ 𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩 : [𝗝𝗼𝗶𝗻](t.me/MAMBA_X_SUPPORT)\n⚡ 𝐔𝐩𝐝𝐚𝐭𝐞𝐬 𝐂𝐡𝐚𝐧𝐧𝐞𝐥 : [𝗝𝗼𝗶𝗻](t.me/MAMBA_NETWORK)\n════════════════════\n\n                  ✨ [𝐑𝐄𝐏𝐎](https://github.com/SUKHPAL443/BlackXIDSpam) ✨")
        
        
   
# help
 
HELP_PIC = "https://telegra.ph/file/95e5058bdc80e0fea8626.jpg"
 
BlackX = "╚»★ 𝗕𝗹𝗮𝗰𝗸 𝗫 𝗦𝗽𝗮𝗺 𝗛𝗲𝗹𝗽 ★«╝\n\n"
 
BlackX += f"__ᴄᴍᴅs ᴀᴠᴀɪʟᴀʙʟᴇ ɪɴ ᴍɪɢʜᴛʏ x sᴘᴀᴍ__\n\n"
 
BlackX += f"𝙐𝙨𝙚𝙧𝘽𝙤𝙩 𝘾𝙢𝙙𝙨\n\n"
 
BlackX += f" `{hl}ping` - `{hl}alive` - `{hl}setpic` - `{hl}delpic` - `{hl}setname` - `{hl}setbio` - `{hl}inviteall` - `{hl}restart` - `{hl}update` - `{hl}stats` - `{hl}addsudo` \n\n"
 
BlackX += f"𝙅𝙤𝙞𝙣/𝙇𝙚𝙖𝙫𝙚 𝘾𝙢𝙙𝙨\n\n"
 
BlackX += f" `{hl}join` - `{hl}pjoin` - `{hl}leave`\n\n"
 
BlackX += f"𝙎𝙥𝙖𝙢/𝙍𝙖𝙞𝙙 𝘾𝙢𝙙𝙨\n\n"
 
BlackX += f" `{hl}spam` - `{hl}bigspam` - `{hl}delayspam` - `{hl}ppspam` \n\n `{hl}abuse` \n\n `{hl}raid` - `{hl}replyraid` - `{hl}dreplyraid` - `{hl}delayraid` \n\n"
 
BlackX += f"𝘿𝙈/𝙀𝙘𝙝𝙤 𝘾𝙢𝙙𝙨\n\n"
 
BlackX += f" `{hl}dm` - `{hl}dmraid` - `{hl}dmspam` \n\n `{hl}addecho` - `{hl}rmecho` \n"
 
BlackX += f"\n[𝘒𝘯𝘰𝘸 𝘔𝘰𝘳𝘦 𝘈𝘣𝘰𝘶𝘵 𝘛𝘩𝘦𝘴𝘦 𝘊𝘔𝘋𝘚](t.me/MAMBA_NETWORK/)\n\n"
 
BlackX += f"[✨ Updates ✨](t.me/MAMBA_NETWORK)       [✨ Support ✨](t.me/MAMBA_X_SUPPORT)\n"
 
@Bla.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):
    if event.sender_id in SUDO_USERS:
     await Bla.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=BlackX)                                                         
 
 
@Bla.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla2.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla3.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla4.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla5.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla6.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla7.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla8.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla9.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla10.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla11.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla12.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla13.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla14.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla15.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla16.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla17.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla18.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla19.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla20.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla21.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla22.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla23.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla24.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla25.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla26.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla27.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla28.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla29.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla30.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla31.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla32.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla33.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla34.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla35.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla36.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla37.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla38.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla39.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
@Bla40.on(events.NewMessage(incoming=True, pattern=r"\%srestart(?: |$)(.*)" % hl))
async def restart(e):
    if e.sender_id in SUDO_USERS:
        text = "𝗥𝗲𝘀𝘁𝗮𝗿𝘁𝗶𝗻𝗴 𝗬𝗼𝘂𝗿 𝗕𝗹𝗮𝗰𝗸𝗫𝗦𝗽𝗮𝗺...n\nPlease Wait For Few Seconds !!"
        await e.reply(text, parse_mode=None, link_preview=None)
        try:
            await Bla.disconnect()
        except Exception:
            pass
        try:
            await Bla2.disconnect()
        except Exception:
            pass
        try:
            await Bla3.disconnect()
        except Exception:
            pass
        try:
            await Bla4.disconnect()
        except Exception:
            pass
        try:
            await Bla5.disconnect()
        except Exception:
            pass
        try:
            await Bla6.disconnect()
        except Exception:
            pass
        try:
            await Bla7.disconnect()
        except Exception:
            pass
        try:
            await Bla8.disconnect()
        except Exception:
            pass
        try:
            await Bla9.disconnect()
        except Exception:
            pass
        try:
            await Bla10.disconnect()
        except Exception:
            pass
        try:
            await Bla11.disconnect()
        except Exception:
            pass
        try:
            await Bla12.disconnect()
        except Exception:
            pass
        try:
            await Bla13.disconnect()
        except Exception:
            pass
        try:
            await Bla14.disconnect()
        except Exception:
            pass
        try:
            await Bla15.disconnect()
        except Exception:
            pass
        try:
            await Bla16.disconnect()
        except Exception:
            pass
        try:
            await Bla17.disconnect()
        except Exception:
            pass
        try:
            await Bla18.disconnect()
        except Exception:
            pass
        try:
            await Bla19.disconnect()
        except Exception:
            pass
        try:
            await Bla20.disconnect()
        except Exception:
            pass
        try:
            await Bla21.disconnect()
        except Exception:
            pass
        try:
            await Bla22.disconnect()
        except Exception:
            pass
        try:
            await Bla23.disconnect()
        except Exception:
            pass
        try:
            await Bla24.disconnect()
        except Exception:
            pass
        try:
            await Bla25.disconnect()
        except Exception:
            pass
        try:
            await Bla26.disconnect()
        except Exception:
            pass
        try:
            await Bla27.disconnect()
        except Exception:
            pass
        try:
            await Bla28.disconnect()
        except Exception:
            pass
        try:
            await Bla29.disconnect()
        except Exception:
            pass
        try:
            await Bla30.disconnect()
        except Exception:
            pass
        try:
            await Bla31.disconnect()
        except Exception:
            pass
        try:
            await Bla32.disconnect()
        except Exception:
            pass
        try:
            await Bla33.disconnect()
        except Exception:
            pass
        try:
            await Bla34.disconnect()
        except Exception:
            pass
        try:
            await Bla35.disconnect()
        except Exception:
            pass
        try:
            await Bla36.disconnect()
        except Exception:
            pass
        try:
            await Bla37.disconnect()
        except Exception:
            pass
        try:
            await Bla38.disconnect()
        except Exception:
            pass
        try:
            await Bla39.disconnect()
        except Exception:
            pass
        try:
            await Bla40.disconnect()
        except Exception:
            pass
 
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
 
