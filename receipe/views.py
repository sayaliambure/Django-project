from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login')
def home(request):
  if request.method == "POST":
    data = request.POST
    # get name and desc from html form
    receipe_name = data.get('receipe_name')
    receipe_desc = data.get('receipe_desc')
    receipe_img = request.FILES.get('receipe_img')

    Receipe.objects.create(
          receipe_name = receipe_name,
          receipe_desc = receipe_desc,
          receipe_img  = receipe_img ,
    )
    return redirect('/home')
  
  queryset = Receipe.objects.all()

  if request.GET.get('search'):
    queryset=queryset.filter(receipe_name__icontains = request.GET.get('search'))

  context = {'receipes':queryset}

  return render(request, 'receipe/home.html', context)

def updateReceipe(request, id):
  queryset = Receipe.objects.get(id=id)
  if request.method == "POST":
    data = request.POST
    # get name and desc from html form
    receipe_name = data.get('receipe_name')
    receipe_desc = data.get('receipe_desc')
    receipe_img = request.FILES.get('receipe_img')
    
    queryset.receipe_name = receipe_name
    queryset.receipe_desc = receipe_desc

    if receipe_img:
      queryset.receipe_img=receipe_img

    queryset.save()
    return redirect('/home')

  context = {'receipe':queryset}
  return render(request, 'receipe/updateReceipe.html', context)


def deleteReceipe(request, id):
  q = Receipe.objects.get(id=id)
  q.delete()
  return redirect('/home')




def loginPage(request):
  if request.method == "POST":
    username = request.POST.get('username')
    password = request.POST.get('password')   

    if not User.objects.filter(username=username).exists(): #if username doesnot exist
      messages.error(request, 'Invalid Password')
      return redirect('/login')

    user = authenticate(username=username, password=password) # would return None if username or pw doesnot match

    if user is None:  #if user returns None
      messages.error(request, 'Invalid Password')
      return redirect('/login')

    else:   # if user is authenticated
      login(request, user)
      return redirect('/home')

  return render(request, 'receipe/login.html')



def logoutPage(request):
  logout(request)
  return redirect('/login')



def registerPage(request):
  if request.method == "POST":
    first_name = request.POST.get('first_name')
    username = request.POST.get('username')
    password = request.POST.get('password')   

    user = User.objects.filter(username=username)

    if user.exists():
      messages.error(request, 'Username already taken')
      return redirect('/register')

    user = User.objects.create(
      first_name = first_name,
      username = username,
    )

    user.set_password(password)
    user.save()

    messages.success(request, 'Account created successfully')

    return redirect('/register/')

  return render(request, 'receipe/register.html')