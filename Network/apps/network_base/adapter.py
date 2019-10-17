from django.conf import settings
from allauth.account.adapter import DefaultAccountAdapter
from requests import get


class CustomUserAdapter(DefaultAccountAdapter):
    """
    Overload clean_email method for make custom verification for email.
    """
    def clean_email(self, email):
        response = get(url=f'https://api.hunter.io/v2/email-verifier?email={email}'
                           f'&api_key={settings.API_HUNTER_KEY}')
        if response.status_code == 200:
            data = response.json()
            result = data.get('data').get('result')
            if result == 'deliverable' or result == 'risky':
                return email
            else:
                raise ValueError("API Hunter didn't validate this email")
