from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
urlpatterns = [
    path('profile/', profile, name='profile'),
    # path('account', HomePage.as_view(), name='home'), #write_note
    path('logout', logout_user, name='logout'),
    # path('account/<int:pk>/edit', UpdatePage.as_view(), name='edit'),
    path('del_user/', del_user, name='delete_profile'),

    #Password RESET
    path('password-change/', PasswordChangeView.as_view(template_name='accounts/pwd_change.html'), name='pwd_change'),
    path('password-change/done/', pwd_change_done, name='password_change_done'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='accounts/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='accounts/password_reset_complete.html'),
         name='password_reset_complete'),
]
