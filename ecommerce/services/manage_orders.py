from ecommerce.models import Orders
from geopy.geocoders import Nominatim
from ecommerce.common.exceptions import InvalidLatLongException


class ManageOrderService:
    def __init__(self, user, payload={}):
        self.request_payload = payload
        self.user = user

    def submit_order(self):
        try:
            geo_data = self.get_address_country_postal_code()
        except InvalidLatLongException:
            return {
                "ok": False,
                "error": "Invalid Lat OR Long"
            }
        order = Orders(user=self.user, house=self.request_payload.get("house"), lat=self.request_payload.get("lat"),
                       long=self.request_payload.get("long"), country=geo_data.get("country"),
                       postcode=geo_data.get("postcode"), address=geo_data.get("address"))
        order.save()
        response = self.request_payload
        response["ok"] = True
        return response

    def get_user_orders(self):
        user_orders = Orders.objects.filter(user=self.user)
        response = dict()
        response['ok'] = True
        response['data'] = self.generate_user_order_list_response(user_orders)
        return response

    def get_address_country_postal_code(self):
        locator = Nominatim(user_agent="myGeocoder")
        coordinates = ", ".join([str(self.request_payload.get("lat")), str(self.request_payload.get("long"))])
        location = locator.reverse(coordinates)
        if not location:
            raise InvalidLatLongException
        response = location.raw
        return {
            "address": response.get("display_name"),
            "country": response.get("address", {}).get("country"),
            "postcode": response.get("address", {}).get("postcode")
        }

    @staticmethod
    def generate_user_order_list_response(user_orders):
        orders_list = []
        for order in user_orders:
            temp = dict()
            temp['id'] = order.pk
            temp['house'] = order.house
            temp['lat'] = order.lat
            temp['long'] = order.long
            temp['country'] = order.country
            temp['postcode'] = order.postcode
            temp['address'] = order.address
            orders_list.append(temp)
        return orders_list
