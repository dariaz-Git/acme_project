from django.contrib.auth import get_user_model
from django.views.generic import CreateView

from .forms import CustomUserCreationForm


User = get_user_model()


class UserCreateView(CreateView):
    model = User
    form_class = CustomUserCreationForm
