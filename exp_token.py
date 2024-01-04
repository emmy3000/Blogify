#!/usr/bin/env python3
"""
Simple demonstration script illustrating the serialization and signing of tokens
using the 'itsdangerous' library.

- This serves as a foundation for implementing the ability to securely reset passwords
  in the "Blogify" web application.
- The script generates a signed token, simulates the passage of time,
  and then verifies the token's signature and expiration.
"""

from itsdangerous import TimestampSigner, BadSignature, SignatureExpired
import json
import time
import random

# Secret key for signing
secret_key = "my secret key"

# Create a TimestampSigner with the secret key
timestamp_signer = TimestampSigner(secret_key)

# Data to be signed
data = {"user_id": 123}

# Sign the data with timestamp
signed_value = timestamp_signer.sign(json.dumps(data))

# Generate a random integer between 1 and 10 (inclusive)
random_digit = random.randint(1, 10)

# Simulate the passage of time (In a real-world scenario,
# this would be the time between token generation and verification)
time.sleep(random_digit)

try:
    # Verify the signature and check expiration
    unsigned_value = timestamp_signer.unsign(signed_value, max_age=5, return_timestamp=True)

    # Extract timestamp and data
    timestamp, value = unsigned_value[1], unsigned_value[0]
    current_time = timestamp_signer.get_timestamp()

    print("Deserialized value:", json.loads(value))
    print("Time Count: Token is still valid")
except SignatureExpired:
    print("Token has expired.")
except BadSignature:
    print("Invalid signature.")

if __name__ == "__main__":
    pass
