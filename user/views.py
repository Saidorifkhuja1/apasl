import requests
from rest_framework.generics import GenericAPIView
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
from datetime import datetime


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





class OctoPaymentInitView(GenericAPIView):
    serializer_class = OctoPaymentSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        full_name = serializer.validated_data['full_name']
        phone_number = serializer.validated_data['phone_number']
        email = serializer.validated_data['email']
        count = serializer.validated_data['count']

        total_price = 2500  # fixed total price, or calculate dynamically
        transaction_id = f"order_{int(datetime.now().timestamp() * 1000)}"

        # Calculate price per item using integer division
        price_per_item = total_price // count
        basket = [{"count": count, "position_desc": "VIP", "price": price_per_item}]

        # Ensure basket sum matches total_price exactly
        basket_sum = sum(item["count"] * item["price"] for item in basket)
        if basket_sum != total_price:
            diff = total_price - basket_sum
            basket[-1]["price"] += diff

        payload = {
            "octo_shop_id": 27137,
            "octo_secret": "3be1f3d7-9a10-4e8a-af18-5ee82c428baa",
            "shop_transaction_id": transaction_id,
            "auto_capture": True,
            "test": True,
            "init_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "user_data": {
                "user_id": full_name,
                "phone": phone_number,
                "email": email,
            },
            "total_sum": total_price,
            "currency": "UZS",
            "description": "TEST_PAYMENT",
            "basket": basket,
            "payment_methods": [
                {"method": "bank_card"},
                {"method": "uzcard"},
                {"method": "humo"},
            ],
            "tsp_id": 18,
            "return_url": "https://octo.uz",
            "notify_url": "https://notify-url.uz",
            "language": "uz",
            "ttl": 15
        }

        try:
            response = requests.post(
                "https://secure.octo.uz/prepare_payment",
                json=payload,
                timeout=10,
                headers={"Content-Type": "application/json"},
                proxies={"http": None, "https": None}
            )

            data = response.json()

            if data.get("error") == 0:
                return Response({
                    "pay_url": data["data"]["octo_pay_url"],
                    "transaction_id": data["data"]["shop_transaction_id"],
                    "uuid": data["data"]["octo_payment_UUID"]
                }, status=status.HTTP_200_OK)
            else:
                return Response({"error": data.get("errMessage", "Payment initialization failed.")},
                                status=status.HTTP_400_BAD_REQUEST)

        except requests.RequestException as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


