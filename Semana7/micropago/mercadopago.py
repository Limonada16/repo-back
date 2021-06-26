import requests
import json


class MercadoPago():

    PREFERENCE_URL = "https://api.mercadopago.com/checkout/preferences"
    def __init__(self, access_token):
        self.access_token = access_token

    def get_headers(self):
        HEADERS = {"Authorization": f"Bearer {self.access_token}"}

    def create_preferences(self, data):
        dumped_data = json.dumps(data)
        response = requests.request("POST", self.__class__.PREFERENCE_URL, data = dumped_data, headers=self.get_headers())
        return response.json

#ACCESS_TOKEN = "TEST-2929882905564744-062202-920d86c10ce08bb1c2f2b62ddcb22ee4-439357502"


# item = {
#     "title": "iphone 12",
#     "description": "El ultimo iphone",
#     "currency_id": "PEN",
#     "quantity": 1,
#     "unit_price": 6500
# }

# preferences = {
#     "items" : [item]
# }



