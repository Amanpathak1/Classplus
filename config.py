import os

API_ID = API_ID = 21063898

API_HASH = os.environ.get("API_HASH", "7f8faf197d0459c45c07e8f5b00faeb3")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7111400415:AAGPEM099MBl1_fyXEaex82bHCC7ilyYtYE")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 7009461779))

LOG = -1001833358236

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "7009461779").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


