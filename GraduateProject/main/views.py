from django.shortcuts import render
from main.models import Img

from .score_mobilenet_input import assessPicture

# Create your views here.

def main(request):

	num_visits = request.session.get('num_visits',0)
	request.session['num_visits'] = num_visits + 1
	isUploadImg = False
	img = None
	if request.method == 'POST':
		img = Img(img_url = request.FILES.get('img'), computerScore=3)
		img.save()
		isUploadImg = True
		img.computerScore = assessPicture(str(img.img_url))
		img.save()

	imgs = Img.objects.all().order_by('-computerScore')
	currentImg = img
	context = {
		'imgs' : imgs,
		'isUploadImg' : isUploadImg,
		'currentImg' : currentImg,
		'num_visits' : num_visits,
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
















