import base64
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import friendlywords as fw

from papertrail.papertraildocument import PaperTrailDocument

class PaperTrailDriver:
    def __init__(self):
        pass

    def encrypt(self, password: str, data_path: str, dest_path: str, designator: str):
        key = self.__derive_key(password)
        with open(data_path, mode="rb") as f:
            data = f.read()
            f.close()
        pt_doc = PaperTrailDocument(key=key, designator=designator, document=dest_path, data=data)
        pt_doc.encrypt()
        document = pt_doc.get_document()
        return dest_path

    def decrypt(self, password: str, document_path: str, dest_path: str) -> str:
        key = self.__derive_key(password)
        pt_doc = PaperTrailDocument(key=key, designator="", document=document_path)
        pt_doc.decrypt()
        data = pt_doc.get_data()
        with open(dest_path, 'wb') as f:
            f.write(data)
            f.close()
        return dest_path

    def gen_designator(self) -> str:
        return fw.generate('poc', separator='-').title()

    def __derive_key(self, password: str) -> bytes:
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"salt",
            iterations=480000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(bytes(password, 'utf-8')))
        return key
