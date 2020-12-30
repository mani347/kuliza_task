from django.http import JsonResponse
from rest_framework import status
from rest_framework.views import APIView

from ecommerce.common.decorators import validate_api_payload
from ecommerce.common.serializers import RegistrationRequestSerializer
from ecommerce.services.registration import RegistrationService


class Registration(APIView):
    permission_classes = []

    @validate_api_payload(RegistrationRequestSerializer)
    def post(self, request):
        request_payload = request.data
        service = RegistrationService(request_payload)
        response = service.register_user()
        return JsonResponse(data=response, status=status.HTTP_200_OK)
