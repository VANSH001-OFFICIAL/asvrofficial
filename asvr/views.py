from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from decimal import Decimal

# 🛑 Sabhi Models ko sirf ek line mein import karein 🛑
from .models import ASVRUser, Transaction 

# Utils/Helper Functions ko import karein
from .utils import check_payout_limits 
def home_test(request):
    # Yeh check karne ke liye ki view load ho raha hai
    return JsonResponse({'status': 'ok', 'message': 'Deployment successful!'}, status=200)

# ... (baaki views functions yahaan shuru honge)

# --- Payout API Endpoint ---

# @csrf_exempt: Isse hattana recommended hai real production mein, par demo ke liye rakhte hain.
'''@csrf_exempt
@require_http_methods(["GET"]) # GET request se data le rahe hain, jaisa ki aapke URL format mein hai
@transaction.atomic
def api_payout_handler(request):
    # 1. URL Parameters lena (API Key aur Payout details)
    api_token = request.GET.get('token')
    recipient_number = request.GET.get('paytm') # Ya koi bhi phone/payment ID
    amount_str = request.GET.get('amount')
    comment = request.GET.get('comment', 'ASVR Payout')
    
    # --- Input Validation ---
    if not all([api_token, recipient_number, amount_str]):
        return JsonResponse({'status': 'FAILED', 'message': 'Missing required parameters (token, paytm, amount).'}, status=400)

    try:
        # Amount ko Decimal mein convert karna
        amount = Decimal(amount_str)
        if amount <= 0:
            raise ValueError
    except:
        return JsonResponse({'status': 'FAILED', 'message': 'Invalid amount provided.'}, status=400)

    # --- 2. API Key Authentication ---
    try:
        # Token ko API Key se match karna
        user_profile = ASVRUser.objects.select_for_update().get(api_key=api_token)
        # select_for_update() ensures ki balance check aur debit ek saath ho (race condition se bachne ke liye)
        
    except ASVRUser.DoesNotExist:
        return JsonResponse({'status': 'FAILED', 'message': 'Invalid API Token.'}, status=403)

    # --- 3. Balance Aur Limits Check ---
    if user_profile.wallet_balance < amount:
        return JsonResponse({'status': 'FAILED', 'message': 'Insufficient ASVR Token balance.'}, status=400)
    
    # *Optional*: check_payout_limits(user_profile, amount) jaise function yahan use ho sakta hai.

 # --- 4. Transaction Processing ---
    
    # A. User ke wallet se tokens debit karna
    user_profile.wallet_balance -= amount
    user_profile.save()
    
    # B. Payout ko process karna (Actual Bank Integration)
    # *******************************************************************
    # Yahan woh code aayega jo asli mein third-party IMPS/NEFT/Payment Partner API ko call karega
    # (Maan lijiye ki yeh call SUCCESSFUL hua)
    # *******************************************************************
    
    # C. Transaction Record banana (database mein store karna)
    # Humein isse UNCOMMENT karke final karna hai:
    
    new_txn = Transaction.objects.create(
        user=user_profile,
        type='PAYOUT',
        amount=amount,
        status='SUCCESS', # Ya 'PENDING' agar bank API response ka wait karna hai
        recipient_details=f"P: {recipient_number} ({comment})", # Details save kiye
        # transaction_id field model mein default set hai
    )
    
    # --- 5. Success Response ---
    return JsonResponse({
        'status': 'SUCCESS',
        'message': f'Payout of {amount} ASVR Tokens to {recipient_number} successfully initiated.',
        'transaction_id': new_txn.transaction_id # Ab hum naya generated ID bhej rahe hain
    })

@login_required
def transaction_history_view(request):
    # Logged-in user ka ASVR profile lena
    user_profile = ASVRUser.objects.get(user=request.user)
    
    # Sirf iss user ki saari transactions latest se pehle tak fetch karna
    transactions = Transaction.objects.filter(
        user=user_profile
    ).order_by('-created_at') # Newest transaction sabse pehle dikhegi
    
    context = {
        'transactions': transactions,
        'current_balance': user_profile.wallet_balance
    }
    

    return render(request, 'transaction_history.html', context)'''

