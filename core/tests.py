from django.test import TestCase
from django.urls import reverse


class TestIndexView(TestCase):
    """ Testing main view """
    def test_get(self):
        response = self.client.get(reverse('main'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/main.html')

    def test_post(self):
        """ Testing POST method """
        data = {'name': 'Test User', 'email': 'test@post.com'}
        response = self.client.post(reverse('main'), data=data)
        self.assertEqual(response.status_code, 200)

