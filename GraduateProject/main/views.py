from django.shortcuts import render
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

# def uploadImg(request):

# 	if request.method == 'POST':
# 		img = Img(img_url = request.FILES.get('img'))
# 		img.save()
# 		isUploadImg = True

# 	imgs = Img.objects.all()
# 	currentImg =  img
# 	context = {
# 		'imgs' : imgs,
# 		'isUploadImg' : isUploadImg,
# 		'currentImg' : currentImg
# 	}

# 	return render(request, 'isUploadImg/index.html', context)
















