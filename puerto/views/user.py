from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from django.contrib.auth.models import User

from puerto.serializers.user import UserSerializer
from puerto.pagination import StandardPagination


class UserViewSet(viewsets.ModelViewSet):
    queryset           = User.objects.all().order_by('id')
    serializer_class   = UserSerializer
    permission_classes = [IsAdminUser]
    pagination_class   = StandardPagination

    @action(
        detail=False,
        methods=['get'],
        permission_classes=[IsAuthenticated],
        url_path='profile',
    )
    def profile(self, request):
        serializer = UserSerializer(request.user)
        return Response(serializer.data)
