from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status


@api_view(http_method_names=("GET",))
@permission_classes(permission_classes=(IsAuthenticated,))
def index(request):
    return Response(data={"app": "Open OAuth 🚀"}, status=status.HTTP_200_OK)
