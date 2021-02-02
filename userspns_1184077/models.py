from django.db import models

# Create your models here.
class User(models.Model):
	nik = models.CharField(max_length=128),
	nama_lengkap = models.CharField(max_length=128) 
	email = models.EmailField(max_length=254, unique=True) 
	tempat_lahir = models.CharField(max_length=50) 
	tanggal_lahir = models.DateField(auto_now=False) 
	instansi = models.CharField(max_length=128) 
	password = models.CharField(max_length=128) 
	confirm_password = models.CharField(max_length=128)