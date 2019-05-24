
## telegrambotapiwrapper
Python Telegram Bot API wrapper

## Why telegrambotapiwrapper?

`telegramapiwrapper` is the simplest Telegram Bot Api wrapper for Python among existing wrappers.

## Requirements
Python 3.7

## Installation
```
pip install telegrambotapiwrapper
```

## Getting started.

## Getting token

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
me: User(id=123456789, is_bot=True, first_name='myrfffrbot', last_name=None, username='myrfffrbot', language_code=None)
isinstance(me, User): True
(venv) dzmitry@mycomp:~$
```
## Examples
### Setting webhook
### Sending message
### Sending file

## Using proxies

## License
MIT License
Copyright (c) 2019 Dzmitry Maliuzhenets

See LICENSE for details.

