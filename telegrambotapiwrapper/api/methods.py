from __future__ import annotations

from dataclasses import dataclass
from typing import Union, Optional, List

from telegrambotapiwrapper.api.base import Base
from telegrambotapiwrapper.api.types import (PassportElementErrorDataField,
                                             PassportElementErrorFrontSide,
                                             PassportElementErrorReverseSide,
                                             PassportElementErrorSelfie,
                                             PassportElementErrorFile,
                                             PassportElementErrorFiles,
                                             PassportElementErrorTranslationFile,
                                             PassportElementErrorUnspecified,
                                             PassportElementErrorTranslationFiles,
                                             InputMediaAnimation,
                                             InputMediaDocument,
                                             InputMediaAudio,
                                             InputMediaPhoto,
                                             InputMediaVideo,
                                             InlineQueryResultCachedAudio,
                                             InlineQueryResultCachedDocument,
                                             InlineQueryResultCachedGif,
                                             InlineQueryResultCachedMpeg4Gif,
                                             InlineQueryResultCachedPhoto,
                                             InlineQueryResultCachedSticker,
                                             InlineQueryResultCachedVideo,
                                             InlineQueryResultCachedVoice,
                                             InlineQueryResultArticle,
                                             InlineQueryResultAudio,
                                             InlineQueryResultContact,
                                             InlineQueryResultGame,
                                             InlineQueryResultDocument,
                                             InlineQueryResultGif,
                                             InlineQueryResultMpeg4Gif,
                                             InlineQueryResultPhoto,
                                             InlineQueryResultVenue,
                                             InlineQueryResultVideo,
                                             InlineQueryResultVoice,
                                             InlineKeyboardMarkup,
                                             ReplyKeyboardMarkup,
                                             ReplyKeyboardRemove,
                                             ForceReply,
                                             InlineQueryResultLocation,
                                             InputFile,
                                             MaskPosition,
                                             LabeledPrice)

PassportElementError = Union[
    PassportElementErrorDataField,
    PassportElementErrorFrontSide,
    PassportElementErrorReverseSide,
    PassportElementErrorSelfie,
    PassportElementErrorFile,
    PassportElementErrorFiles,
    PassportElementErrorTranslationFile,
    PassportElementErrorTranslationFiles,
    PassportElementErrorUnspecified
]

InputMedia = Union[
    InputMediaAnimation,
    InputMediaDocument,
    InputMediaAudio,
    InputMediaPhoto,
    InputMediaVideo
]

InlineQueryResult = Union[
    InlineQueryResultCachedAudio,
    InlineQueryResultCachedDocument,
    InlineQueryResultCachedGif,
    InlineQueryResultCachedMpeg4Gif,
    InlineQueryResultCachedPhoto,
    InlineQueryResultCachedSticker,
    InlineQueryResultCachedVideo,
    InlineQueryResultCachedVoice,
    InlineQueryResultArticle,
    InlineQueryResultAudio,
    InlineQueryResultContact,
    InlineQueryResultGame,
    InlineQueryResultDocument,
    InlineQueryResultGif,
    InlineQueryResultLocation,
    InlineQueryResultMpeg4Gif,
    InlineQueryResultPhoto,
    InlineQueryResultVenue,
    InlineQueryResultVideo,
    InlineQueryResultVoice,
]
@dataclass
class GetMe(Base):
    """A simple method for testing your bot's auth token. Requires no
       parameters. Returns basic information about the     bot in form of a
       User object."""



@dataclass
class SendMessage(Base):
    """Use this method to send text messages. On success, the sent Message
       is returned."""

    chat_id: Union[int, str]
    text: str
    parse_mode: Optional[str] = None
    disable_web_page_preview: Optional[bool] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class ForwardMessage(Base):
    """Use this method to forward messages of any kind. On success, the sent
       Message is returned."""

    chat_id: Union[int, str]
    from_chat_id: Union[int, str]
    message_id: int
    disable_notification: Optional[bool] = None


