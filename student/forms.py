from django import forms
from student.models import Profile

GENDER_CHOICE=(
    ('M','MALE'),
    ('F','FEMALE'),
    ('O','OTHER'),
)

JOB_CITY_CHOICE=(
    ("Bangalore", "Bangalore"),
    ("Hyderabad", "Hyderabad"),
    ("Pune", "Pune"),
    ("Mumbai", "Mumbai"),
    ("Delhi", "Delhi"),
    ("Gurgaon", "Gurgaon"),
    ("Noida", "Noida"),
)

class profileform(forms.ModelForm):
    gender =forms.ChoiceField( 
        choices=GENDER_CHOICE, 
        widget=forms.RadioSelect)
    
    job_city=forms.MultipleChoiceField(
        choices=JOB_CITY_CHOICE,
        widget=forms.CheckboxSelectMultiple,
        label='preffered job cities',
        help_text='select one or more cities where you prefer to work'
    )
    
    class Meta:
        model=Profile
        fields=[
            'name','dob','gender','locality','city','pin','state','mobile','email','job_city','profile_image','my_file'
        ]
        labels ={
            'name':'Full name',
            'dob':'Date Of Birth',
            'pin':'Pin Code',
            'mobile' : 'Mobile Number',
        }
        #giving help text through form same as we give in modle for some feild
        help_texts={
            'profile_image':'optional:Upload a profile image',
            'my_file':'optional:Attach any additional document(PDF,DOCX,etc.)'
        }
        #applying css
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'dob':forms.DateInput(attrs={'class':'form-control','id':'datepicker','type':'date'}),
            'locality':forms.TextInput(attrs={'class':'form-control','placeholder':'write your area name'}),
            'pin':forms.NumberInput(attrs={'class':'form-control','placeholder':'6-digit pin code'}),
            'city':forms.TextInput(attrs={'class':'form-control','placeholder':'city'}),
            'state':forms.Select(attrs={'class':'form-select'}),
            'mobile':forms.NumberInput(attrs={'class':'form-control','placeholder':'enter your mobile number'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'enter email address'}),
            'job_city':forms.TextInput(attrs={'class':'form-control','placeholder':'city'}),

        }