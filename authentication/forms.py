from django import forms
class Authforms(forms.Form):
    Username=forms.CharField(label="Enter your username")
    Email=forms.EmailField(label="Enter your Email")
    Password=forms.CharField(label="Enter password",widget=forms.PasswordInput)
    Password2=forms.CharField(label="confirm password",widget=forms.PasswordInput)
  
    POINTS_CHOICES2 = (   
        ('', 'Select an option'),
        ('1', '1 - Owner'),
        ('2', '2 - Manager'),
        ('3', '3 - User'),
        
    )
    class1=forms.ChoiceField(
        label="Select your role",
        choices=POINTS_CHOICES2,
        widget=forms.RadioSelect(attrs={'class': 'form-control'})
    )
  

    
   