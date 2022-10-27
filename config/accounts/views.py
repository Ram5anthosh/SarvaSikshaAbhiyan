from django.shortcuts import render,redirect
from .forms import VolunteerForm
from django.contrib import messages
from .models import Volunteer

# Create your views here.

def signup(request):
    if request.method == "POST":
        form=VolunteerForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect(signup)
    else:
        return render(request, 'signup.html',{})


def signin(request):
#    if request.method == "POST":
#        username = request.POST['username']
#        passwd = request.POST['passwd']
#        all_users=Volunteer.objects.all 
#        for item in all_users:
#            if username == item.username:
#                if passwd == item.username:
#                    messages.success(request,('You are successfully logged in!'))
#                    return redirect('home')
#               else:
#                    messages.success(request, ('You entered wrong password!'))
#                    return redirect('signin')
    return render(request, 'signin.html',{})

