
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from .serializers import *
from rest_framework import generics, permissions, status
from rest_framework.permissions import IsAuthenticated
from .utils import unhash_token
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import NotFound, AuthenticationFailed
from django.contrib.auth.hashers import make_password, check_password
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema



class UserRegistrationAPIView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()


            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)

            return Response({
                "uid": user.uid,
                "message": "User registered successfully!",
                "refresh": str(refresh),
                "access": access_token
            }, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class RetrieveProfileView(generics.RetrieveAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uid'

    def get(self, request, *args, **kwargs):
        decoded_token = unhash_token(self.request.headers)
        user_id = decoded_token.get('user_id')

        if not user_id:
            raise NotFound("User not found")

        user = get_object_or_404(User, uid=user_id)
        serializer = self.get_serializer(user)

        return Response(serializer.data)


class UpdateProfileView(generics.UpdateAPIView):
    serializer_class = UserUpdateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "uid"

    def get_queryset(self):
        decoded_token = unhash_token(self.request.headers)
        user_id = decoded_token.get('user_id')
        return User.objects.filter(uid=user_id)


class PasswordResetView(APIView):
    queryset = User.objects.all()
    serializer_class = PasswordResetSerializer
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        request_body=PasswordResetSerializer
    )
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        decoded_token = unhash_token(request.headers)
        user_id = decoded_token.get("user_id")

        if not user_id:
            raise AuthenticationFailed("User ID not found in token")

        old_password = serializer.validated_data.get("old_password")
        new_password = serializer.validated_data.get("new_password")

        user = get_object_or_404(User, uid=user_id)

        if not check_password(old_password, user.password):
            return Response(
                {"error": "Incorrect old password!"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.password = make_password(new_password)
        user.save()

        return Response({"data": "Password changed successfully"}, status=status.HTTP_200_OK)


class DeleteProfileAPIView(generics.DestroyAPIView):
    serializer_class = UserProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'uid'

    def get_queryset(self):
        decoded_token = unhash_token(self.request.headers)
        user_id = decoded_token.get('user_id')
        return User.objects.filter(uid=user_id)

    def perform_destroy(self, instance):

        instance.delete()

    def delete(self, request, *args, **kwargs):

        user = self.get_object()

        self.perform_destroy(user)

        return Response({"message": "User successfully deleted"}, status=status.HTTP_204_NO_CONTENT)




import requests
import time
from datetime import datetime
from rest_framework import status, permissions, generics
from rest_framework.response import Response

class OctoPaymentInitView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = OctoPaymentInitSerializer
    def post(self, request, *args, **kwargs):
        try:
            user = request.user

            shop_transaction_id = f"order_{int(time.time() * 1000)}"

            user_data = {
                "user_id": str(user.uid),
                "phone": user.phone_number.replace("+", ""),
                "email": user.email,
            }

            payload = {
                "octo_shop_id": 27137,
                "octo_secret": "3be1f3d7-9a10-4e8a-af18-5ee82c428baa",
                "shop_transaction_id": shop_transaction_id,
                "auto_capture": True,
                "test": True,
                "init_time": datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S"),
                "user_data": user_data,
                "total_sum": 2500.0,
                "currency": "UZS",
                "description": "PAYMENT",
                "basket": [
                    {"count": 2, "position_desc": "VIP", "price": 1000.0},
                    {"count": 1, "position_desc": "VIP", "price": 500.0},
                ],
                "payment_methods": [
                    {"method": "bank_card"},
                    {"method": "uzcard"},
                    {"method": "humo"},
                ],
                "tsp_id": 18,
                "return_url": "https://octo.uz",
                "notify_url": "https://notify-url.uz",
                "language": "uz",
                "ttl": 15,
            }

            response = requests.post("https://pay.octo.uz/api/init-payment", json=payload)
            data = response.json()

            if response.status_code == 200 and data.get("error") == 0:
                return Response({
                    "status": "success",
                    "payment_url": data["data"]["octo_pay_url"],
                    "transaction_id": data["data"]["shop_transaction_id"],
                    "uuid": data["data"]["octo_payment_UUID"],
                    "total_sum": data["data"]["total_sum"],
                }, status=status.HTTP_200_OK)

            return Response({
                "status": "failed",
                "error": data.get("errMessage", "Unexpected error"),
                "raw": data
            }, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