@dataclass
class SendPhoto(Base):
    """Use this method to send photos. On success, the sent Message is
       returned."""

    chat_id: Union[int, str]
    photo: Union[InputFile, str]
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class SendAudio(Base):
    """Use this method to send audio files, if you want Telegram clients to
       display them in the music player. Your audio     must be in the .mp3
       format. On success, the sent Message is returned. Bots can currently
       send     audio files of up to 50 MB in size, this limit may be changed
       in the future."""

    chat_id: Union[int, str]
    audio: Union[InputFile, str]
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    duration: Optional[int] = None
    performer: Optional[str] = None
    title: Optional[str] = None
    thumb: Optional[Union[InputFile, str]] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class SendDocument(Base):
    """Use this method to send general files. On success, the sent Message
       is returned. Bots can     currently send files of any type of up to 50
       MB in size, this limit may be changed in the future."""

    chat_id: Union[int, str]
    document: Union[InputFile, str]
    thumb: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class SendVideo(Base):
    """Use this method to send video files, Telegram clients support mp4
       videos (other formats may be sent as Document). On success, the sent
       Message is returned. Bots can     currently send video files of up to 50
       MB in size, this limit may be changed in the future."""

    chat_id: Union[int, str]
    video: Union[InputFile, str]
    duration: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    thumb: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    supports_streaming: Optional[bool] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class SendAnimation(Base):
    """Use this method to send animation files (GIF or H.264/MPEG-4 AVC
       video without sound). On success, the sent Message is returned. Bots can
       currently send animation files of up to 50 MB in size, this     limit
       may be changed in the future."""

    chat_id: Union[int, str]
    animation: Union[InputFile, str]
    duration: Optional[int] = None
    width: Optional[int] = None
    height: Optional[int] = None
    thumb: Optional[Union[InputFile, str]] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class SendVoice(Base):
    """Use this method to send audio files, if you want Telegram clients to
       display the file as a playable voice message.     For this to work, your
       audio must be in an .ogg file encoded with OPUS (other formats may be
       sent as Audio or Document). On success, the sent Message     is
       returned. Bots can currently send voice messages of up to 50 MB in size,
       this limit may be changed in the future."""

    chat_id: Union[int, str]
    voice: Union[InputFile, str]
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    duration: Optional[int] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class SendVideoNote(Base):
    """As of v.4.0, Telegram clients support rounded     square mp4 videos
       As of v.4.0, Telegram clients support rounded     square mp4 videos of
       up to 1 minute long. Use this method to send video messages. On success,
       the sent Message is returned."""

    chat_id: Union[int, str]
    video_note: Union[InputFile, str]
    duration: Optional[int] = None
    length: Optional[int] = None
    thumb: Optional[Union[InputFile, str]] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class SendMediaGroup(Base):
    """Use this method to send a group of photos or videos as an album. On
       success, an array of the sent Messages     is returned."""

    chat_id: Union[int, str]
    media: List[Union[InputMediaPhoto, InputMediaVideo]]
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None


@dataclass
class SendLocation(Base):
    """Use this method to send point on the map. On success, the sent
       Message is returned."""

    chat_id: Union[int, str]
    latitude: float
    longitude: float
    live_period: Optional[int] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class EditMessageLiveLocation(Base):
    """Use this method to edit live location messages sent by the bot or via
       the bot (for inline     bots). A location can be edited until its
       live_period expires or editing is explicitly disabled by a     call to
       stopMessageLiveLocation. On success, if the edited message was sent
       by the bot, the edited Message is returned, otherwise True is returned."""

    latitude: float
    longitude: float
    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass
class StopMessageLiveLocation(Base):
    """Use this method to stop updating a live location message sent by the
       bot or via the bot (for inline     bots) before live_period expires. On
       success, if the message was sent by the bot, the sent Message is
       returned, otherwise True is returned."""

    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass
class SendVenue(Base):
    """Use this method to send information about a venue. On success, the
       sent Message is returned."""

    chat_id: Union[int, str]
    latitude: float
    longitude: float
    title: str
    address: str
    foursquare_id: Optional[str] = None
    foursquare_type: Optional[str] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class SendContact(Base):
    """Use this method to send phone contacts. On success, the sent Message
       is returned."""

    chat_id: Union[int, str]
    phone_number: str
    first_name: str
    last_name: Optional[str] = None
    vcard: Optional[str] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class SendPoll(Base):
    """Use this method to send a native poll. A native poll can't be sent to
       a private chat. On success, the sent Message is returned."""

    chat_id: Union[int, str]
    question: str
    options: List[str]
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class SendChatAction(Base):
    """Use this method when you need to tell the user that something is
       happening on the bot's side. The status is set     for 5 seconds or less
       (when a message arrives from your bot, Telegram clients clear its typing
       status). Returns True     on success."""

    chat_id: Union[int, str]
    action: str


