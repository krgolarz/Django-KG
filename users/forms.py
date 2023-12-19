from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
        labels = {
            'first_name': 'Imie',
            'last_name': 'Nazwisko'
        }

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, *kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'uk-input'
            field.error_messages['required'] = f"Pole {field.label} jest wymagane"
            field.error_messages['max_length'] = f"Pole {field.label} jest za dlugie"
