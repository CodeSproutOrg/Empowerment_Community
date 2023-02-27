from django.core.mail import send_mail


def feedback_func(form):
    name = form.data['name']
    email = form.data['email']
    feedback = form.data['feedback']
    # Send feedback to email
    send_mail('New feedback',
              f'{name} | {email} \n{feedback}',
              'empowermentonlline@gmail.com',
              ['empowermentonlline@gmail.com', ]
              )
    return 'feedback -200'
