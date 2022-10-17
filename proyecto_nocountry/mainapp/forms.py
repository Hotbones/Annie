from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
<<<<<<< HEAD
from .models import Niñera,Cliente,Reserva,Mensaje
=======
from .models import Niñera,Cliente,Reserva, Mensaje
>>>>>>> 75e1d78eba2100f257ad8a5dd09144158f391f9e


class NiñeraForm(forms.ModelForm):

    class Meta:
        model = Niñera
        fields = '__all__'
        exclude = ['perfil','created','updated']
        

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = '__all__'
        exclude = ['perfil','created','updated']


class RegisterForm(forms.Form):
    username = forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class' : 'form-control',
                                    'id' : 'username',
                                }))
    email = forms.EmailField(required=True,
                            widget=forms.EmailInput(attrs={
                                'class' : 'form-control',
                                'id' : 'username',
        }))
    password = forms.CharField(required=True,
                               min_length=4,max_length=30,
                                widget=forms.PasswordInput(attrs={
                                    'class' : 'form-control',
                                }))
    password2  = forms.CharField(label='Confirmar password',
                                required=True,
                                    widget=forms.PasswordInput(attrs={
                                        'class' : 'form-control',
                                    }))


    def clean_username(self):
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')
        return email

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2','El password no coincide')
    
    def save(self):
            return User.objects.create_user(
                self.cleaned_data.get('username'),
                self.cleaned_data.get('email'),
                self.cleaned_data.get('password')
            )
            
            
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = '__all__'
        exclude = ['created','updated']

class MensajeForm(forms.ModelForm):
    class Meta:
        model = Mensaje
<<<<<<< HEAD
        fields = '__all__'
        exclude = ['created','updated']
=======
        fields = ('puntaje','mensaje')
>>>>>>> 75e1d78eba2100f257ad8a5dd09144158f391f9e
