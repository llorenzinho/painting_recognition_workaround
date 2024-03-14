import base64
import binascii

def base64_to_bytes(base64_string: str) -> bytes:
    # convert base64 to image bytes
    return base64.b64decode(base64_string)

# check if string is in base64 format
def is_base64(base64_string: str) -> bool:
    try:
        base64.b64decode(base64_string)
        return True
    except binascii.Error:
        return False