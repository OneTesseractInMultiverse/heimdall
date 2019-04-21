import hashlib
from cryptography.hazmat.backends import (
    default_backend
)
from cryptography.hazmat.primitives import (
    hashes,
    serialization
)
from cryptography.hazmat.primitives.asymmetric import (
    padding,
    rsa,
    utils
)
from cryptography.hazmat.primitives.serialization import (
    load_pem_private_key,
    load_pem_public_key
)
import pprint


def generate_rsa_key_pair(bits=4096):
    new_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=bits,
        backend=default_backend()
    )
    private_key = new_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    )
    public_key = new_key.public_key().public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.PKCS1
    )
    return {
        "public": public_key,
        "private": private_key
    }


print(type(generate_rsa_key_pair(4096)['public'].decode('utf-8')))

private_key_string = generate_rsa_key_pair(4096)['private'].decode('utf-8')
public_key_string = generate_rsa_key_pair(4096)['public'].decode('utf-8')

print("Private Key Size: {}".format(len(private_key_string)))
print("Public Key Size: {}".format(len(public_key_string)))

pprint.pprint(public_key_string)

key_private = load_pem_private_key(private_key_string.encode('utf-8'), password=None, backend=default_backend())
key_public = load_pem_public_key(public_key_string.encode('utf-8'), backend=default_backend())

# Private Key Testing
pprint.pprint(key_private.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
))

# Public Key Testing
pprint.pprint(key_public.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.PKCS1
))
