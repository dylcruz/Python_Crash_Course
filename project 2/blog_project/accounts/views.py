from django.shortcuts import redirect, render
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def registration(request):
    if request.method != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('blog_site:index')
    context = {"form": form}
    return render(request, "registration/registration.html", context)