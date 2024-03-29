from django.shortcuts import render
from django.http import HttpRequest, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt

import braintree

# Create your views here.

gateway = braintree.BraintreeGateway(
  braintree.Configuration(
      braintree.Environment.Sandbox,
      merchant_id="kbmtyn3hd2mbxh6c",
      public_key="xtfg37zsn8ttcb74",
      private_key="98607da43f46d7f8b07b5815e9a379bf"
  )
)

def validate_user_ession(id, token):
        UserModel = get_user_model()

        try:
                user = UserModel.objects.get(pk=id)
                if user.session_token == token:
                        return True
                return False
        except UserModel.DoesNotExist:
                return False
        
@csrf_exempt
def generate_token(request,id,token):
        if not validate_user_ession(id,token):
                return JsonResponse({"error": "Invalid session, Please log in again"})
        return JsonResponse({"Client Token :" : gateway.client_token.generate(), 'success' : True })

@csrf_exempt
def process_payment(request,id, token):
        if not validate_user_ession(id,token):
                return JsonResponse({"error": "Invalid session, Please log in again"})
        nonce_from_client = request.POST("paymentMethodNonce")
        amount_from_the_client = request.POST("amount")

        result = gateway.transaction.sale({
                "amount" :amount_from_the_client,
                "payment_method_nonce": nonce_from_client,
                "options":
                {"submit_for_settlement" :True}

        })

        if result.is_success:
                return JsonResponse({
                        "Success": result.is_success,
                        "transaction": {"id" : result.transaction.id,
                                        "amount": result.transaction.amount}
                        })
        else:
                return JsonResponse({"error": True, "success": False })