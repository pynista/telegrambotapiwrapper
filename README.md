# What is telegrambotapiwrapper?
`telegramapiwrapper` is the simplest Telegram Bot Api wrapper for Python among existing wrappers.
# Requirements
Python 3.7
# Installation
```
pip install telegrambotapiwrapper
```

# Getting started.
### Creating a bot

You must [create a bot and get a token](https://core.telegram.org/bots#6-botfather)

### Testing your bot's auth token
We use the method [getMe](https://core.telegram.org/bots/api#getme):
```python
>>> from telegrambotapiwrapper.wrapper import Api
>>> first_bot_api = Api(token="<paste your token here>")
>>> me = first_bot_api.get_me()
>>> me
User(id=123456679, is_bot=True, first_name='botbotbot', last_name=None, username='myrudatingposterbot', language_code=None)
```
Check result type:
```python
>>> from telegrambotapiwrapper.typelib import User
>>> isinstance(me, User)
True
```
### Sending a text message to channel
#### Preconditions
Before sending a text message to a channel, you must:
1. [create channel](https://www.wikihow.com/Create-a-Telegram-Channel-on-Android)
1. [add bot to channel as administrator](https://stackoverflow.com/questions/33126743/how-do-i-add-my-bot-to-a-channel)
1. [get channel id](https://stackoverflow.com/questions/32423837/telegram-bot-how-to-get-a-group-chat-id)
### Sending to the channel

### Sending a photo to channel

## License
MIT License
Copyright (c) 2019 Dzmitry Maliuzhenets

See LICENSE for details.

