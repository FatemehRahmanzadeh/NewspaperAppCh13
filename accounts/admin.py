from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


# برای اینکه از مدل و فرم های تعریف شده خودمان بجای یوزر جنگو استفاده کنیم
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser

    # تعیین می کنیم که چه فیلدهایی در پنل ادمین ما نمایش داده شوند
    list_display = ['email', 'username', 'age', 'is_staff', ]

    # در زمان تغییر یا ویرایش یوزر چه فیلدهایی نمایش داده شود
    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields': ('age',)}),
    )
    # در زمان ساخت یوزر جدید چه فیلدهایی نمایش داده شود
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields': ('age',)}),
    )


admin.site.register(CustomUser, CustomUserAdmin)
