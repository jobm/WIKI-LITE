from django.contrib import admin
# Register your models here.

from authentication.forms import SignUpForm
from authentication.models import SignUp


class SignUpAdmin(admin.ModelAdmin):
    list_display = ["__unicode__", "timestamp", "updated"]
    form = SignUpForm
# class Meta:
# 	model = SignUp


admin.site.register(SignUp, SignUpAdmin)
