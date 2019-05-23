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

TOKEN = "<past_your_bot_api_token>"

bot_api = Api(token=TOKEN)
me = bot_api.get_me()
print("me: {}".format(me))
print("type of `me`: {}".format(type(me))) # see type of result
```
Result:
```
(venv) dzmitry@mycomp:~$ python3 firstbot.py 
me: User(id=432916128, is_bot=True, first_name='myrudatingposterbot', last_name=None, username='myrudatingposterbot', language_code=None)
type of `me`:<class 'telegrambotapiwrapper.api.types.User'>
(venv) dzmitry@mycomp:~$
```
## Documentation
_stub_

## License
MIT License
Copyright (c) 2019 Dzmitry Maliuzhenets

See LICENSE for details.

