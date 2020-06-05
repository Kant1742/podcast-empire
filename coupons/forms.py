from django import forms
from django.contrib import messages
from .models import Coupon

class CouponApplyForm(forms.Form):
    code = forms.CharField()
    