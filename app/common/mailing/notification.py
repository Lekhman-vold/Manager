import base64

import mandrill
import argparse
import traceback
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


mandrill_api_key = '82ebc412a56792dcb4c238810aa88736-us5'
mandrill_from_email = 'volodya.l@yahoo.com'


class EmailSystem:
    mandrill_client = mandrill.Mandrill(mandrill_api_key)

    def send_email(self, message: str, receiver: str, subject: str = None, attachments: list = None):
        message = {
            'from_email': mandrill_from_email,
            'html': message,
            'subject': subject,
            'to': [
                {
                    'email': receiver,
                }
            ],
            "attachments": attachments
        }

        if attachments:
            message['attachments'] = attachments

        return self.mandrill_client.messages.send(message)


class NotificationSystem(EmailSystem):
    pass


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--email')
    parser.add_argument('--sms')
    parser.add_argument('--message')
    parser.add_argument('--subject')
    parser.add_argument('--file')
    parser.add_argument('--remove_file')
    args = parser.parse_args()
    errors = ''
    # if not args.message:
    #     with open(args.file, 'r') as f:
    #         args.message = f.read()
    #     if args.remove_file:
    #         os.remove(args.file)

    notification_system = NotificationSystem()
    if args.email:
        print(f'sending email to {args.email}...', end='')
        try:
            result = notification_system.send_email(args.message, args.email, args.subject)
            if result[0]['status'] == 'sent':
                print('SUCCESS')
            else:
                raise Exception(result)
        except Exception as e:
            print('FAIL')
            errors += f'SENDING EMAIL TO {args.email}:\n{traceback.format_exc()}\n\n'

    if errors:
        raise Exception(errors)