
import re
from django.shortcuts import render , redirect
from .forms import AccountCreationForm, LoginForm

from django.contrib.auth import authenticate, login, logout



def email_to_name(email):
    "Generates display name from an email"
    username = email.split("@")[0]
    parts = re.findall(r"[a-zA-Z]+", username)

    if len(parts) == 2:
        display_name = " ".join(parts)
    elif parts:
        display_name = max(parts, key=len)
        if len(display_name) < 3:
            display_name = username
    else:
        display_name = username
    display_name = display_name[:30]
    display_name = display_name.strip().title()
    return display_name




def register(request):
    if request.method == 'POST':
        form = AccountCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to login page
            return redirect('account:login')
            
    else:
        form = AccountCreationForm()
    return render(request, 'account/register.html', {'form': form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        # validate email and password
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("account:home")
    else:
        form = LoginForm()
    context = {"form": form}
    return render(request, "account/login.html", context)


def home(request):
    message =  "Your account has been login successful .."
    email = request.user.email 
    username = email_to_name(email)
    return render(request, 'index.html', {'message': message, 'username': username})


# logout function
def logout_request(request):
    logout(request)
    return redirect("account:login")