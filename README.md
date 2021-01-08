# Table of contents
[What is telegrambotapiwrapper?](https://github.com/pynista/telegrambotapiwrapper#whatis)  
[Why telegrambotapiwrapper?](https://github.com/pynista/telegrambotapiwrapper#why)  
[Requirements](https://github.com/pynista/telegrambotapiwrapper#requirements)  
[Installation](https://github.com/pynista/telegrambotapiwrapper#installation)  
[Usage](https://github.com/pynista/telegrambotapiwrapper#usage)
- [General remarks](https://github.com/pynista/telegrambotapiwrapper#remarks)  
- [Types](https://github.com/pynista/telegrambotapiwrapper#types)
- [Methods](https://github.com/pynista/telegrambotapiwrapper#methods)
- [Making requests](https://github.com/pynista/telegrambotapiwrapper#requests)
- [Responses](https://github.com/pynista/telegrambotapiwrapper#responses)  

[Examples](https://github.com/pynista/telegrambotapiwrapper#examples)  
[FAQ](https://github.com/pynista/telegrambotapiwrapper#FAQ)  
[License](https://github.com/pynista/telegrambotapiwrapper#license)  
[Contributing](https://github.com/pynista/telegrambotapiwrapper#contributing)  
[Contacts](https://github.com/pynista/telegrambotapiwrapper#contacts)  


# What is telegrambotapiwrapper?<a name="whatis"></a>

`telegrambotapiwrapper` is Telegram Bot Api implementation for Python

# Why telegrambotapiwrapper?<a name="why"></a>

`telegrambotapiwrapper`is stable reliable implementation of Telegram Bot Api

# Requirements<a name="whatis"></a>

## Python implementations

CPython

## Python versions

3.7, 3.8, 3.9

# Installation<a name="whatis"></a>
```
pip install telegrambotapiwrapper
```
# Usage<a name="usage"></a>
## General remarks<a name="remarks"></a>
* Implemented all methods Telegram Bot Api
* Implemented all types Telegram Bot Api

## Types<a name="types"></a>
All types of Telegram Bot Api are imported from the `typelib` module.

For example:
```python

>>> from telegrambotapiwrapper.typelib import User
>>> user = User(id=123456789, is_bot=False, first_name="UserFirstName")
```

Types are all completely in line with the Telegram API's definition of the types, except for the Message's from field, which is renamed to from_ (because from is a Python reserved token)

For example:
```python
>>> from telegrambotapiwrapper.typelib import User, Message, Chat
>>> user = User(id=123456789, is_bot=False, first_name="UserFirstName")
>>> message = Message(
...    message_id=1234567891011,
...    date=987654321987,
...    chat=Chat(id=36725367325, type='group'),
...    from_=user # !
...)
```

## Methods<a name="methods"></a>

All Telegram Bot Api methods can be accessed through an instance of the `Api` class

Methods are renamed to follow common Python naming conventions. E.g. getMe is renamed to get_me and sendMessage to send_message.

For example:
```python
>>> from telegrambotapiwrapper import Api
>>> bot_api = Api(token="<paste your token here>")
>>> bot_api.send_message(chat_id=-321532153215, text="Hello world")
```

## Making requests<a name="requests"></a>
## Responses<a name="responses"></a>
# Examples<a name="examples"></a>
### 1. Getting information about bot
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
# FAQ<a name="FAQ"></a>
# License<a name="license"></a>
MIT License
Copyright (c) 2020 Dzmitry Maliuzhenets

See LICENSE for details.
# Contributing<a name="contributing"></a>
Feel free to contribute

# Contacts<a name="contacts"></a>
maliuzhenetsdzmitry @ gmail dot com