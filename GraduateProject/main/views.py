from django.shortcuts import render
from django.contrib import auth
from django.http import HttpResponseRedirect 
from main.models import Img

# Create your views here.

def main(request):

	isUploadImg = False
	img = None

	if request.method == 'POST':
		img = Img(img_url = request.FILES.get('img'))
		img.save()
		isUploadImg = True

	imgs = Img.objects.all()
	currentImg = img
	context = {
		'imgs' : imgs,
		'isUploadImg' : isUploadImg,
		'currentImg' : currentImg
	}

	return render(request, 'main/index.html', context);

def login(request):
	if request.user.is_authenticated:
		return HttpResponseRedirect('/main/')
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')
	user = auth.authenticate(username=username, password=password)
	if user is not None and user.is_activate:
		auth.login(request, user)
		return HttpResponseRedirect('/main/')
	else :
		return render(request, 'login.html', locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/main/')
















