from django.test import TestCase
from django.core import mail


class SubscribePostValid(TestCase):
    def setUp(self):
        data = dict(name='Matheus', cpf='12345678901',
                    email='matheus@lopes.com', phone='11984028729')
        self.resp = self.client.post('/inscricao/', data)
        self.email = mail.outbox[0]

    def test_subscription_email_subject(self):
        expect = 'Confirmação de inscrição'

        self.assertEqual(expect, self.email.subject)

    def test_subscription_email_from(self):
        expect = 'matheuslopes.py@gmail.com'

        self.assertEqual(expect, self.email.from_email)

    def test_subscription_email_to(self):
        expect = ['matheuslopes.py@gmail.com', 'matheus@lopes.com']

        self.assertEqual(expect, self.email.to)

    def test_subscription_email_body(self):
        contents = [
            'Matheus',
            '12345678901',
            'matheus@lopes.com',
            '11984028729',
        ]
        for content in contents:
            with self.subTest():
                self.assertIn(content, self.email.body)
