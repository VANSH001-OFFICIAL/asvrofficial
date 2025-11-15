import uuid
import hashlib
import os

def generate_api_key_set(email: str) -> tuple:
    """
    Generates a unique API Key and Secret Token for a new user.
    """
    
    # 1. Unique API Key Generation
    # Use UUID for randomness and format it nicely with the ASVR prefix
    api_key_base = str(uuid.uuid4()).replace('-', '')
    api_key = f"ASVR-{api_key_base[:16].upper()}" 
    
    # 2. Secure Secret Token Generation
    # Use a combination of email and random salt for high security
    salt = os.urandom(16)
    
    # Generate a strong hash
    secret_token_base = hashlib.sha256(email.encode('utf-8') + salt).hexdigest()
    
    # We take a fixed length for cleaner usage
    secret_token = secret_token_base[:32]
    
    return api_key, secret_token