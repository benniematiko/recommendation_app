from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth import login, authenticate,logout

from carbonlevel.forms import LoginForm, RegisterForm, UsersInputForm
# Create your views here.
#from django.http import HttpResponse



def home(request):
    return render(request, 'carbonlevel/home.html')

def sign_in(request):

    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('sign_inpage')
            
        form = LoginForm()
        return render(request, 'carbonlevel/sign_in.html', {'form': form}) 

    elif request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username, password=password)
            if user:
                login(request, user)
                messages.success(request,f'Hi {username.title()}, welcome back!')
                return redirect('dashboardpage')       
    
     # form is not valid or user is not authenticated
    messages.error(request,f'Invalid username or password') 
    return render(request, 'carbonlevel/sign_in.html')


def sign_up(request):

    if request.method == 'GET':
        form = RegisterForm()
        return render(request, 'carbonlevel/sign_up.html', { 'form': form})
    
    if request.method == 'POST':
        form = RegisterForm(request.POST) 
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, 'You have singed up successfully.')
            login(request, user)
            return redirect('sign_inpage')
        else:
            return render(request, 'carbonlevel/sign_up.html', {'form': form})

    #return render(request, 'carbonlevel/sign_up.html')

def sign_out(request):
    logout(request)
    messages.success(request,f'You have been logged out!')
    #return render(request, 'carbonlevel/sign_out.html')
    return render(request, 'carbonlevel/home.html')


#def dashboard(request):   

    #if request.method == 'GET':
            #form = UsersInputForm()
            #return render(request, 'carbonlevel/dashboard.html', {'form': form}) 
   
def dashboard(request):
    form = UsersInputForm(request.POST or None)
    return render(request, 'carbonlevel/dashboard.html' , {'form': form})

def calculatedresults(request):
    val1 = int(request.POST['houseHoldNumber'])
    val2 = int(request.POST['houseSize'])
    res = (val1 + val2) * 66   

    
    return render(request, 'carbonlevel/calculatedresults.html', {'result': res})  


