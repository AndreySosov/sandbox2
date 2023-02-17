from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import PasswordChangeView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib import messages


from .forms import UpdateUserForm, UpdateProfileForm
from .services import user_deleter


# Create your views here.

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'accounts/pwd_change.html'
    success_message = "Successfully Changed Your Password"
    success_url = reverse_lazy('profile')


# RESERT USERS PWD
class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    email_template_name = 'accounts/password_reset_email.html'
    subject_template_name = 'accounts/password_reset_subject'
    success_message = "We've emailed you instructions for setting your password, " \
                      "if an account exists with the email you entered. You should receive them shortly." \
                      " If you don't receive an email, " \
                      "please make sure you've entered the address you registered with, and check your spam folder."
    success_url = reverse_lazy('main/home')


def logout_user(request):
    logout(request)
    return redirect('/')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)
    return render(request, 'accounts/profile.html', {'user_form': user_form, 'profile_form': profile_form})



def del_user(request):
    user_deleter(request)
    return render(request, 'main/main.html')


@login_required
def pwd_change_done(request):
    logout(request)
    return redirect('main/main')