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

# Secret key that will be signed with the 'TimestampSigner' class object.
secret_key = "my secret key"

# Create a 'TimestampSigner' instance with the secret key.
timestamp_signer = TimestampSigner(secret_key, salt="new password")

# Data to be signed after undergoing serialization.
data = {"user_id": 123}

# Sign the serialized data with a timestamp.
signed_value = timestamp_signer.sign(json.dumps(data))

# Generate a random integer between 1 and 10 (inclusive).
random_digit = random.randint(1, 10)

# Simulate the passage of time (In a real-world scenario,
# this would be the time between token generation and verification).
time.sleep(random_digit)

try:
    # Verify the signature and check its expiration.
    unsigned_value = timestamp_signer.unsign(
        signed_value, max_age=5, return_timestamp=True
    )

    # Extract the timestamp and serialized data signed earlier.
    timestamp, value = unsigned_value[1], unsigned_value[0]
    current_time = timestamp_signer.get_timestamp()

    # Return the value of deserialized data and message if the token is still valid.
    print("Deserialized value:", json.loads(value))
    print("Time Count: Token is still valid")
except SignatureExpired:
    # Return a token expiration message.
    print("Token has expired.")
except BadSignature:
    # Return a message if the token altered maliciously.
    print("Invalid signature.")


if __name__ == "__main__":
    pass
