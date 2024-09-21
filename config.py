#(©)Codeflix_Bots

import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "6665400364:AAEIjvJlWxiVt_AU3WmmOhq5GZkSEp-mxOQ")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", "12448836"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "7171909f346277ef38ee08334ad08986")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002034209239"))

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "2145086581"))

#Port
PORT = os.environ.get("PORT", "8180")

#Database 
DB_URI = os.environ.get("DATABASE_URL", "mongodb+srv://hariharan011205:DCPmNk8OxjyeI0fe@cluster0.2igcqay.mongodb.net/?retryWrites=true&w=majority")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluser0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL_1 = int(os.environ.get("FORCE_SUB_CHANNEL_1", ""))
FORCE_SUB_CHANNEL_2 = int(os.environ.get("FORCE_SUB_CHANNEL_2", ""))
FORCE_SUB_CHANNEL_3 = int(os.environ.get("FORCE_SUB_CHANNEL_3", ""))
FORCE_SUB_CHANNEL_4 = int(os.environ.get("FORCE_SUB_CHANNEL_4", ""))
FORCE_SUB_CHANNEL_5 = int(os.environ.get("FORCE_SUB_CHANNEL_5", ""))
FORCE_SUB_CHANNEL_6 = int(os.environ.get("FORCE_SUB_CHANNEL_6", ""))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

#Set to `False` to disable auto link creation, or `True` to enable Auto link creation.
ENABLE_LINK_CREATION = True

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>ʜᴇʟʟᴏ {first}\n\n ɪ ᴀᴍ ᴍᴜʟᴛɪ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ , ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ » @POCKET_PFM</b>")
try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1103392937").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "Sorry {first} You Have To join the Below Channels First To Access Our Files..\n\n So Please Join The Below Channels First And Click On “Now Click Here” button....!")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", "<b>» ʙʏ @POCKET_PFM</b>")

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "True") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!\n\n» ᴍʏ ᴏᴡɴᴇʀ : @Audio_Versee"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

# LinkShortner Added
LINKSHORTX_API= os.environ.get("LINKSHORTX_API",'5b2908ac9710e83f0a4186a74c25ca3e728faac6')

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
