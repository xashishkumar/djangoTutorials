from django import forms

from .models import Profile

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    ('O', 'Other'),
)

JOB_CITY = [
    ('Delhi', 'Delhi'),
    ('Noida', 'Noida'),
    ('Gurgaon', 'Gurgaon'),
    ('Banglore', 'Banglore'),
    ('Mumbai', 'Mumbai'),
    ('Pune', 'Pune')
]

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [
            'name',
            'dob',
            'gender',
            'phone',
            'area',
            'city',
            'state',
            'pincode'

        ]