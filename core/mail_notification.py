from django.core.mail import send_mail


def feedback_notification(name: str, email: str, feedback: str) -> str:
    send_mail('New feedback',
              f'{name} | {email} \n{feedback}',
              'empowermentonlline@gmail.com',
              ['empowermentonlline@gmail.com', ]
              )
    return 'feedback -200'
