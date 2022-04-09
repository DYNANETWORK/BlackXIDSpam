from telethon.sessions import StringSession
from telethon.sync import TelegramClient


print(
    """\n
╔══╗╔╗──╔═══╦═══╦╗╔═╗╔═╗╔═╦═══╦═╗╔═╦══╗╔═══╗
║╔╗║║║──║╔═╗║╔═╗║║║╔╝║║╚╝║║╔═╗║║╚╝║║╔╗║║╔═╗║
║╚╝╚╣║──║║─║║║─╚╣╚╝╝─║╔╗╔╗║║─║║╔╗╔╗║╚╝╚╣║─║║
║╔═╗║║─╔╣╚═╝║║─╔╣╔╗║─║║║║║║╚═╝║║║║║║╔═╗║╚═╝║
║╚═╝║╚═╝║╔═╗║╚═╝║║║╚╗║║║║║║╔═╗║║║║║║╚═╝║╔═╗║
╚═══╩═══╩╝─╚╩═══╩╝╚═╝╚╝╚╝╚╩╝─╚╩╝╚╝╚╩═══╩╝─╚╝
"""
)

print("\n  ### TERA STRING SESSION IDHR SE HI MILEGA GANDU ###")
print("\n >>>> BLACKMAMBA 2.0 IS BACK <<<<")
print("\n MERE DUSHMANO NE SOCHA HOGA KI BLACKMAMBA DAR GYA ABE MERI AULAD H TU BETA, AGAR SHER EK KADAM PICHE KAR LE TOO YE MAT SAMJHNA KI SHER DAR GYA, SHER APNE SHIKAR KO NISHANA BNA RHA HOTA HAI")

print("\n\n ABE CHUTIYE APNI DETAILS SAHI SE DAALNA FIR BOLTA HAI KI BOT ME CHUTIYAPA HAI SANJHA CHAL DAAL BE AB DETAILS !\n\n")

        
APP_ID = int(input("\n APNI APP ID DAAL BE JALDI KR: "))
API_HASH = input("\n APNI APP HASH DAAL BE JALDI KR  : ")


try:
   with TelegramClient(StringSession(), APP_ID, API_HASH) as Black:
       print("\nBC TERA STRING SESSION READY HO GYA H !!\nJAA SAVE MESSAGES ME JAAKR CHECK KR .\n@MAMBA_NETWORK JOIN HOJAA, CHUTIYE HAWA ME AAKE ISKO SHARE MAT KARNA . ")
       Black.send_message("me", f"**Black XIDSpam Session :**\n\n`{Black.session.save()}`\n\n__Don't Share it With Anyone.__")
       
except Exception as e:
    print(f"{e}") 
