from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print(
    """\n.
╔══╗╔╗──╔═══╦═══╦╗╔═╗
║╔╗║║║──║╔═╗║╔═╗║║║╔╝
║╚╝╚╣║──║║─║║║─╚╣╚╝╝
║╔═╗║║─╔╣╚═╝║║─╔╣╔╗║
║╚═╝║╚═╝║╔═╗║╚═╝║║║╚╗
╚═══╩═══╩╝─╚╩═══╩╝╚═╝"""
)

print("\n • Telethon String Session •")

print("\n\nEnter Your Valid Details To Continue!\n\n")

        
APP_ID = int(input("\nEnter APP ID Here : "))
API_HASH = input("\nEnter API HASH Here : ")


try:
   with TelegramClient(StringSession(), APP_ID, API_HASH) as Black:
       print("\nSTRING SESSION GENERATED SUCCESSFULLY !!\nCHECK YOUR SAVED MASSAGES.\nString is a Sensitive Data, Don't Share it With Anyone. ")
       Black.send_message("me", f"**Black X Spam Session :**\n\n`{Black.session.save()}`\n\n__Don't Share it With Anyone.__")
       
except Exception as e:
    print(f"{e}") 
