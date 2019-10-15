from django.contrib import admin
from .models import Img, User, Comment
# Register your models here.
class adminIMG(admin.ModelAdmin):
    list_display = ('img_url','create_time','computerScore','creator')
admin.site.register(Img,adminIMG)

# admin.site.register(User)

admin.site.register(Comment)