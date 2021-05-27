from django import forms


class regForm(forms.Form):
    
    Name = forms.CharField()
    Phone = forms.IntegerField()
    Dob = forms.DateField()
    PinCode = forms.IntegerField()
    Aadhar = forms.IntegerField()
    VDate = forms.DateField()
    VSlot = forms.CharField()
