from django.shortcuts import render,redirect
from django.contrib.auth import logout,login,authenticate
from .models import Sport,GameHighlight,User
from .forms import RegisterForm

# Create your views here.
def home(request):

    sports = Sport.objects.all()
    gamehighlights = GameHighlight.objects.all()

    return render(request,'index.html',{'sports': sports, 'gamehighlights': gamehighlights})


def register(request):
    if request.method=='POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = User.objects.create_user(
                first_name = form.cleaned_data['first_name'],
                last_name = form.cleaned_data['last_name'],
                username = form.cleaned_data['username'],
                email = form.cleaned_data['email'],
                password = form.cleaned_data['password']
            )
            return redirect('/admin/login')
    else:
        form = RegisterForm()
    return render(request,'registration/register.html',{'form':form})


def logout_view(request):
    logout(request)
    return redirect('home-page')