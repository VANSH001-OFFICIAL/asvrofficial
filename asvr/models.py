from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal

# --- 1. User Model (Simple Version) ---
class ASVRUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    # Custom Currency Balance (ASVR Tokens)
    wallet_balance = models.DecimalField(max_digits=15, decimal_places=2, default=Decimal('0.00')) 
    
    # API Keys (Registration par generate honge)
    api_key = models.CharField(max_length=30, unique=True, editable=False)
    secret_token = models.CharField(max_length=32, unique=True, editable=False)
    
    def __str__(self):
        return self.user.username

# --- 2. Withdrawal Request Model ---
class WithdrawalRequest(models.Model):
    STATUS_CHOICES = (
        ('PENDING', 'Pending Admin Approval'),
        ('APPROVED', 'Approved (Processed)'),
        ('REJECTED', 'Rejected'),
    )

    user = models.ForeignKey(ASVRUser, on_delete=models.CASCADE)
    amount_tokens = models.DecimalField(max_digits=15, decimal_places=2)
    
    # Jahan paisa bhejna hai (Bank/Phone No. details)
    recipient_details = models.TextField() 
    
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='PENDING')
    requested_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"WDR-{self.id} for {self.user.user.username}"

# --- 3. Admin Configuration (Telegram Bot Setup) ---
# Sirf ek hi row honi chahiye is table mein
class AdminConfig(models.Model):
    telegram_bot_token = models.CharField(max_length=100)
    admin_chat_id = models.CharField(max_length=50) # Jahan alerts aayenge
    
    def __str__(self):
        return "Global Admin Settings"