# What is telegrambotapiwrapper?

`telegrambotapiwrapper` is Telegram Bot Api implementation for Python

# Why telegrambotapiwrapper?

`telegrambotapiwrapper`is stable reliable implementation of Telegram Bot Api

# Requirements

## Python implementations

CPython

## Python versions

3.7, 3.8, 3.9

# Installation
```
pip install telegrambotapiwrapper
```
# Usage
## Общие замечания
* Implemented all methods Telegram Bot Api
* Implemented all types Telegram Bot Api

## Import
* All types of Telegram Bot Api are imported from the `typelib` module.
## Making requests
## Responses
# Examples
### 1. Получение информации о боте
```python
>>> from telegrambotapiwrapper import Api
>>> first_bot_api = Api(token="<paste your token here>")
>>> me = first_bot_api.get_me()
>>> me
User(id=123456789, is_bot=True, first_name='botbotbot', last_name=None, username='ttesttesstttestbot', language_code=None)
```
Let's check the result type:
```python
>>> from telegrambotapiwrapper.typelib import User
>>> isinstance(me, User)
True
```

### 2. Sending a photo to channel
```python
>>> with open('/home/dzmitry/Pictures/500800998.jpg', 'rb') as image:
...    first_bot_api.send_photo(chat_id=-12345678912345, photo=image,
...                             caption="hello world")

>>>
```
>  Note the open file mode.
### 3. Sending a text message to channel
```python
>>> first_bot_api.send_message(chat_id=-12345678912345, text="sdjfhjsdfbjdbvhj")
Message(message_id=299, date=1558966491, chat=Chat(id=--12345678912345, type='channel', title='FooFoo', username='lalalalalalala', first_name=None, last_name=None, all_members_are_administrators=None, photo=None, description=None, invite_link=None, pinned_message=None, sticker_set_name=None, can_set_sticker_set=None), from_user=None, forward_from=None, forward_from_chat=None, forward_from_message_id=None, forward_signature=None, forward_sender_name=None, forward_date=None, reply_to_message=None, edit_date=None, media_group_id=None, author_signature=None, text='sdjfhjsdfbjdbvhj', entities=None, caption_entities=None, audio=None, document=None, animation=None, game=None, photo=None, sticker=None, video=None, voice=None, video_note=None, caption=None, contact=None, location=None, venue=None, poll=None, new_chat_members=None, left_chat_member=None, new_chat_title=None, new_chat_photo=None, delete_chat_photo=None, group_chat_created=None, supergroup_chat_created=None, channel_chat_created=None, migrate_to_chat_id=None, migrate_from_chat_id=None, pinned_message=None, invoice=None, successful_payment=None, connected_website=None, passport_data=None)
```
>  Note that chat_id is negative.
### 4.
# FAQ
# License
The MIT License (MIT)
# Contributing
MIT License
Copyright (c) 2020 Dzmitry Maliuzhenets

See LICENSE for details.
# Contacts
maliuzhenetsdzmitry @ gmail dot com