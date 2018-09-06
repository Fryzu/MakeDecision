from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False)
    last_name = forms.CharField(max_length=150, required=False)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'password1',
            'password2',
            'first_name',
            'last_name',
        )

    '''def clean(self):
        # checking for wrong data so that it wont be inserted into database
        # https://simpleisbetterthancomplex.com/article/2017/08/19/how-to-render-django-form-manually.html
        
        cleaned_data = super(RegistrationForm, self).clean()

        # all the fields are checked by the super method - reminder for adding new fields
        '''

    def save(self, commit = True):
        # overwriting the save method so that it uses all the fields

        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')

        if commit:
            user.save()

        return user