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
            check = await e.reply("????????????????!")
            end = datetime.now()
            ms = (end-start).microseconds / 1000
            user = await e.client(GetFullUserRequest(e.sender_id))
            firstname = user.user.first_name
            userid = user.user.id
    if userid == OWNER_ID:
        await check.edit(f"????????????????????????????????????????????????\n????????????????????????????????????????????????\n\n    ??? ???????????????????? ???? ???????????????????\n\n???????????????? : `{ms}` ???s\n???????????????????? : [{firstname}](tg://user?id={userid})")
    else:
        await check.edit(f"????????????????????????????????????????????????\n????????????????????????????????????????????????\n\n    ??? ???????????????????? ???? ???????????????????\n\n???????????????? : `{ms}` ???s\n???????????????? ???????????????? : [{firstname}](tg://user?id={userid})")
 
# ALIVE
 
BLA_PIC = ALIVE_PIC if ALIVE_PIC else "https://telegra.ph/file/95e5058bdc80e0fea8626.jpg"
 
BLA_TEXT = ALIVE_TEXT if ALIVE_TEXT else "???????? ???????????????????????????????????????? ???????? ???????????????? ????????"
 
 
 
   
@Bla.on(events.NewMessage(incoming=True, pattern=r"\%salive" % hl))
async def alive(event):
    if event.sender_id in SUDO_USERS:
        start = datetime.now()
        text = "????????????????????????????????..."
        check = await event.reply(text, parse_mode=None, link_preview=None)
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        await check.delete()
        await Bla.send_file(event.chat_id, MIG_PIC, caption=f"{Bla_TEXT}\n\n????????????????????????????????????????????????????????????\n??? ???????????????? : {ms}?????\n??? ???????????????????? : {mention}\n??? ???????????????????? ???? ???????????????? : `{blackversion}`\n??? ???????????????????????? ???????????????????????????? : `3.9.6`\n??? ???????????????????????????????? ???????????????????????????? : `{version.__version__}`\n??? ???????????????????????????? ???????????????????? : [????????????????](t.me/MAMBA_X_SUPPORT)\n??? ???????????????????????????? ???????????????????????????? : [????????????????](t.me/MAMBA_NETWORK)\n????????????????????????????????????????????????????????????\n\n                  ??? [????????????????](https://github.com/SUKHPAL443/BlackXIDSpam) ???")
        
        
   
# help
 
HELP_PIC = "https://telegra.ph/file/95e5058bdc80e0fea8626.jpg"
 
BlackX = "???????? ???????????????????? ???? ???????????????? ???????????????? ????????\n\n"
 
BlackX += f"__?????????s ??????????????????????? ???? ?????????????? x s?????????__\n\n"
 
BlackX += f"???????????????????????????? ????????????????\n\n"
 
BlackX += f" `{hl}ping` - `{hl}alive` - `{hl}setpic` - `{hl}delpic` - `{hl}setname` - `{hl}setbio` - `{hl}inviteall` - `{hl}restart` - `{hl}update` - `{hl}stats` - `{hl}addsudo` \n\n"
 
BlackX += f"????????????????/???????????????????? ????????????????\n\n"
 
BlackX += f" `{hl}join` - `{hl}pjoin` - `{hl}leave`\n\n"
 
BlackX += f"????????????????/???????????????? ????????????????\n\n"
 
BlackX += f" `{hl}spam` - `{hl}bigspam` - `{hl}delayspam` - `{hl}ppspam` \n\n `{hl}abuse` \n\n `{hl}raid` - `{hl}replyraid` - `{hl}dreplyraid` - `{hl}delayraid` \n\n"
 
BlackX += f"????????/???????????????? ????????????????\n\n"
 
BlackX += f" `{hl}dm` - `{hl}dmraid` - `{hl}dmspam` \n\n `{hl}addecho` - `{hl}rmecho` \n"
 
BlackX += f"\n[???????????????? ???????????????? ???????????????????? ???????????????????? ????????????????](t.me/MAMBA_NETWORK/)\n\n"
 
BlackX += f"[??? Updates ???](t.me/MAMBA_NETWORK)       [??? Support ???](t.me/MAMBA_X_SUPPORT)\n"
 
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
        text = "???????????????????????????????????????? ???????????????? ????????????????????????????????????????...n\nPlease Wait For Few Seconds !!"
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
 
