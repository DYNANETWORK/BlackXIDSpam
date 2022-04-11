import asyncio
import os
import random
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from BlackXSpam import Bla, Bla2, Bla3, Bla4, Bla5 , Bla6, Bla7, Bla8, Bla9, Bla10, Bla11, Bla12, Bla13, Bla14, Bla15, Bla16, Bla17, Bla18, Bla19, Bla20, Bla21, Bla22, Bla23, Bla24, Bla25, Bla26, Bla27, Bla28, Bla29, Bla30, Bla31, Bla32, Bla33, Bla34, Bla35, Bla36, Bla37, Bla38, Bla39, Bla40, SUDO_USERS
from resources.data import BlackX
from .. import CMD_HNDLR as hl
  
    
@Bla.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla2.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla3.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla4.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla5.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla6.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla7.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla8.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla9.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla10.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla11.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla12.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla13.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla14.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla15.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla16.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla17.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla18.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla19.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla20.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla21.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bka22.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla23.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla24.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla25.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla26.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla27.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla28.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla29.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla30.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla31.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla32.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla33.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla34.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla35.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla36.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla37.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla38.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla39.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
@Bla40.on(events.NewMessage(incoming=True, pattern=r"\%sabuse(?: |$)(.*)" % hl))
async def _(e):
    usage = "**Module Name = Abuse**\n\nCommand:\n\n .abuse <Username of User>\n\nit will continuously abuse until you restart!!."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        BlackX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        bitxh = await e.get_reply_message()
        if len(Black) == 1:
            user = str(Black[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in BlackX:
                text = f"I can't abuse BlackX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"This Guy is a Sudo User."
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                c = a.first_name
                name = f"[{c}](tg://user?id={g})"
                caption1 =f"{name} GAND FATT GYII KYA HIJRE KI AULAAD"
                caption2 =f"{name} **RANDI KE PILLLE**"
                caption3 =f" {name} 𝑪𝑯𝑯𝑯𝑯𝑯𝑼𝑼𝑼𝑼𝑼𝑫𝑫𝑫𝑫 𝑮𝒀𝑨𝑨𝑨𝑨𝑨𝑨𝑨 𝑳𝑶𝑽𝑽𝑽𝑽𝑽𝑫𝑫𝑬𝑬 𝑻𝑼𝑼𝑼𝑼"
                caption4 =f" {name} 𝕋𝕖𝕣𝕚 𝕄𝕒𝕒 𝕂𝕚 𝕏𝕙𝕠𝕥 𝕓𝕒𝕕𝕙𝕧𝕖"
                caption5 =f"{name} **ISKE MAA KI CHUTT LELO FREE FULL NIGHT**"
                caption6 =f" {name} __TERE MAA KI CHUTT MASTT SOFT SOFT HE__ 🤤"
                caption7 =f"# {name} TERE MAA KI CHUT ME MERAA LUNDD"
                caption8 =f"{name} **RAANDD KAA PILLAAA**"
                caption9 =f"{name} 𝙄𝙎𝙆𝙄 𝘽𝙃𝙀𝙉 𝙈𝙀𝙍𝘼 𝙇𝙐𝙉𝘿 𝘾𝙃𝙊𝙊𝙎𝙏𝙄𝙄 𝙃𝘼𝙄"
                caption10 =f"{name} __AGAYA SWADH__"
                caption11 =f"{name} **TERI MAAA**"
                caption12 =f"**MERE SE**"
                caption13 =f"**Rozz CHUDTII**"
                caption14 =f"__Haiii__"
                caption15 =f"{name} TERE BHEN KO CHODU"
                caption16 =f"🆃🅰🅿🅰"
                caption17 =f"🆃🅰🅿"
                caption18 =f"🆃🅰🅿🅰"
                caption18 =f"🆃🅰🅿"
                caption20 =f"__NON STOP__"
                caption21 =f"{name} 𝗧𝗘𝗥𝗜 𝗠𝗔𝗔 𝗠𝗘𝗥𝗘 𝗟𝗨𝗡𝗗 𝗟𝗘 𝗡𝗔𝗖𝗛𝗧𝗜 𝗛𝗘"
                caption22 =f"🤤"
                caption23 =f"{name} __TERI MAA MST ARAAM DETI HE__🤤🤤"
                caption24 =f"{name} __KE BHEN KI CHUT LELO FULL NIGHT FREEE__"
                caption25 =f"{name} __KI BHEN RANDIII__"
                caption26 =f"{name} __ISKE BHEN MST MARI RANDI__ 🤤🤤"
                caption27 =f"😂🖕🤣"
                caption28 =f"😂"
                caption29 =f"__EK RUPAY KI PEPSI {name} KI NAANI SEXYY__"
                caption30 =f"{name} **ISKI BHEN MERI PERSONAL HE MENE BOHOT CHODAA HE USKO__ \n\n __DM {name} FOR PERSONAL RANDI__"
                fuk = e.chat_id
                async with e.client.action(fuk, "typing"):
                        await e.client.send_message(fuk, caption1)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption2)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption3)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption4)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption5)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption6)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption7)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption8)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption9)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption10)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption11)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption12)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption13)
                        await asyncio.sleep(0.4)
                        await e.client.send_message(fuk, caption14)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption15)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption16)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption17)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption18)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption19)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption20)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption21)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption22)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption23)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption24)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption25)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption26)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption27)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption28)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption29)
                        await asyncio.sleep(0.3)
                        await e.client.send_message(fuk, caption30)
                        await asyncio.sleep(0.3)

        else:
             await e.reply(usage)
