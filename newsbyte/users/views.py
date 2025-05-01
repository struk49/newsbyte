from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm
from django.contrib.auth.views import LogoutView
from django.views import View  # ✅ Import View here

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "users/register.html", {"form": form})
        
    def post(self, request):
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            try:
                form.save()
                messages.success(request, "Registration successful! You can now log in.")
                return redirect("index")
            except Exception as e:
                messages.error(request, f"An error occurred during registration: {str(e)}")
                return render(request, "users/register.html", {"form": form})
        else:
            messages.error(request, "Please correct the errors below.")
            return render(request, "users/register.html", {"form": form})


class LogoutAllowGETView(LogoutView):
    http_method_names = ['get', 'post']
    template_name = 'users/logout.html'