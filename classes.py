from cryptography.fernet import Fernet
import qrcode
import cv2

class PaperTrailDocument:
    def __init__(self, key: bytes, data = None, document = ""):
        # Initialize a document with data and Fernet key

        # Initial assignments
        self.document = document
        self.data = data
        self.key = key
        
    def encrypt(self):
        # Encrypt data using key into a document and store in self

        # Encrypt data into Fernet token
        fernet = Fernet(self.key)
        enc_data = fernet.encrypt(self.data)

        # Generate QR code
        qr = qrcode.QRCode(
            version = 1,
            error_correction = qrcode.constants.ERROR_CORRECT_L,
            box_size = 10,
            border = 4,
        )
        qr.add_data(enc_data)
        img = qr.make_image(fill_color = "black", back_color = "white")
        img.save("./qrcode.png")
        self.document = "./qrcode.png"
        
    def decrypt(self):
        # Decrypt document with key into data and store in self

        # Initialize QR code detector
        img = cv2.imread(self.document)
        detector = cv2.QRCodeDetector()
        enc_data, bbox, straight_qrcode = detector.detectAndDecode(img)
        
        # Initialize Fernet and decrypt
        fernet = Fernet(self.key)
        self.data = fernet.decrypt(enc_data)

    def get_data(self):
        # Get data if present, if not return an empty bytestring
        return self.data

    def get_document(self):
        # Get document if present, if not return some sort of null response
        return self.document