@dataclass
class GetUserProfilePhotos(Base):
    """Use this method to get a list of profile pictures for a user. Returns
       a UserProfilePhotos     object."""

    user_id: int
    offset: Optional[int] = None
    limit: Optional[int] = None


@dataclass
class GetFile(Base):
    """Use this method to get basic info about a file and prepare it for
       downloading. For the moment, bots can download     files of up to 20MB
       in size. On success, a File object is returned. The file can then be
       downloaded via the link
       https://api.telegram.org/file/bot<token>/<file_path>, where <file_path>
       is taken from the response. It is guaranteed that the link will be valid
       for at least 1 hour. When the link expires,     a new one can be
       requested by calling getFile again."""

    file_id: str


@dataclass
class KickChatMember(Base):
    """Use this method to kick a user from a group, a supergroup or a
       channel. In the case of supergroups and channels, the     user will not
       be able to return to the group on their own using invite links, etc.,
       unless unbanned first. The bot must be an administrator in the chat for
       this to work     and must have the appropriate admin rights. Returns
       True on success."""

    chat_id: Union[int, str]
    user_id: int
    until_date: Optional[int] = None


@dataclass
class UnbanChatMember(Base):
    """Use this method to unban a previously kicked user in a supergroup or
       channel. The user will not     return to the group or channel
       automatically, but will be able to join via link, etc. The bot must be
       an     administrator for this to work. Returns True on success."""

    chat_id: Union[int, str]
    user_id: int


@dataclass
class RestrictChatMember(Base):
    """Use this method to restrict a user in a supergroup. The bot must be
       an administrator in the supergroup for this to     work and must have
       the appropriate admin rights. Pass True for all boolean parameters to
       lift restrictions     from a user. Returns True on success."""

    chat_id: Union[int, str]
    user_id: int
    until_date: Optional[int] = None
    can_send_messages: Optional[bool] = None
    can_send_media_messages: Optional[bool] = None
    can_send_other_messages: Optional[bool] = None
    can_add_web_page_previews: Optional[bool] = None


@dataclass
class PromoteChatMember(Base):
    """Use this method to promote or demote a user in a supergroup or a
       channel. The bot must be an administrator in the     chat for this to
       work and must have the appropriate admin rights. Pass False for all
       boolean parameters to     demote a user. Returns True on success."""

    chat_id: Union[int, str]
    user_id: int
    can_change_info: Optional[bool] = None
    can_post_messages: Optional[bool] = None
    can_edit_messages: Optional[bool] = None
    can_delete_messages: Optional[bool] = None
    can_invite_users: Optional[bool] = None
    can_restrict_members: Optional[bool] = None
    can_pin_messages: Optional[bool] = None
    can_promote_members: Optional[bool] = None


@dataclass
class ExportChatInviteLink(Base):
    """Use this method to generate a new invite link for a chat; any
       previously generated link is revoked. The bot must be     an
       administrator in the chat for this to work and must have the appropriate
       admin rights. Returns the new invite     link as String on success."""

    chat_id: Union[int, str]


@dataclass
class SetChatPhoto(Base):
    """Use this method to set a new profile photo for the chat. Photos can't
       be changed for private chats. The bot must     be an administrator in
       the chat for this to work and must have the appropriate admin rights.
       Returns True     on success."""

    chat_id: Union[int, str]
    photo: InputFile


@dataclass
class DeleteChatPhoto(Base):
    """Use this method to delete a chat photo. Photos can't be changed for
       private chats. The bot must be an     administrator in the chat for this
       to work and must have the appropriate admin rights. Returns True on
       success."""

    chat_id: Union[int, str]


