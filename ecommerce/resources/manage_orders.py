from django.http import JsonResponse
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from ecommerce.common.decorators import validate_api_payload
from ecommerce.common.serializers import SubmitOrderRequestSerializer
from ecommerce.services.manage_orders import ManageOrderService
from ecommerce.common.exceptions import InvalidLatLongException


class ManageOrders(APIView):
    permission_classes = [IsAuthenticated]

    @validate_api_payload(SubmitOrderRequestSerializer)
    def post(self, request):
        request_payload = request.data
        service = ManageOrderService(request.user, request_payload)
        try:
            response = service.submit_order()
        except InvalidLatLongException:
            response = {
                "ok": False,
                "error": "Invalid Lat OR Long"
            }
            return JsonResponse(data=response, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse(data=response, status=status.HTTP_200_OK)

    def get(self, request):
        service = ManageOrderService(request.user)
        response = service.get_user_orders()
        return JsonResponse(data=response, status=status.HTTP_200_OK)
