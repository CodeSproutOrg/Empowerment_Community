import logging
from django.shortcuts import render, redirect

from .mail_notification import feedback_notification

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(funcName)s - %(message)s",
    handlers=[logging.FileHandler('./server.log', encoding='utf-8')]
)
logger = logging.getLogger(__name__)


def index(request):
    data = {"title": "Empowerment Community"}
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        feedback = request.POST.get('feedback')
        feedback_notification(name, email, feedback)
        return render(request, "pages/main.html", context=data)
    return render(request, "pages/main.html", context=data)


def pageNotFound(request, exception):
    data = {"title": "Ops, something is wrong"}
    return render(request, "pages/error.html", context=data)
