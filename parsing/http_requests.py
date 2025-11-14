"""
# Challenge 14: Build a breach checker
def check_password_breach(password):
    
    Use haveibeenpwned API to check if password is compromised
    
    API: https://api.pwnedpasswords.com/range/{first5_hash_chars}
    1. Hash password with SHA1
    2. Send first 5 chars of hash to API
    3. Check if rest of hash appears in response
    4. Return number of times seen in breaches
    
    Handle all network errors gracefully
    
    pass

# Test with: check_password_breach("password123")
"""
