from django import forms
from userspns_1184077.models import User
from captcha.fields import CaptchaField

PILIHAN = [
		('BUMN', '-Pilih-'),
		('BUMN', 'PEGAWAI'),
		('SWASTA', 'KARYAWAN'),
]

class NewUserForm(forms.ModelForm):
	kode_sekuriti = CaptchaField()
	instansi = forms.ChoiceField(choices=PILIHAN)
	class Meta:
		model = User
		fields = '__all__'
		