from django.contrib.auth import get_user_model  # it will import the user model which is currently active in this project
from django.contrib.auth.forms import UserCreationForm#useercreation form is already builtin in user authorization model


class UserCreateForm(UserCreationForm):


    class Meta:
        fields=('username','email','password1','password2')
        model=get_user_model()


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Display Name'
        self.fields['email'].label='Email Address'#customization what we want to show instead of username or Email
