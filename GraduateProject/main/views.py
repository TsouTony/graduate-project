from django.shortcuts import render
from main.models import Img, Comment
from django.contrib.auth.decorators import login_required
from .score_mobilenet_input import assessPicture

# Create your views here.


def main(request):
	num_visits = request.session.get('num_visits',0)
	request.session['num_visits'] = num_visits + 1
	isUploadImg = False
	img = None

	print(request.user.username)
	if request.method == 'POST' and request.content_type == 'multipart/form-data':
		print(request.content_type)
		img = Img(img_url = request.FILES.get('img'), creator = request.user)
		img.save()
		isUploadImg = True
		img.computerScore = assessPicture(str(img.img_url))
		img.save()

	if request.method == 'POST' and request.content_type == 'application/x-www-form-urlencoded':
		comment = Comment(content = request.POST.get('comment_field'), creator = request.user)
		comment.save()

	comments = Comment.objects.all().order_by('create_time')
	imgs = Img.objects.all().order_by('-computerScore')
	context = {
		'imgs' : imgs,
		'isUploadImg' : isUploadImg,
		'currentImg' : img,
		'num_visits' : num_visits,
		'comments' : comments,
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
















