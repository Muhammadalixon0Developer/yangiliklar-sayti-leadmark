from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
# from captcha.fields import CaptchaField
from .models import *


class AddPostForm(forms.ModelForm):
    # def init(self, *args, **kwargs):
    #     super().init(*args, **kwargs)
    #     self.fields['cat'].empty_label = "nomsiz"

    class Meta:
        model = News
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']

    # title = forms.CharField(max_length=255)
    # slug = forms.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    # photo = forms.ImageField(upload_to="photos/%Y/%m/%d/")
    # cat = forms.ModelChoiceField(Category.objects.all())


class AddAbout(forms.ModelForm):
    class Meta:
        model = About
        fields = ['title', 'content', 'photo', ]


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='password1', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='parolni qaytaring', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    # photo = forms.ImageField(label='rasm', upload_to='usersphotos', widget=forms.ImageField(attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='name', max_length=255)
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    # captcha = CaptchaField()
