import requests
from django.conf import settings


class Paystack:
    def __init__(self) -> None:
        self.url = "https://api.paystack.co/charge"
        self.headers = {
            "Authorization": f"Bearer {settings.PAYSTACK_SECRET_KEY}",
            "Content-Type": "application/json",
        }

    def charge(self, course_price, user_email, phone_number):
        data = {
            "amount": str(course_price),
            "email": user_email,
            "currency": "GHS",
            "mobile_money": {"phone": phone_number, "provider": "mtn"},
        }
        return requests.post(url=self.url, json=data, headers=self.headers)
