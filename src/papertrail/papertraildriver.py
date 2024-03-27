import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from papertraildocument import PaperTrailDocument

class PaperTrailDriver:
    def __init__():
        pass

    def encrypt(self, password: str, data: bytes): # TODO: Add return type annotation
        key = __derive_key(password)
        pt_doc = PaperTrailDocument(key=key, data=data)
        pt_doc.encrypt()
        return pt_doc.get_document()

    def decrypt(self, password: str, document) -> bytes: # TODO: Add type for document
        key = __derive_key(password)
        pt_doc = PaperTrailDocument(key=key, document=document)
        pt_doc.decrypt()
        return pt_doc.get_data()

    def __derive_key(self, password:str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"salt",
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
