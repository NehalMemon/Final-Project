from django.contrib import admin
from poll.models import poll
from poll.models import Formdata

class adminpoll(admin.ModelAdmin):
    list_display=('name','id','Homepage_des','Overall_des','Exterior_des','Interior_des','main_img','Exterior_img1','Exterior_img2','interior_img1','interior_img2',)
    
    
admin.site.register(poll,adminpoll)    
class VoteAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'selected_id')

    def has_add_permission(self, request):
        # Disables the "Add" button for Vote model in the admin
        return False

# Register the Vote model with the custom admin class
admin.site.register(Formdata, VoteAdmin)

