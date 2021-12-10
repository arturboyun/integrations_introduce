from abc import ABC, abstractmethod
from typing import Union

from contrib import Alert, Telegram


class NotifyBase(ABC):
    """Base class for notify integrations"""

    @abstractmethod
    def send_message(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def send_alert(self, alert: Alert):
        raise NotImplementedError


class SlackIntegration(NotifyBase):

    def __init__(self, webhook_url: str):
        if not webhook_url:
            raise ValueError('webhook_url is required')
        self.webhook_url = webhook_url

    def send_message(self, text: str):
        print(f"Slack send_message: {text}")

    def send_alert(self, alert: Alert):
        print(f"Slack send_message: webhook_url={self.webhook_url} message={alert.message}, fields={alert.fields}")


class MSTeamsIntegration(NotifyBase):

    def __init__(self, webhook_url: str):
        if not webhook_url:
            raise ValueError('webhook_url is required')
        self.webhook_url = webhook_url

    def send_message(self, text: str):
        print(f"Teams send_message: {text}")

    def send_alert(self, alert: Alert):
        print(f"Teams send_message: webhook_url={self.webhook_url} message={alert.message}, fields={alert.fields}")


class TelegramIntegration(NotifyBase):

    def __init__(self, chat_id: Union[str, int]):
        if not chat_id:
            raise ValueError('chat_id is required')
        self.chat_id = chat_id

    def send_message(self, text: str):
        Telegram.send_message(self.chat_id, text)

    def send_alert(self, alert: Alert):
        Telegram.send_message(self.chat_id, f"message={alert.message}, fields={alert.fields}")
