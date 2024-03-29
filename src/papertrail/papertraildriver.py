import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

from papertraildocument import PaperTrailDocument

class PaperTrailDriver:
    def __init__():
        pass

    def encrypt(self, password: str, data_path: str, dest_path: str):
        key = __derive_key(password)
        # TODO: Read data file from given path into bytes
        pt_doc = PaperTrailDocument(key=key, data=data)
        pt_doc.encrypt()
        document = pt_doc.get_document()
        # TODO: Save document to given dest_path

    def decrypt(self, password: str, document_path: str, dest_path: str):
        key = __derive_key(password)
        # TODO: Read dpcument from given path into something
        pt_doc = PaperTrailDocument(key=key, document=document)
        pt_doc.decrypt()
        data = pt_doc.get_data()
        # TODO: Save data to given dest_path

    def __derive_key(self, password:str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"salt",
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(password))
        return key
