from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Kweet
from .forms import KweetForm, UserRegistrationForm
from django.contrib.auth import login

def test_view(request):
    return render(request, 'layout.html')

def index(request):
    return render(request, "index.html")


def kweet_list(request):
    kweets = Kweet.objects.all().order_by('-created_at')
    return render(request, 'kweet_list.html', {'kweets': kweets})

@login_required
def kweet_create(request):
    if request.method == "POST":
        form = KweetForm(request.POST, request.FILES)
        if form.is_valid():
            kweet = form.save(commit=False)
            kweet.user = request.user
            kweet.save()
            return redirect('kweet_list')
    else:
        form = KweetForm()
    return render(request, 'kweet_form.html', {'form': form})

@login_required
def kweet_edit(request, kweet_id):
    kweet = get_object_or_404(Kweet, pk=kweet_id, user=request.user)
    if request.method == 'POST':
        form = KweetForm(request.POST, request.FILES, instance=kweet)
        if form.is_valid():
            kweet = form.save(commit=False)
            kweet.user = request.user
            kweet.save()
            return redirect('kweet_list')
    else:
        form = KweetForm(instance=kweet)
    return render(request, 'kweet_form.html', {'form': form})

@login_required
def kweet_delete(request, kweet_id):
    kweet = get_object_or_404(Kweet, pk=kweet_id, user=request.user)
    if request.method == 'POST':
        kweet.delete()
        return redirect('kweet_list')
    return render(request, 'kweet_confirm_delete.html', {'kweet': kweet})


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('kweet_list')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})