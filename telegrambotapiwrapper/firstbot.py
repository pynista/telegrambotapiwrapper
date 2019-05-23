import sys

sys.path.insert(0, "/home/dzmitry/PycharmProjects/telegrambotapiwrapper/")


from telegrambotapiwrapper.wrapper import Api
from telegrambotapiwrapper.api.types import User

TOKEN = "432916128:AAG-rZvzYDzZCUr2psOlBrYeJa0_is7LR9o"
# TOKEN = "<your_bot_api_token>"

bot_api = Api(token=TOKEN)
me = bot_api.get_me()
print("me: {}".format(me))
print("isinstance(me, User): {}".format(isinstance(me, User)))  # see type of result

