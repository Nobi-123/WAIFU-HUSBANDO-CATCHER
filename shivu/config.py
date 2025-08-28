class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "7694170809"
    sudo_users = "7694170809"
    GROUP_ID = "-1002681848382"
    TOKEN = "8384664511:AAE4mHfbqg-cwJ_QAF9T6wXSrtxSMUafj3g"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "cardioXlog"
    UPDATE_CHAT = "botXjarvis"
    BOT_USERNAME = "ExChatzBot"
    CHARA_CHANNEL_ID = "-1002754048423"
    api_id = "26626068"
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
