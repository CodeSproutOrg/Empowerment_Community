import logging
from django.shortcuts import render

from .forms import ContactForm
from .func import feedback_func

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(funcName)s - %(message)s",
    handlers=[logging.FileHandler('./server.log', encoding='utf-8')]
)
logger = logging.getLogger(__name__)


def index(request):
    form = ContactForm(request.POST)
    data = {
        "title": "Empowerment Community",
        'form': form,
    }
    if not form.is_valid():
        return render(request, "pages/main.html", context=data)
    else:
        feedback_func(form)
        return render(request, "pages/main.html", context=data)


def pageNotFound(request, exception):
    data = {"title": "Ops, something is wrong"}
    return render(request, "pages/error.html", context=data)
