from jwt import decode
from django.conf import settings
from rest_framework.exceptions import AuthenticationFailed






def unhash_token(request_header):
    token = request_header.get("Authorization", "")
    if token:
        try:
            token = token.split(" ")[1]
            decoded_token = decode(token, settings.SECRET_KEY, algorithms=["HS256"])
            return decoded_token
        except IndexError:
            raise AuthenticationFailed("Invalid token format")
        except Exception as e:
            raise AuthenticationFailed("Invalid or expired token")
    else:
        raise AuthenticationFailed("Authorization header missing")




import uuid


def mock_octo_prepare_payment(data):
    return {
        "error": 0,
        "data": {
            "shop_transaction_id": data.get("shop_transaction_id"),
            "octo_payment_UUID": str(uuid.uuid4()),
            "status": "created",
            "octo_pay_url": f"https://mocked.octo.uz/pay/{uuid.uuid4()}?language=uz",
            "refunded_sum": 0,
            "total_sum": data.get("total_sum", 0),
        },
        "apiMessageForDevelopers": "Mocked response",
    }