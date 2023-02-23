from django import forms



class UserReg(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.CharField(max_length=100)
    password = forms.CharField()

class UserLogin(forms.Form):
    username = forms.CharField(max_length=100)
    user_password = forms.CharField(max_length=100)


class MembersReg(forms.Form):
    name = forms.CharField(max_length=100)
    age = forms.CharField(max_length=100)
    phone = forms.CharField()
    city = forms.CharField()
    country = forms.CharField()