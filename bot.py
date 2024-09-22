# (©)Codexbotz

from aiohttp import web
from plugins import web_server

from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime, timedelta
import os
from apscheduler.schedulers.background import BackgroundScheduler

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, \
    FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2, FORCE_SUB_CHANNEL_3, FORCE_SUB_CHANNEL_4, \
    FORCE_SUB_CHANNEL_5, FORCE_SUB_CHANNEL_6, CHANNEL_ID, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

        # Initialize Background Scheduler
        self.scheduler = BackgroundScheduler()
        self.scheduler.start()

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        # Set up Force Subscribe Channels
        for i in range(1, 7):  # Loop through channels 1 to 6
            channel_var = f'FORCE_SUB_CHANNEL_{i}'
            channel_value = globals().get(channel_var)  # Use globals().get to avoid KeyError if channel doesn't exist
            if channel_value:
                try:
                    link = (await self.get_chat(channel_value)).invite_link
                    if not link:
                        await self.export_chat_invite_link(channel_value)
                        link = (await self.get_chat(channel_value)).invite_link
                    setattr(self, f"invitelink{i}", link)  # Dynamically set invitelink1, invitelink2, etc.
                except Exception as a:
                    self.LOGGER(__name__).warning(a)
                    self.LOGGER(__name__).warning(f"Bot can't Export Invite link from Force Sub Channel {i}!")
                    self.LOGGER(__name__).warning(f"Please double check the {channel_var} value and make sure the Bot is Admin in the channel with Invite Users via Link Permission, Current Value: {channel_value}")
                    sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make sure the bot is Admin in DB Channel, and double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/+r-6ztnSy3yo3Mzc9 for support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/POCKET_PFM")
        self.LOGGER(__name__).info(f"""
  ___ ___  ___  ___ ___ _    _____  _____  ___ _____ ___ 
 / __/ _ \|   \| __| __| |  |_ _\ \/ / _ )/ _ \_   _/ __|
| (_| (_) | |) | _|| _|| |__ | | >  <| _ \ (_) || | \__ \\
 \___\___/|___/|___|_| |____|___/_/\_\___/\___/ |_| |___/
                                                         """)

        self.username = usr_bot_me.username
        
        # Start the web server
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    # Define the delete_file function to remove files and update the database
    async def delete_file(self, file_path, db_reference):
        if os.path.exists(file_path):
            os.remove(file_path)
            self.LOGGER(__name__).info(f"Deleted file: {file_path}")
            # Logic to remove the reference from the database
            # Example: await self.remove_from_db(db_reference)
        else:
            self.LOGGER(__name__).info(f"File {file_path} does not exist.")

    # Example: Send a file to a user and schedule deletion
    async def send_file_to_user(self, chat_id, file_path, db_reference):
        await self.send_document(chat_id, open(file_path, 'rb'))

        # Schedule the deletion of the file after 1 hour
        run_date = datetime.now() + timedelta(hours=1)
        self.scheduler.add_job(self.delete_file, 'date', run_date=run_date, args=[file_path, db_reference])

    async def stop(self, *args):
        # Shut down the scheduler
        self.scheduler.shutdown(wait=False)

        # Stop the bot
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
