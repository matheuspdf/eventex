from django.test import TestCase
from eventex.core.models import Speaker, Contact
from django.core.exceptions import ValidationError


class ContactModelTest(TestCase):
    def setUp(self):
        self.speaker = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='https://cdn.hashnode.com/res/hashnode/image/upload/v1679856878830/hVpMcHC'
                  'Cz.jpeg?w=500&h=500&fit=crop&crop=faces&auto=compress,format&format=webp'
        )

    def test_email(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='henrique@bastos.net'
        )

        self.assertTrue(Contact.objects.exists())

    def test_phone(self):
        contact = Contact.objects.create(
            speaker=self.speaker,
            kind=Contact.PHONE,
            value='21-996186180'
        )

        self.assertTrue(Contact.objects.exists())

    def test_choices(self):
        """Contact kind should be limited to E or P"""
        contact = Contact(speaker=self.speaker, kind='A', value='B')
        self.assertRaises(ValidationError, contact.full_clean)

    def test_str(self):
        contact = Contact(
            speaker=self.speaker,
            kind=Contact.EMAIL,
            value='henrique@bastos.net'
        )
        self.assertEqual('henrique@bastos.net', str(contact))


class ContactManagerTest(TestCase):
    def setUp(self):
        s = Speaker.objects.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='http://hbn.link/hb-pic'
        )

        s.contact_set.create(kind=Contact.EMAIL, value='henrique@bastos.net')
        s.contact_set.create(kind=Contact.PHONE, value='21-996186180')

    def test_email(self):
        qs = Contact.objects.emails()
        expected = ['henrique@bastos.net']
        self.assertListEqual(list(qs.values_list('value', flat=True)), expected)

    def test_phones(self):
        qs = Contact.objects.phones()
        expected = ['21-996186180']
        self.assertListEqual(list(qs.values_list('value', flat=True)), expected)
