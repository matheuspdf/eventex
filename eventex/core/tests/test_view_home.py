from django.test import TestCase


class HomeTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_get(self):
        """
        GET / must return status code 200
        :return:
        """
        self.assertEqual(200, self.response.status_code)

    def test_template(self):
        """
        Must use index.html
        :return:
        """
        self.assertTemplateUsed(self.response, 'index.html')

    def test_subscription_link(self):
        self.assertContains(self.response, 'href="/inscricao/"')
