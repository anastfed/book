from django.contrib.auth.models import User
from django.test import TestCase, Client


class TestMainApp(TestCase):
    # def setUp(self):
    #     # prepare to each test in class
    #     self.client = Client()
    #     self.user_1 = User.objects.create_user(
    #         username='user1',
    #         email='user1@kpk.kss45.ru',
    #         password='pass'
    #     )
    #     self.user_2_credentials = {
    #         'username': 'user2',
    #         'email': 'user2@kpk.kss45.ru',
    #         'password': 'kpkpkpk23'
    #     }
    #     self.users = [self.user_1, ]

    def test_index_page(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200, 'неверный код ответа')

        self.assertIn('главная', response.content.decode(), 'главная не найдена')
        self.assertIn('войти', response.content.decode(), 'войти не найдено')
        # print(response.context.keys())
        self.assertFalse(response.context['user'].is_authenticated)

