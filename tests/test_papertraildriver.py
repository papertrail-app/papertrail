# Unit tests for PaperTrailDriver

import unittest as ut
import filecmp as fc
import os
from papertrail.papertraildriver import PaperTrailDriver

class TestPaperTrailDriver(ut.TestCase)

    def test_encrypt_text(self):
        '''Test encrypting a text file'''
        # Note: This may not be possible to do depending on PDF metadata
        driver = PaperTrailDriver()
        password = "password1234"
        in_path = os.path.join("resources", "text01.txt")
        out_path = "tmp_pdf01.pdf"
        ref_path = os.path.join("resources", "pdf01.pdf")
        designator = "PDF_01"
        driver.encrypt(password, in_path, out_path, designator)
        self.assertTrue(fc.cmp(out_path, ref_path, shallow=False))

    def test_encrypt_image(self):
        '''Test encrypting an image file'''
        # Note: This may not be possible to do depending on PDF metadata
        driver = PaperTrailDriver()
        password = "password1234"
        in_path = os.path.join("resources", "img02.png")
        out_path = "tmp_pdf02.pdf"
        ref_path = os.path.join("resources", "pdf02.pdf")
        designator = "PDF_02"
        driver.encrypt(password, in_path, out_path, designator)
        self.assertTrue(fc.cmp(out_path, ref_path, shallow=False))

    def test_decrypt_text(self):
        '''Test decrypting a known document into text'''
        driver = PaperTrailDriver()
        password = "password1234"
        in_path = os.path.join("resources", "pdf01.pdf")
        out_path = "tmp_text01.txt"
        ref_path = os.path.join("resources", "text01.txt")
        driver.decrypt(password, in_path, out_path)
        self.assertTrue(fc.cmp(out_path, ref_path, shallow=False))

    def test_decrypt_image(self):
        '''Test decrypting a known document into an image'''
        driver = PaperTrailDriver()
        password = "password1234"
        in_path = os.path.join("resources", "pdf02.pdf")
        out_path = "tmp_img02.png"
        ref_path = os.path.join("resources", "img02.png")
        driver.decrypt(password, in_path, out_path)
        self.assertTrue(fc.cmp(out_path, ref_path, shallow=False))

    def test_encryptdecrypt_text(self):
        '''Test encrypting known text data and then decrypting it'''
        driver = PaperTrailDriver()
        password = "password1234"
        in_path = os.path.join("resources", "text01.txt")
        inter_path = "tmp_pdf03.pdf"
        out_path = "tmp_text03.txt"
        ref_path = os.path.join("resources", "text01.txt")
        designator = "PDF_03"
        driver.encrypt(password, in_path, inter_path, designator)
        driver.decrypt(password, inter_path, out_path)
        self.assertTrue(fc.cmp(out_path, ref_path, shallow=False))

    def test_encryptdecrypt_text(self):
        '''Test encrypting known image data and then decrypting it'''
        driver = PaperTrailDriver()
        password = "password1234"
        in_path = os.path.join("resources", "img02.png")
        inter_path = "tmp_pdf04.pdf"
        out_path = "tmp_img04.png"
        ref_path = os.path.join("resources", "img02.png")
        designator = "PDF_04"
        driver.encrypt(password, in_path, inter_path, designator)
        driver.decrypt(password, inter_path, out_path)
        self.assertTrue(fc.cmp(out_path, ref_path, shallow=False))

if __name__ == "__main__":
    ut.main()

    
