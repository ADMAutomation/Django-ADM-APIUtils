from django.test import TestCase
from django.utils import timezone
from datetime import timedelta
from django.core.exceptions import ValidationError
from modelsAbstracts import TokensAbstract
# Create your tests here.
class TokensTestCase(TestCase):
    def test_abstract(self):
        el = TokensAbstract()
        el.clean()
        str(el)
        """
        Dates
        """
        el.creationDateTime = timezone.now()
        el.expirationDateTime = timezone.now() + timedelta(days=1)
        el.clean()
        el.creationDateTime = timezone.now() + timedelta(days=2)
        self.assertRaises(ValidationError, el.clean)
        """
        Token
        """
        el.token = el.generateToken()
        str(el)