@dataclass
class SetChatTitle(Base):
    """Use this method to change the title of a chat. Titles can't be
       changed for private chats. The bot must be an     administrator in the
       chat for this to work and must have the appropriate admin rights.
       Returns True on     success."""

    chat_id: Union[int, str]
    title: str


@dataclass
class SetChatDescription(Base):
    """Use this method to change the description of a supergroup or a
       channel. The bot must be an administrator in the chat     for this to
       work and must have the appropriate admin rights. Returns True on
       success."""

    chat_id: Union[int, str]
    description: Optional[str] = None


@dataclass
class PinChatMessage(Base):
    """Use this method to pin a message in a group, a supergroup, or a
       channel. The bot must be an administrator in the chat for this to work
       and must have the ‘can_pin_messages’ admin right in the supergroup or
       ‘can_edit_messages’ admin right in the channel. Returns True on success."""

    chat_id: Union[int, str]
    message_id: int
    disable_notification: Optional[bool] = None


@dataclass
class UnpinChatMessage(Base):
    """Use this method to unpin a message in a group, a supergroup, or a
       channel. The bot must be an administrator in the chat for this to work
       and must have the ‘can_pin_messages’ admin right in the supergroup or
       ‘can_edit_messages’ admin right in the channel. Returns True on success."""

    chat_id: Union[int, str]


@dataclass
class LeaveChat(Base):
    """Use this method for your bot to leave a group, supergroup or channel.
       Returns True on success."""

    chat_id: Union[int, str]


@dataclass
class GetChat(Base):
    """Use this method to get up to date information about the chat (current
       name of the user for one-on-one conversations,     current username of a
       user, group or channel, etc.). Returns a Chat object on success."""

    chat_id: Union[int, str]


@dataclass
class GetChatAdministrators(Base):
    """Use this method to get a list of administrators in a chat. On
       success, returns an Array of ChatMember     objects that contains
       information about all chat administrators except other bots. If the chat
       is a group or a     supergroup and no administrators were appointed,
       only the creator will be returned."""

    chat_id: Union[int, str]


@dataclass
class GetChatMembersCount(Base):
    """Use this method to get the number of members in a chat. Returns Int
       on success."""

    chat_id: Union[int, str]


@dataclass
class GetChatMember(Base):
    """Use this method to get information about a member of a chat. Returns
       a ChatMember object on     success."""

    chat_id: Union[int, str]
    user_id: int


@dataclass
class SetChatStickerSet(Base):
    """Use this method to set a new group sticker set for a supergroup. The
       bot must be an administrator in the chat for     this to work and must
       have the appropriate admin rights. Use the field can_set_sticker_set
       optionally     returned in getChat requests to check if the bot can use
       this method. Returns True     on success."""

    chat_id: Union[int, str]
    sticker_set_name: str


@dataclass
class DeleteChatStickerSet(Base):
    """Use this method to delete a group sticker set from a supergroup. The
       bot must be an administrator in the chat for     this to work and must
       have the appropriate admin rights. Use the field can_set_sticker_set
       optionally     returned in getChat requests to check if the bot can use
       this method. Returns True     on success."""

    chat_id: Union[int, str]


@dataclass
class AnswerCallbackQuery(Base):
    """Use this method to send answers to callback queries sent from inline
       keyboards. The answer will be displayed to the     user as a
       notification at the top of the chat screen or as an alert. On success,
       True is returned."""

    callback_query_id: str
    text: Optional[str] = None
    show_alert: Optional[bool] = None
    url: Optional[str] = None
    cache_time: Optional[int] = None



@dataclass
class SendGame(Base):
    """Use this method to send a game. On success, the sent Message is
       returned."""

    chat_id: int
    game_short_name: str
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass
class SetGameScore(Base):
    """Use this method to set the score of the specified user in a game. On
       success, if the message was sent by the bot,     returns the edited
       Message, otherwise returns True. Returns an error, if the new     score
       is not greater than the user's current score in the chat and force is
       False."""

    user_id: int
    score: int
    force: Optional[bool] = None
    disable_edit_message: Optional[bool] = None
    chat_id: Optional[int] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None


