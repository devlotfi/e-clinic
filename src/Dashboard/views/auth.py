from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from ..decorators import login_not_required
from ..forms import SignInForm, SearchForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.db.models import Q

# Create your views here.
@login_not_required
def signIn(request: HttpRequest):
  form = SignInForm()
  if request.method == 'POST':
    form = SignInForm(request.POST)
    if form.is_valid():
      user = authenticate(request=request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
      if user is not None:
        login(request=request, user=user)
        return redirect('dashboard')
      else:
        messages.error(request=request, message="Wrong username or password")

  context = { 'form': form }
  return render(request, 'pages/auth/sign-in.html', context=context)

@login_required(login_url='sign-in')
def signOut(request: HttpRequest):
  logout(request=request)
  return redirect('sign-in')

@login_required(login_url='sign-in')
def userList(request: HttpRequest):
  form = SearchForm(request.GET)
  users = []
  if form.is_valid():
    search = form.cleaned_data['search']
    users = User.objects.filter(
      Q(id__icontains=search) |
      Q(username__icontains=search) |
      Q(email__icontains=search) |
      Q(id__icontains=search) |
      Q(date_joined__icontains=search)
    )
  else:
    users = User.objects.all()
  context = { 'users': users, 'form': form }
  return render(request, 'pages/auth/user-list.html', context=context)

@login_required(login_url='sign-in')
def addUser(request: HttpRequest):
  form = UserCreationForm()

  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='User created successfully')
      return redirect('user-list')

  context = { 'form': form }
  return render(request, 'pages/auth/add-user.html', context=context)

@login_required(login_url='sign-in')
def editUser(request: HttpRequest, userId: str):
  user = get_object_or_404(User, id=userId)
  form = UserChangeForm(instance=user)

  if request.method == 'POST':
    form = UserChangeForm(data=request.POST, instance=user)
    if form.is_valid():
      form.save()
      messages.success(request=request, message='User updated successfully')
      return redirect('user-list')

  context = { 'form': form }
  return render(request, 'pages/auth/edit-user.html', context=context)

@login_required(login_url='sign-in')
def deleteUser(request: HttpRequest, userId: str):
  user = get_object_or_404(User, id=userId)
  if request.method == 'POST':
    user.delete()
    return redirect('user-list')