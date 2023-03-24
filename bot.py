import discord
import pyzipper
import os
from dotenv import load_dotenv
import datetime

load_dotenv()

TOKEN = os.getenv("TOKEN")
FILE_PATH = os.getenv("FILE_PATH")
PASSWORD = os.getenv("PASSWORD")
BACKUP_CHANNEL_ID= os.getenv("CHANNEL_ID")

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)
        # print(FILE_PATH, PASSWORD)

        channel = client.get_channel(int(BACKUP_CHANNEL_ID))
        
        await compressAndEncrypt(FILE_PATH, PASSWORD)
        await channel.send('Compressing and encrypting files...')
        await channel.send(file=discord.File((fr'{datetime.datetime.now().strftime("%Y-%m-%d")}.zip')))

async def compressAndEncrypt(path, password):
    secret_password = bytes(password, 'utf-8')

    with pyzipper.AESZipFile(f'{datetime.datetime.now().strftime("%Y-%m-%d")}.zip', 'w', compression=pyzipper.ZIP_LZMA, encryption=pyzipper.WZ_AES) as zf:
        zf.setpassword(secret_password)

        if os.path.isdir(FILE_PATH):
            for root, dirs, files in os.walk(path):
                for file in files:
                    zf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), os.path.join(path, '..')))
        else:
            zf.write(FILE_PATH)

    '''
    with pyzipper.AESZipFile('new_test.zip') as zf:
        zf.setpassword(secret_password)
        my_secrets = zf.read('test.txt')
    '''

client = MyClient()
client.run(TOKEN)