from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from authorization.models import ParkUser
import django.forms as forms

class MyUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = ParkUser
        fields = ('username', 'first_name', 'last_name', 'password1', 'password2', 'email', 'age', 'avatar' )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''


class MyUserChangeForm(UserChangeForm):

    class Meta:
        model = ParkUser
        fields = ('username', 'first_name', 'last_name', 'password', 'email', 'age', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__( *args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.help_text = ''
            if field_name == 'password':
                field.widget = forms.HiddenInput()
