import os

API_ID = API_ID = 22253680

API_HASH = os.environ.get("API_HASH", "4fc4c646519fe43891bebd1449744b7e")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7164381935:AAFLJQcZR6blolTwQkoQirLWtIltMTUDGnE")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6352927253))

LOG = -1001833358236

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "1311808931").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


