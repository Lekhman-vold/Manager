from notification import NotificationSystem


class Mailing:
    def __init__(self):
        self.notification_system = NotificationSystem()

    def sent_mail(self):
        self.notification_system.send_email('Test main', 'volodya.l@yahoo.com', 'Create User')


if __name__ == '__main__':
    m = Mailing()
    m.sent_mail()
