from django.urls import path
# 🛑 Yeh line wapas use karein 🛑
from . import views 


urlpatterns = [
    # --- Authentication Routes ---
    path('', views.home_test, name='home'),
    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    
    # --- Main Application Routes ---
    path('dashboard/', views.dashboard_view, name='dashboard'), # Dashboard ke liye views.py mein function banana hoga
    path('withdraw/', views.submit_withdrawal_request, name='withdraw'), # Already provided logic
    
 


    path('api/api.php/', views.api_payout_handler, name='api_payout'), 
    # Humne URL ko aapke format (api.php) ke jaisa rakha hai, par yeh phir bhi Python function call karega.

    # ... other paths ...
    path('history/', views.transaction_history_view, name='transaction_history'), 
    # ...

]



