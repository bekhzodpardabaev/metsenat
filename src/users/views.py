from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.authtoken.serializers import AuthTokenSerializer

from .authentication import ExampleAuthentication
# from .authentication import ExampleAuthentication
from .serializers import CustomUserSerializer, UserDetailSerializer
from .models import CustomUser, Token
from rest_framework.authentication import SessionAuthentication


class CustomUserCreateView(CreateAPIView):
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()

    def perform_create(self, serializer):
        serializer.validated_data.pop("password2")
        serializer.save()


class LoginView(APIView):
    serializer_class = AuthTokenSerializer

    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token = Token.objects.filter(user=user)
        if token.count() == 3:
            token.order_by('created_at')[0].delete()
        token = Token.objects.create(user=user)
        return Response({"token": token.key})


class CustomUserDetailView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, user):
        custom_user = CustomUser.objects.get(username=user)
        serializer = UserDetailSerializer(custom_user)
        return Response(serializer.data)


class RandomListView(APIView):
    authentication_classes = (ExampleAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        print(self.request.user)
        return Response({"my user": "token"})
