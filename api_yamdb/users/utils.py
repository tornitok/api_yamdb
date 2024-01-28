from django.conf import settings
from django.core.mail import send_mail


def send_confirmation_email(email, confirmation_code):
    subject = 'Код подтверждения для вашего аккаунта'
    message = (
        f'<html>'
        f'<body>'
        f'<p>Здравствуйте!</p>'
        f'<p>Благодарим вас за регистрацию на нашем портале. Для завершения '
        f'процесса регистрации, пожалуйста, введите следующий '
        f'код подтверждения:</p>'
        f'<p><h3><strong>{confirmation_code}</strong></h3></p>'
        f'<p>Если вы не регистрировались на нашем сайте, '
        f'проигнорируйте это письмо.</p>'
        f'<p>С уважением,<br>'
        f'Ваша команда "Yamdb"</p>'
        f'</body>'
        f'</html>'
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(
        subject, message, from_email, recipient_list, html_message=message
    )
