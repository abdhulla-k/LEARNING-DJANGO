from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import RegisterForm

# Create your views here.

# register user
def register( request ):
    if request.method == 'POST':
        form = RegisterForm( request.POST )
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get( username )
            messages.success( request, f'Welcome {username}, your account is successfully created!' )
            return redirect( 'food:index' )
    else:
        form = RegisterForm()
    return render( request, 'users/register.html', { 'form' : form })