from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


User = get_user_model()


class CustomUserCreationForm(UserCreationForm):
    template_name = 'registration/registration_form.html'
    success_url = reverse_lazy('pages:homepage')

    class Meta(UserCreationForm.Meta):
        model = User
