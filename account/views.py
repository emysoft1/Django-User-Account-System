from django.views.generic import CreateView, TemplateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from .forms import ProfileForm
from .models import Profile
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()



class HomeView(TemplateView):
    template_name = "index.html"
    
    

class SignUpView( SuccessMessageMixin, CreateView):
    model = User
    form_class = RegisterForm
    template_name = 'account/signup.html'
    success_url = reverse_lazy('login')
    success_message = 'Your account has been created!'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response

class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'account/login.html'

    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)


class ProfileUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'account/profile.html'
    success_url = reverse_lazy('profile')
    success_message = 'Profile updated successfully'

    def get_object(self, queryset=None):
        return self.request.user.profile

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, self.success_message)
        return response



class ResetPasswordView(PasswordResetView):
    template_name = 'password_reset/password_reset.html'
    email_template_name = 'password_reset/password_reset_email.html'
    subject_template_name = 'password_reset/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('password_reset')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        user = User.objects.filter(email=email).first()

        if not user:
            messages.error(self.request, 'The email address does not exist.')
            return self.render_to_response(self.get_context_data(form=form))

        return super().form_valid(form)

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'password_reset/change_password.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('home')
