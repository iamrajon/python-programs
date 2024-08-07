import hmac
import hashlib
import base64

message = "Message"
secret = "secret"

# Convert strings to bytes using UTF-8 encoding
message_bytes = message.encode('utf-8')
secret_bytes = secret.encode('utf-8')

# Generate HMAC using SHA256 algorithm
hash = hmac.new(secret_bytes, message_bytes, hashlib.sha256)

# Get the digest and encode it in base64
hashInBase64 = base64.b64encode(hash.digest()).decode()

print(hashInBase64)


# WQUn0WNePdfX7ikttNaDMbLqoXVvwwpJjxsIWtDO0Fs=
