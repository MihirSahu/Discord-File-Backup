# Discord File Backup

My attempt to use Discord Nitro's 500MB file upload as a form of storage. This uses your Discord account instead of a bot account - known as a userbot - and is against Discord's TOS. I am not responsible for your actions.

## Steps
1. Authenticate as user
2. Compress and encrypt file/folder with 256-bit AES using the given password
3. Upload file to designated channel

## ENV structure
```
TOKEN=USER_TOKEN
FILE_PATH=BACKUP_FILE_OR_FOLDER_PATH
PASSWORD=AES_ENCRYPTION_PASSWORD
CHANNEL_ID=BACKUP_CHANNEL_ID
```

## Resources
- [Discord.py-self](https://github.com/dolfies/discord.py-self)
- [PyZipper](https://github.com/danifus/pyzipper)
- [Python Zipfile](https://docs.python.org/3/library/zipfile.html)