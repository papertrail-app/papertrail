from cryptography.fernet import Fernet
from classes import PaperTrailDocument

my_key = Fernet.generate_key()

doc1 = PaperTrailDocument(data=b"hello world", key=my_key)
doc1.encrypt()
document = doc1.get_document()

doc2 = PaperTrailDocument(document="./qrcode.png", key=my_key)
doc2.decrypt()
data = doc2.get_data()

print(data)
