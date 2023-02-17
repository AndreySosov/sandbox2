from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render
from .models import *

# Create your views here.

@login_required
def user_deleter(request):
    try:
        user = User.objects.get(id = request.user.id)
        logout(request)
        user.delete()
        messages.success(request, "Профиль удален")

    except User.DoesNotExist:
        messages.error(request, "Профиль не найден")
        return render(request, 'test_db_con/main.html')

    except Exception as e:
        return render(request, 'test_db_con/main.html',{'err':e.message})

    return render(request, 'test_db_con/main.html')