from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('login_view')
        else:
            messages.error(request, 'Registration failed. Try again.')
    else:
        form = UserCreationForm()
    return render(request, 'usermodule/register.html', {'form': form})


from django.contrib.auth import authenticate, login

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful.')
            return redirect('book.lab10_part2_listbooks')  # or any success page
        else:
            messages.error(request, 'Invalid credentials.')
    return render(request, 'usermodule/login.html')
