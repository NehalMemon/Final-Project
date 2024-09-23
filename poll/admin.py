from django.contrib import admin
from poll.models import poll

class adminpoll(admin.ModelAdmin):
    list_display=('name','dis1','dis2','img1','img2',)
    
    
admin.site.register(poll,adminpoll)    

