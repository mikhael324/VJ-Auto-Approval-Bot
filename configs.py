# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "20389440"))
    API_HASH = getenv("API_HASH", "a1a06a18eb9153e9dbd447cfd5da2457")
    BOT_TOKEN = getenv("BOT_TOKEN", "5893612267:AAEwtzs0tsR2qd13ae9ZRw-I_Yq8ZXoWow0")
    FSUB = getenv("FSUB", "MvM_Links")
    CHID = int(getenv("CHID", "-1001603478834"))
    SUDO = list(map(int, getenv("SUDO", "1746132193").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://mvmpre:mvmpre@cluster0.vzaeiqm.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @VJ_Botz
# Subscribe YouTube Channel For Amazing Bot @Tech_VJ
# Ask Doubt on telegram @KingVJ01
