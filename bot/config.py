import os


class config:
    BOT_TOKEN = "2124088863:AAHpMNBnJEU0_jAmB8UyKRoY5K_V1l7qlc0"
    APP_ID = "2171111"
    API_HASH = "fd7acd07303760c52dcc0ed8b2f73086"
    DATABASE_URL = os.getenv("DATABASE_URL")
    SUDO_USERS = "1089528685" # Sepearted by space.
    SUPPORT_CHAT_LINK = "t.me/hexbotsdg"
    DOWNLOAD_DIRECTORY = "./downloads/"
    G_DRIVE_CLIENT_ID = "492722340804-56k45gjjoka298godnspdjscgb02avq1.apps.googleusercontent.com"
    G_DRIVE_CLIENT_SECRET = "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"


class BotCommands:
  Download = ['download', 'dl']
  Authorize = ['auth', 'authorize']
  SetFolder = ['setfolder', 'setfl']
  Revoke = ['revoke']
  Clone = ['copy', 'clone']
  Delete = ['delete', 'del']
  EmptyTrash = ['emptyTrash']
  YtDl = ['ytdl']

class Messages:
    START_MSG = "**Hi there {}.**\n**I'm Google Drive Uploader Bot.You can use me to upload any file / video to Google Drive from direct link or Telegram Files.**\n**You can know more from /help.**"

    HELP_MSG = [
        ".",
        "**Google Drive Uploader**\n**I can upload files from direct link or Telegram Files to your Google Drive. All i need is to authenticate me to your Google Drive Account and send a direct download link or Telegram File.**\n\nI have more features... ! Wanna know about it ? Just walkthrough this tutorial and read the messages carefully.",
        
        f"**Authenticating Google Drive**\n**Send the /{BotCommands.Authorize[0]} commmand and you will receive a URL, visit URL and follow the steps and send the received code here. Use /{BotCommands.Revoke[0]} to revoke your currently logged Google Drive Account.**\n\n**Note: I will not listen to any command or message (except /{BotCommands.Authorize[0]} command) until you authorize me.\nSo, Authorization is mandatory !**",
        
        f"**Direct Links**\n**Send me a direct download link for a file and i will download it on my server and Upload it to your Google Drive Account. You can rename files before uploading to GDrive Account. Just send me the URL and new filename separated by ' | '.**\n\n****Examples:****\n```https://example.com/AFileWithDirectDownloadLink.mkv | New FileName.mkv```\n\n**Telegram Files**\n**To Upload telegram files in your Google drive Account just send me the file and i will download and upload it to your Google Drive Account. Note: Telegram Files Downloading are slow. it may take longer for big files.**\n\n**YouTube-DL Support**\n**Download files via youtube-dl.\nUse /{BotCommands.YtDl[0]} (YouTube Link/YouTube-DL Supported site link)**",
        
        f"**Custom Folder for Upload**\n**Want to upload in custom folder or in** **TeamDrive** ** ?\nUse /{BotCommands.SetFolder[0]} (Folder URL) to set custom upload folder.\nAll the files are uploaded in the custom folder you provide.**",
        
        f"**Delete Google Drive Files**\n**Delete google drive files. Use /{BotCommands.Delete[0]} (File/Folder URL) to delete file or reply /{BotCommands.Delete[0]} to bot message.\nYou can also empty trash files use /{BotCommands.EmptyTrash[0]}\nNote: Files are deleted permanently. This process cannot be undone.\n\n**Copy Google Drive Files**\n**Yes, Clone or Copy Google Drive Files.\n**Use /{BotCommands.Clone[0]} (File id / Folder id or URL) to copy Google Drive Files in your Google Drive Account.**",
        
        "**Rules & Precautions**\n**1. Don't copy BIG Google Drive Files/Folders. It may hang the bot and your files maybe damaged.\n2. Send One request at a time unless bot will stop all processes.\n3. Don't send slow links @transload it first.\n4. Don't misuse, overload or abuse this free service.**",
        
        # Dont remove this ↓ if you respect developer.
        #"**Developed by @viperadnan**"
        ]
     
    RATE_LIMIT_EXCEEDED_MESSAGE = "❗ **Rate Limit Exceeded.**\n**User rate limit exceeded try after 24 hours.**"
    
    FILE_NOT_FOUND_MESSAGE = "❗ **File/Folder not found.**\n**File id - {} Not found. Make sure it\'s exists and accessible by the logged account.**"
    
    INVALID_GDRIVE_URL = "❗ **Invalid Google Drive URL**\nMake sure the Google Drive URL is in valid format."
    
    COPIED_SUCCESSFULLY = "✅ **Copied successfully.**\n[{}]({}) **({})**"
    
    NOT_AUTH = f"🔑 **You have not authenticated me to upload to any account.**\n**Send /{BotCommands.Authorize[0]} to authenticate.**"
    
    DOWNLOADED_SUCCESSFULLY = "📤 **Uploading File...**\n**Filename:** ```{}```\n**Size:** ```{}```"
    
    UPLOADED_SUCCESSFULLY = "✅ **Uploaded Successfully.**\n[{}]({}) **({})**"
    
    DOWNLOAD_ERROR = "❗**Downloader Failed**\n{}\n**Link - {}**"
    
    DOWNLOADING = "📥 **Downloading File...\nLink:** ```{}```"
    
    ALREADY_AUTH = "🔒 **Already authorized your Google Drive Account.**\n**Use /revoke to revoke the current account.**\n**Send me a direct link or File to Upload on Google Drive**"
    
    FLOW_IS_NONE = f"❗ **Invalid Code**\n**Run {BotCommands.Authorize[0]} first.**"
    
    AUTH_SUCCESSFULLY = '🔐'
    
    INVALID_AUTH_CODE = '❗ **Invalid Code**\n**The code you have sent is invalid or already used before. Generate new one by the Authorization URL**'
    
    AUTH_TEXT = "⛓️ **To Authorize your Google Drive account visit this [URL]({}) and send the generated code here.**\n**Visit the URL > Allow permissions > you will get a code > copy it > Send it here**"
    
    DOWNLOAD_TG_FILE = "📥 **Downloading File...**\n**Filename:** ```{}```\n**Size:** ```{}```\n**MimeType:** ```{}```"
    
    PARENT_SET_SUCCESS = '🆔✅ **Custom Folder link set successfully.**\n**Your custom folder id - {}\nUse** ```/{} clear``` **to clear it.**'
    
    PARENT_CLEAR_SUCCESS = f'🆔🚮 **Custom Folder ID Cleared Successfuly.**\n**Use** ```/{BotCommands.SetFolder[0]} (Folder Link)``` **to set it back**.'
    
    CURRENT_PARENT = "🆔 **Your Current Custom Folder ID - {}**\n**Use** ```/{} (Folder link)``` **to change it.**"
    
    REVOKED = f"🔓 **Revoked current logged account successfully.**\n**Use /{BotCommands.Authorize[0]} to authenticate again and use this bot.**"
    
    NOT_FOLDER_LINK = "❗ **Invalid folder link.**\n**The link you send its not belong to a folder.**"
    
    CLONING = "🗂️ **Cloning into Google Drive...**\n**G-Drive Link - {}**"
    
    PROVIDE_GDRIVE_URL = "**❗ Provide a valid Google Drive URL along with commmand.**\n**Usage - /{} (GDrive Link)**"
    
    INSUFFICIENT_PERMISSONS = "❗ **You have insufficient permissions for this file.**\n**File id - {}**"
    
    DELETED_SUCCESSFULLY = "🗑️✅ **File Deleted Successfully.**\n**File deleted permanently !\nFile id - {}**"
    
    WENT_WRONG = "⁉️ **ERROR: SOMETHING WENT WRONG**\n**Please try again later.**"
    
    EMPTY_TRASH = "🗑️🚮**Trash Emptied Successfully !**"
    
    PROVIDE_YTDL_LINK = "❗**Provide a valid YouTube-DL supported link.**"