@dataclass
class GetGameHighScores(Base):
    """Use this method to get data for high score tables. Will return the
       score of the specified user and several of his     neighbors in a game.
       On success, returns an Array of GameHighScore objects."""

    user_id: int
    chat_id: Optional[int] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None



@dataclass
class GetUpdates(Base):
    """Use this method to receive incoming updates using long polling
       (wiki). An Array of Update objects is returned."""

    offset: Optional[int] = None
    limit: Optional[int] = None
    timeout: Optional[int] = None
    allowed_updates: Optional[List[str]] = None


@dataclass
class SetWebhook(Base):
    """Use this method to specify a url and receive incoming updates via an
       outgoing webhook. Whenever there is an update     for the bot, we will
       send an HTTPS POST request to the specified url, containing a JSON-
       serialized Update. In case of an unsuccessful request, we will give up
       after a reasonable amount of     attempts. Returns True on success."""

    url: str
    certificate: Optional[InputFile] = None
    max_connections: Optional[int] = None
    allowed_updates: Optional[List[str]] = None


@dataclass
class DeleteWebhook(Base):
    """Use this method to remove webhook integration if you decide to switch
       back to getUpdates.     Returns True on success."""



@dataclass
class GetWebhookInfo(Base):
    """Use this method to get current webhook status. Requires no
       parameters. On success, returns a WebhookInfo     object. If the bot is
       using getUpdates, will return an object with the url field     empty."""




@dataclass
class AnswerInlineQuery(Base):
    """Use this method to send answers to an inline query. On success, True
       is returned.No more than     50 results per query are allowed."""

    inline_query_id: str
    results: List[InlineQueryResult]
    cache_time: Optional[int] = None
    is_personal: Optional[bool] = None
    next_offset: Optional[str] = None
    switch_pm_text: Optional[str] = None
    switch_pm_parameter: Optional[str] = None


@dataclass
class AnswerInlineQuery(Base):
    """Use this method to send answers to an inline query. On success, True
       is returned.No more than     50 results per query are allowed."""

    inline_query_id: str
    results: List[InlineQueryResult]
    cache_time: Optional[int] = None
    is_personal: Optional[bool] = None
    next_offset: Optional[str] = None
    switch_pm_text: Optional[str] = None
    switch_pm_parameter: Optional[str] = None



@dataclass
class SetPassportDataErrors(Base):
    """Informs a user that some of the Telegram Passport elements they
       provided contains errors. The user will not be able     to re-submit
       their Passport to you until the errors are fixed (the contents of the
       field for which you returned the     error must change). Returns True on
       success."""

    user_id: int
    errors: List[PassportElementError]



@dataclass
class SendInvoice(Base):
    """Use this method to send invoices. On success, the sent Message is
       returned."""

    chat_id: int
    title: str
    description: str
    payload: str
    provider_token: str
    start_parameter: str
    currency: str
    prices: List[LabeledPrice]
    provider_data: Optional[str] = None
    photo_url: Optional[str] = None
    photo_size: Optional[int] = None
    photo_width: Optional[int] = None
    photo_height: Optional[int] = None
    need_name: Optional[bool] = None
    need_phone_number: Optional[bool] = None
    need_email: Optional[bool] = None
    need_shipping_address: Optional[bool] = None
    send_phone_number_to_provider: Optional[bool] = None
    send_email_to_provider: Optional[bool] = None
    is_flexible: Optional[bool] = None
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass
class AnswerShippingQuery(Base):
    """If you sent an invoice requesting a shipping address and the
       parameter is_flexible was specified, the Bot     API will send an Update
       with a shipping_query field to the bot. Use this method to     reply to
       shipping queries. On success, True is returned."""

    shipping_query_id: str
    ok: bool
    shipping_options: Optional[List[LabeledPrice]] = None
    error_message: Optional[str] = None


@dataclass
class AnswerPreCheckoutQuery(Base):
    """Once the user has confirmed their payment and shipping details, the
       Bot API sends the final confirmation in the form     of an Update with
       the field pre_checkout_query. Use this method to respond to such
       pre-checkout queries. On success, True is returned. Note: The Bot API
       must receive an answer within     10 seconds after the pre-checkout
       query was sent."""

    pre_checkout_query_id: str
    ok: bool
    error_message: Optional[str] = None



