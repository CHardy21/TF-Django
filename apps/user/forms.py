# apps/user/forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class SignUpForm(forms.ModelForm):
    password = forms.CharField(
        widget=forms.PasswordInput,
        label="Contraseña"
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirmar contraseña"
    )

    class Meta:
        model = User
        fields = ["username", "email", "password",  "avatar"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este correo ya está en uso.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")

        if password and password2 and password != password2:
            self.add_error("password2", "Las contraseñas no coinciden.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])  # Encripta la contraseña
        if commit:
            user.save()
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['avatar', 'username', 'email', 'avatar']
        
class EditProfileForm(forms.ModelForm):
    
    email = forms.EmailField(
        disabled=True,
        widget=forms.EmailInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
    )

    class Meta:
        model = User
        fields = ['avatar', 'first_name', 'last_name', 'email']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'avatar': forms.FileInput(attrs={'class': 'form-control'}),
        }

