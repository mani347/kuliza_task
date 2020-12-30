from functools import wraps

from rest_framework import status
from rest_framework.response import Response


def validate_api_payload(serializer_class):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kw):
            request = args[0].request
            serializer = serializer_class(data=request.data)
            if not serializer.is_valid():
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            return f(*args, **kw)
        return wrapper
    return decorator
