# bot developer @mr_jisshu
from os import environ 

class Config:
    
    API_ID = environ.get("API_ID", "28243586")
    API_HASH = environ.get("API_HASH", "4022d5686b9b7a7cf8891205921a0ab3")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7064899225:AAF80y8D2VbmKb8S_k5PgKBq5hjRV5L3Rcs") 
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6929340267 6551906246').split()]
    BOT_SESSION = environ.get("BOT_SESSION", "bot") 

    PICS = (environ.get('PICS', 'https://vault.pictures/p/4add4cab289149138c7f5ea4ec9d4813'))
    
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://madarazbotz:MJlmnDPtC63ihNK5@cluster0.7dxhb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    
    LOG_CHANNEL = int(environ.get('LOG_CHANNEL', '-1002303065410'))
    FORCE_SUB_CHANNEL = environ.get("FORCE_SUB_CHANNEL", "https://t.me/vr_unreal") # FORCE SUB channel link 
    FORCE_SUB_ON = environ.get("FORCE_SUB_ON", "True")  # FORCE SUB ON - OFF


class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
    
