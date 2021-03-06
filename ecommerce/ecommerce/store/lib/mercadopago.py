import requests
import json


class MercadoPago():

    PREFERENCE_URL = "https://api.mercadopago.com/checkout/preferences"
    PAYMAN_URL = "https://api.mercadopago.com/v1/payments"
    def __init__(self, access_token):
        self.access_token = access_token

    def get_headers(self):
        HEADERS = {"Authorization": f"Bearer {self.access_token}"}
        return HEADERS

    def create_preferences(self, data):
        dumped_data = json.dumps(data)
        response = requests.request("POST", self.__class__.PREFERENCE_URL, data = dumped_data, headers=self.get_headers())
        return response.json()

    def create_payments(self, data):
        dumped_data = json.dumps(data)
        response = requests.request("POST", self.__class__.PAYMAN_URL, data = dumped_data, headers=self.get_headers())
        return response.json()