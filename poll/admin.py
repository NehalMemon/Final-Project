from django.contrib import admin
from poll.models import poll

class adminpoll(admin.ModelAdmin):
    list_display=('name','id','Homepage_des','Overall_des','Exterior_des','Interior_des','main_img','Exterior_img1','Exterior_img2','interior_img1','interior_img2',)
    
    
admin.site.register(poll,adminpoll)    

