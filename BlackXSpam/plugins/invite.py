# By - LΣGΣΠD | @ITZ_SUKHI
# For BlackXSpam | @BlackXSpam
# From Kangers Import BlackMamba
# Keep Credits BlackMamba !!

import os
import sys
import random
from os import execl
import asyncio
import telethon.utils
from requests import get
from BlackXSpam import Bla, Bla2, Bla3, Bla4, Bla5 ,Bla6, Bla7, Bla8, Bla9, Bla10, Bla11, Bla12, Bla13, Bla14, Bla15, Bla16, Bla17, Bla18, Bla19, Mig20, Mig21, Mig22, Mig23, Mig24, Mig25, Mig26, Mig27, Mig28, Mig29, Mig30, Mig31, Mig32, Mig33, Mig34, Mig35, Mig36, Mig37, Mig38, Mig39, Mig40, DEV
from .. import CMD_HNDLR as hl
from telethon.tl import functions, types
from telethon import events
 
 
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError, InviteHashEmptyError, InviteHashExpiredError, InviteHashInvalidError)
from telethon.events import NewMessage
from telethon.tl.types import Channel, Chat, User
from telethon.tl.functions.channels import GetFullChannelRequest, InviteToChannelRequest, GetParticipantsRequest
from telethon.errors import FloodWaitError
from telethon.tl.functions.messages import GetHistoryRequest, CheckChatInviteRequest, GetFullChatRequest
from telethon.errors.rpcerrorlist import YouBlockedUserError
from urllib.error import HTTPError



async def get_chatinfo(event):
    chat = event.pattern_match.group(1)
    chat_info = None
    if chat:
        try:
            chat = int(chat)
        except ValueError:
            pass
    if not chat:
        if event.reply_to_msg_id:
            replied_msg = await event.get_reply_message()
            if replied_msg.fwd_from and replied_msg.fwd_from.channel_id is not None:
                chat = replied_msg.fwd_from.channel_id
        else:
            chat = event.chat_id
    try:
        chat_info = await event.client(GetFullChatRequest(chat))
    except:
        try:
            chat_info = await event.client(GetFullChannelRequest(chat))
        except ChannelInvalidError:
            await event.reply("`Invalid Channel/Group`")
            return None
        except ChannelPrivateError:
            await event.reply("`This is a Private Channel/Group or I Am Banned From There`")
            return None
        except ChannelPublicGroupNaError:
            await event.reply("`Channel or Supergroup Doesn't Exist`")
            return None
        except (TypeError, ValueError) as err:
            await event.reply("`Invalid Channel/Group`")
            return None
    return chat_info



def user_full_name(user):
    names = [user.first_name, user.last_name]
    names = [i for i in list(names) if i]
    full_name = ' '.join(names)
    return full_name

            
@Bla.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla2.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla3.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla4.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla5.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Mig6.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla7.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla8.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla9.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla10.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla11.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla12.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla13.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla14.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla15.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla16.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla17.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla18.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla19.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla20.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla21.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla22.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla23.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla24.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla25.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla26.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla27.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla28.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla29.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla30.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla31.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla32.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla33.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla34.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla35.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla36.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla37.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla38.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla39.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
@Bla40.on(events.NewMessage(incoming=True, pattern=r"\%sinviteall(?: |$)(.*)" % hl))
async def get_users(event):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗜𝗻𝘃𝗶𝘁𝗲𝗔𝗹𝗹\n\nCommand:\n\n.inviteall <group username/id/link>"
    if event.sender_id in DEV:
        sender = await event.get_sender() ; me = await event.client.get_me()
    if not sender.id == me.id:
        legend = await event.reply("__Processing... 🌚__")
    else:
    	legend = await event.edit("__Processing... 🌚__")
    legendop = await get_chatinfo(event) ; chat = await event.get_chat()
    if event.is_private:
              return await legend.edit("`Sorry, Can't Add Users Here..!`")    
    s = 0 ; f = 0 ; error = 'None'   
  
    await legend.edit("⚡ 𝐁𝐋𝐀𝐂𝐊 𝐗 𝐒𝐏𝐀𝐌 ⚡\n\n🔥 **Terminal Status** 🔥\n\n`Collecting Users..!! ✨`")
    async for user in event.client.iter_participants(legendop.full_chat.id):
                try:
                    if error.startswith("Too"):
                        return await legend.edit(f"⚡ 𝐁𝐋𝐀𝐂𝐊 𝐗 𝐒𝐏𝐀𝐌⚡\n\n**Terminal Finished With Error :**\n(`May Got Limit Error From Telethon Please Try Again Later`)\n**Error** : \n`{error}`\n\n🎉 Invited `{s}` People \n⚠️ Failed To Invite `{f}` People")
                    await asyncio.sleep(5)
                    await event.client(functions.channels.InviteToChannelRequest(channel=chat,users=[user.id]))
                    s = s + 1                                                    
                    await legend.edit(f"⚡ 𝐁𝐋𝐀𝐂𝐊 𝐗 𝐒𝐏𝐀𝐌 ⚡\n\n🔥 **Terminal Running...** 🔥\n\n🎉 Invited `{s}` People \n⚠️ Failed To Invite `{f}` People\n\n**‼️LastError :** `{error}`")                
                except Exception as e:
                    error = str(e) ; f = f + 1             
    return await legend.edit(f"⚡ 𝐁𝐋𝐀𝐂𝐊 𝐗 𝐒𝐏𝐀𝐌 ⚡\n\n🔥 **Terminal Finished** 🔥\n\n✨ Successfully Invited `{s}` People \n❌ Failed To Invite `{f}` People")
    
 
