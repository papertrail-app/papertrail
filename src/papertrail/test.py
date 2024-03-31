from cryptography.fernet import Fernet
from papertraildocument import PaperTrailDocument

my_key = Fernet.generate_key()

string = b"x" * 2143 * 3
#string = b"hello world"
print(len(string))

doc1 = PaperTrailDocument(data=string, key=my_key)
doc1.encrypt()
document = doc1.get_document()

doc2 = PaperTrailDocument(document="./pdftest.pdf", key=my_key)
doc2.decrypt()
data = doc2.get_data()

print(data)
