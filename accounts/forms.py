from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


# فرم برای ساختن یوزر با فیلدهای دلخواه خودمان (آپدیت فرم دیفالت جنگو)
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm):
        model = CustomUser
        # فیلدهای دیفالت فرم جنگو
        # fields = UserCreationForm.Meta.fields + ('age',)
        # اگر بخواهیم ایمیل هم در زمان ساخت اکانت از کاربر بگیریم
        fields = ('username', 'email', 'age',)


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        # fields = UserChangeForm.Meta.fields
        fields = ('username', 'email', 'age',)
