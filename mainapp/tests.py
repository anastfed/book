from django.contrib.auth.models import User
from django.test import TestCase, Client

# from __future__ import unicode_literals

from django.test import TestCase as DjangoTestCase
from robokassa.forms import RobokassaForm, ResultURLForm
from robokassa.conf import LOGIN, PASSWORD1, PASSWORD2


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

class RobokassaFormTest(TestCase):
    def setUp(self):
        self.form = RobokassaForm(initial={
            'OutSum': 50,
            'InvId': 1,
            'Desc': 'Покупка',
            # 'Email': ''

        })

        def testSignature(self):
            self.assertEqual(self.form._get_signature_string(),
                             '%s:50:1:%s:shpparam1=password4543:shpparam2=password4545' % (LOGIN, PASSWORD1))
            self.assertEqual(len(self.form.fields['SignatureValue'].initial), 32)

        def testSignatureMissingParams(self):
            form = RobokassaForm(initial={'InvId': 5})
            self.assertEqual(form._get_signature_string(),
                             '%s:50:1:%s:shpparam1=password4543:shpparam2=password4545' % (LOGIN, PASSWORD1))

        def testRedirectUrl(self):
            url = "https://merchant.roboxchange.com/Index.aspx?MrchLogin=Chitalocka&OutSum=50&InvId=1&Desc=b00d3a26323497e7f7d36f8887262fd5&SignatureValue=32ad004b9859a94e59f850c53aa4ad0e&shpparam1=32ad004b9859a94e59f850c53aa4ad0e&shpparam2=aa7b54caac9b87a186c89db4ddf5b5fe&isTest=1"
            self.assertEqual(self.form.get_redirect_url(), url)

class RobokassaFormExtraTest(TestCase):
    def testExtra(self):
        form = RobokassaForm(initial={
            'InvId': 1,
            'OutSum': 50,
            'param1': 'password4543',
            'param2': 'password4545'
        })
        self.assertEqual(form._get_signature_string(),
                         '%s:50:1:%s:shpparam1=password4543:shpparam2=password4545' % (LOGIN, PASSWORD1))

class ResultURLTest(DjangoTestCase):
    def testFormExtra(self):
        form = ResultURLForm({
            'OutSum': '50',
            'InvId': '1',
            'SignatureValue': '',
            'shpparam1': 'password4543',
            'shpparam2': 'password4545',
        })
        self.assertTrue(form.is_valid())
        self.assertEqual(form._get_signature_string(),
                         '50:1:%s:shpparam1=password4543:shpparam2=password4545' % (PASSWORD2))
        self.assertEqual(form.extra_params(), {'param1': 'password4543', 'param2': 'password4545'})

    def testFormValid(self):
        self.assertTrue(ResultURLForm({
            'OutSum': '50',
            'InvId': '1',
            'SignatureValue': '32ad004b9859a94e59f850c53aa4ad0e',
            'shpparam1': 'password4543',
            'shpparam2': 'password4545',
        }).is_valid())

        self.assertFalse(ResultURLForm({
            'OutSum': '50',
            'InvId': '1',
            'SignatureValue': '32ad004b9859a94e59f850c53aa4ad0e',
            'shpparam1': 'password4543',
            'shpparam2': 'password4545',
        }).is_valid())

    def testEmptyFormValid(self):
        self.assertFalse(ResultURLForm().is_valid())