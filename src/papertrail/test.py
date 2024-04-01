from cryptography.fernet import Fernet
from papertraildocument import PaperTrailDocument
import friendlywords

my_key = Fernet.generate_key()

#string = b"x" * 2143 * 3
#string = b"hello world"
string = bytes(friendlywords.generate('o'*1000, separator=' '), 'utf-8')
print(len(string))

designator = "test"

doc1 = PaperTrailDocument(data=string, key=my_key, designator = designator)
doc1.encrypt()
document = doc1.get_document()

doc2 = PaperTrailDocument(document=f"./papertrail_{designator}.pdf", key=my_key)
doc2.decrypt()
data = doc2.get_data()

print(data)
