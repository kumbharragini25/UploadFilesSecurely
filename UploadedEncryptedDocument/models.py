from django.db import models
from cryptography.fernet import Fernet

class UploadedEncryptedDocument(models.Model):
    name = models.CharField(max_length=255)
    encrypted_file = models.FileField(upload_to='uploads/encrypted/')

    def encrypt_file(self, file):
       
        key = Fernet.generate_key()
        
        
        f = Fernet(key)
        
       
        with file.open('rb') as f:
            file_content = f.read()
        
        
        encrypted_content = f.encrypt(file_content)
        
       
        self.encrypted_file.save(file.name, encrypted_content)

    def decrypt_file(self):
        
        f = Fernet(self.key)
        
       
        with self.encrypted_file.open('rb') as f:
            encrypted_content = f.read()
        
        
        decrypted_content = f.decrypt(encrypted_content)
        
        return decrypted_content