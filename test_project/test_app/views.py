from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from test_app.forms import OrdererForm, ExecutorForm, ExperienceForm
from test_app.models import Orderer, Executor


def home(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'base.html')
    else:
        messages.success(request, 'You have to log in!')
        return redirect('login')


def admin_redirect(request):
    user = request.user
    if user.is_authenticated:
        return render(request, 'admin')
    else:
        messages.success(request, 'You have to log in!')
        return redirect('login')

@login_required
def become_orderer(request):
    user = request.user
    if request.method == 'POST':
        form = OrdererForm(request.POST)
        if form.is_valid():

            orderer = form.save(commit=False)
            orderer.user = user
            orderer.save()
            messages.success(request, "You've successfully become an orderer!")
            return redirect('home')
    else:
        form = OrdererForm()

    return render(request, 'become_orderer.html', {'form': form})

@login_required
def become_executor(request):
    user = request.user
    if request.method == 'POST':
        form = ExecutorForm(request.POST)
        if form.is_valid():

            executor = form.save(commit=False)
            executor.user = user
            executor.save()

            messages.success(request, "You've successfully become an executor!")
            return redirect('home')
    else:
        form = ExecutorForm()

    return render(request, 'become_executor.html', {'form': form})


@login_required
def set_experience(request):
    user = request.user
    executor = Executor.objects.filter(user=user).first()
    if not executor:
        messages.error(request, "You are not an executor!")
        return redirect('home')

    if request.method == 'POST':
        form = ExperienceForm(request.POST)
        if form.is_valid():
            experience = form.save(commit=False)
            experience.user = executor
            experience.save()
            messages.success(request, "Your experience has been added successfully!")
            return redirect('home')
    else:
        form = ExperienceForm()

    return render(request, 'set_experience.html', {'form': form})


@login_required
def profile(request):
    user = request.user
    context = {
        'user': user,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return render(request, 'profile.html', context)


@login_required
def profile_executor(request):
    user = request.user
    context = {
        'user': user,
        'email': user.email,
        'first_name': user.first_name,
        'last_name': user.last_name,
    }
    return render(request, 'profile-executor.html', context)
