
# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from .forms import CustomUserCreationForm

class SignUpView(generic.CreateView):
    form_class = CustomUserCreationForm
    # サインアップ成功後はログイン画面に飛ばす
    success_url = reverse_lazy('accounts:login')
    template_name = 'accounts/signup.html'