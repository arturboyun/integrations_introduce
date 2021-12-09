from abc import ABC, abstractmethod

from contrib import Alert


class NotifyBase(ABC):
    """Base class for notify integrations"""

    @abstractmethod
    def send_message(self, text: str):
        raise NotImplementedError

    @abstractmethod
    def send_alert(self, alert: Alert):
        raise NotImplementedError


class SlackIntegration(NotifyBase):
    def send_message(self, text: str):
        print(f"Slack send_message: {text}")

    def send_alert(self, alert: Alert):
        print(f"Slack send_message: message={alert.message}, fields={alert.fields}")


class MSTeamsIntegration(NotifyBase):
    def send_message(self, text: str):
        print(f"Teams send_message: {text}")

    def send_alert(self, alert: Alert):
        print(f"Teams send_message: message={alert.message}, fields={alert.fields}")
