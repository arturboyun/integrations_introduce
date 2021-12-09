from typing import Union


class Alert(object):
    """Mock Labyrinth Alert"""
    def __init__(self, message: str, fields: dict = None):
        if fields is None:
            fields = {}

        self.fields = fields
        self.message = message


class Message(object):
    """Mock Telegram Message Entity"""
    def __init__(self, chat_id: Union[str, int], text: str):
        self.chat_id = chat_id
        self.text = text


class Telegram(object):
    """Mock Telegram API Client"""
    @staticmethod
    def send_message(chat_id: Union[str, int], text: str) -> Message:
        message = Message(chat_id, text)
        print(f'Telegram message sent ({message.chat_id=}, {message.text=})')
        return message
