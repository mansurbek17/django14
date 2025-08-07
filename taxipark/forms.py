from django import forms
from .models import *

class AdminForm(forms.ModelForm):
    class Meta:
        model = Admin
        fields = '__all__'

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = '__all__'

class MijozForm(forms.ModelForm):
    class Meta:
        model = Mijoz
        fields = '__all__'

class ShartnomaForm(forms.ModelForm):
    class Meta:
        model = Shartnoma
        fields = '__all__'

class CamentForm(forms.ModelForm):
    class Meta:
        model = Cament
        fields = '__all__'

class StaticForm(forms.ModelForm):
    class Meta:
        model = Static
        fields = '__all__'

class TolovForm(forms.ModelForm):
    class Meta:
        model = Tolov
        fields = '__all__'
