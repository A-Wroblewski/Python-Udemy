from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, message: str) -> None:
        self.message = message

    @abstractmethod
    def send(self) -> bool: ...


class EmailNotification(Notification):
    def send(self) -> bool:
        print('email notif:', self.message)
        return True


class GameNotification(Notification):
    def send(self) -> bool:
        print('game notif:', self.message)
        return False


def notify(notification: Notification):
    notification_sent = notification.send()

    if notification_sent:
        print('enviou')
    else:
        print('não enviou')

email_notification = EmailNotification('oi')
notify(email_notification)

game_notification = GameNotification('banana')
notify(game_notification)