@dataclass
class SendSticker(Base):
    """Use this method to send .webp stickers. On success, the sent Message
       is returned."""

    chat_id: Union[int, str]
    sticker: Union[InputFile, str]
    disable_notification: Optional[bool] = None
    reply_to_message_id: Optional[int] = None
    reply_markup: Optional[Union[InlineKeyboardMarkup, ReplyKeyboardMarkup, ReplyKeyboardRemove, ForceReply]] = None


@dataclass
class GetStickerSet(Base):
    """Use this method to get a sticker set. On success, a StickerSet object
       is returned."""

    name: str


@dataclass
class UploadStickerFile(Base):
    """Use this method to upload a .png file with a sticker for later use in
       createNewStickerSet and addStickerToSet     methods (can be used
       multiple times). Returns the uploaded File on success."""

    user_id: int
    png_sticker: InputFile


@dataclass
class CreateNewStickerSet(Base):
    """Use this method to create new sticker set owned by a user. The bot
       will be able to edit the created sticker set.     Returns True on
       success."""

    user_id: int
    name: str
    title: str
    png_sticker: Union[InputFile, str]
    emojis: str
    contains_masks: Optional[bool] = None
    mask_position: Optional[MaskPosition] = None


@dataclass
class AddStickerToSet(Base):
    """Use this method to add a new sticker to a set created by the bot.
       Returns True on success."""

    user_id: int
    name: str
    png_sticker: Union[InputFile, str]
    emojis: str
    mask_position: Optional[MaskPosition] = None


@dataclass
class SetStickerPositionInSet(Base):
    """Use this method to move a sticker in a set created by the bot to a
       specific position . Returns True on     success."""

    sticker: str
    position: int


@dataclass
class DeleteStickerFromSet(Base):
    """Use this method to delete a sticker from a set created by the bot.
       Returns True on success."""

    sticker: str



@dataclass
class EditMessageText(Base):
    """Use this method to edit text and game messages sent by the bot or via
       the bot (for inline bots). On success, if edited message is sent by the
       bot, the edited Message is returned, otherwise True is returned."""

    text: str
    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    parse_mode: Optional[str] = None
    disable_web_page_preview: Optional[bool] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass
class EditMessageCaption(Base):
    """Use this method to edit captions of messages sent by the bot or via
       the bot (for inline     bots). On success, if edited message is sent by
       the bot, the edited Message is returned,     otherwise True is returned."""

    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    caption: Optional[str] = None
    parse_mode: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass
class EditMessageMedia(Base):
    """Use this method to edit animation, audio, document, photo, or video
       messages. If a message is a part of a message     album, then it can be
       edited only to a photo or a video. Otherwise, message type can be
       changed arbitrarily. When     inline message is edited, new file can't
       be uploaded. Use previously uploaded file via its file_id or specify a
       URL. On success, if the edited message was sent by the bot, the edited
       Message is returned,     otherwise True is returned."""

    media: InputMedia
    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass
class EditMessageReplyMarkup(Base):
    """Use this method to edit only the reply markup of messages sent by the
       bot or via the bot (for inline     bots). On success, if edited message
       is sent by the bot, the edited Message is returned,     otherwise True
       is returned."""

    chat_id: Optional[Union[int, str]] = None
    message_id: Optional[int] = None
    inline_message_id: Optional[str] = None
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass
class StopPoll(Base):
    """Use this method to stop a poll which was sent by the bot. On success,
       the stopped Poll with the final results is returned."""

    chat_id: Union[int, str]
    message_id: int
    reply_markup: Optional[InlineKeyboardMarkup] = None


@dataclass
class DeleteMessage(Base):
    """Use this method to delete a message, including service messages, with
       the following limitations:- A message can     only be deleted if it was
       sent less than 48 hours ago.- Bots can delete outgoing messages in
       private chats,     groups, and supergroups.- Bots granted
       can_post_messages permissions can delete outgoing messages in
       channels.- If the bot is an administrator of a group, it can delete any
       message there.- If the bot has can_delete_messages     permission in a
       supergroup or a channel, it can delete any message there.Returns True on
       success."""

    chat_id: Union[int, str]
    message_id: int


