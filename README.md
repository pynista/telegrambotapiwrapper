# What is telegrambotapiwrapper?

`telegrambotapiwrapper` is Telegram Bot Api implementation for Python
# Requirements
Python 3.7 or Python 3.8
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
>>> from telegrambotapiwrapper import Api
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
#### Sending to the channel
```python
>>> first_bot_api.send_message(chat_id=-12345678912345, text="sdjfhjsdfbjdbvhj")
Message(message_id=299, date=1558966491, chat=Chat(id=--12345678912345, type='channel', title='FooFoo', username='lalalalalalala', first_name=None, last_name=None, all_members_are_administrators=None, photo=None, description=None, invite_link=None, pinned_message=None, sticker_set_name=None, can_set_sticker_set=None), from_=None, forward_from=None, forward_from_chat=None, forward_from_message_id=None, forward_signature=None, forward_sender_name=None, forward_date=None, reply_to_message=None, edit_date=None, media_group_id=None, author_signature=None, text='sdjfhjsdfbjdbvhj', entities=None, caption_entities=None, audio=None, document=None, animation=None, game=None, photo=None, sticker=None, video=None, voice=None, video_note=None, caption=None, contact=None, location=None, venue=None, poll=None, new_chat_members=None, left_chat_member=None, new_chat_title=None, new_chat_photo=None, delete_chat_photo=None, group_chat_created=None, supergroup_chat_created=None, channel_chat_created=None, migrate_to_chat_id=None, migrate_from_chat_id=None, pinned_message=None, invoice=None, successful_payment=None, connected_website=None, passport_data=None)
```
>  Note that chat_id is negative.
### Sending a photo to channel
```python
>>> with open('/home/dzmitry/Pictures/500800998.jpg', 'rb') as image:
...    first_bot_api.send_photo(chat_id=-12345678912345, photo=image,
...                             caption="hello world")

>>>

```
>  Note the open file mode.
## Method and types
* Implemented all methods Telegram Bot Api
* Implemented all types Telegram Bot Api
* All types of Telegram Bot Api are imported from the `typelib` module.
## License
MIT License
Copyright (c) 2019 Dzmitry Maliuzhenets

See LICENSE for details.

