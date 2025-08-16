# apps/user/forms.py
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django import forms
from apps.core.widgets import AdminAvatarWidget 

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
            'avatar': AdminAvatarWidget,
        }

    def save(self, commit=True):
        user = super().save(commit=False)

        if self.data.get('delete_avatar') == '1' and user.avatar:
            user.avatar.delete(save=False)  
            user.avatar = None              

        if commit:
            user.save()
        return user


class CustomUserForm(forms.ModelForm):
    delete_avatar = forms.BooleanField(required=False, widget=forms.HiddenInput())

    class Meta:
        model = User
        fields = '__all__'
        widgets = {
            'avatar': AdminAvatarWidget,
        }

    def clean_delete_avatar(self):
        return self.data.get('delete_avatar') in ['1', 'true']

    def save(self, commit=True):
        instance = super().save(commit=False)

        if self.cleaned_data.get('delete_avatar'):
            if instance.avatar:
                instance.avatar.delete(save=False)
            instance.avatar = None  

        if commit:
            instance.save()
        return instance