from django.conf import settings
from django.core.mail import send_mail


def send_confirmation_email(email, confirmation_code):
    subject = 'Код подтверждения для вашего аккаунта'
    message = (
        '<html>'
        '<body>'
        '<p>Здравствуйте!</p>'
        '<p>Благодарим вас за регистрацию на нашем портале. Для завершения '
        'процесса регистрации, пожалуйста, введите следующий '
        'код подтверждения:</p>'
        f'<p><h3><strong>{confirmation_code}</strong></h3></p>'
        '<p>Если вы не регистрировались на нашем сайте, '
        'проигнорируйте это письмо.</p>'
        '<p>С уважением,<br>'
        'Ваша команда "Yamdb"</p>'
        '</body>'
        '</html>'
    )
    from_email = settings.DEFAULT_FROM_EMAIL
    recipient_list = [email]
    send_mail(
        subject, message, from_email, recipient_list, html_message=message
    )
