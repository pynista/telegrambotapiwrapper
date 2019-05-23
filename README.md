# IN DEVELOPING

## telegrambotapiwrapper
Python Telegram Bot API wrapper

## Why telegrambotapiwrapper?

`telegramapiwrapper` is the simplest Telegram Bot Api wrapper for Python among existing wrappers.

## Requirements
Python 3.7

## Installation
_stub_

## Writing first bot
```python
# firstbot.py
from telegrambotapiwrapper.wrapper import Api
from telegrambotapiwrapper.api.types import User

TOKEN = "<past_your_bot_api_token>"

bot_api = Api(token=TOKEN)
me = bot_api.get_me()
print("me: {}".format(me))
print("isinstance(me, User): {}".format(isinstance(me, User)))  # see type of result
```
Result:
```
(venv) dzmitry@mycomp:~$ python3 firstbot.py 
me: User(id=432916128, is_bot=True, first_name='myrudatingposterbot', last_name=None, username='myrudatingposterbot', language_code=None)
isinstance(me, User): True
(venv) dzmitry@mycomp:~$
```
## Examples
###Sending message
###Sending file

## Using proxies

## License
MIT License
Copyright (c) 2019 Dzmitry Maliuzhenets

See LICENSE for details.

