from django.contrib import admin
# Register your models here.
from .models import Project
# admin.site.register(Car)

#####################################################

from . import models

# class CarAdmin(admin.ModelAdmin):   #=> 3shan tzhr f admin panel
#     list_display=[ 'name','description','price' , 'color']
#     list_display_links =['name' , 'price'] #=> link 3shan a2dr ad5ol 3leha
#     list_editable =['color'] #> a2dr a3dl feha mn bra w mynf3sh tkon displaylink
#     search_fields =['name' , 'price']
#     list_filter = ["price" , 'color']
#     # fields=['name' , 'description'] #=> b3d ma bd5ol 3leha 3shan a3dl details
# admin.site.register(models.Car , CarAdmin)
# admin.site.register(models.Employee)


class CarAdmin(admin.ModelAdmin):   #=> 3shan tzhr f admin panel
    list_display=[ 'name','description','category' , 'current_situation']
    # list_display_links =['name' , 'price'] #=> link 3shan a2dr ad5ol 3leha
    # list_editable =['color'] #> a2dr a3dl feha mn bra w mynf3sh tkon displaylink
    # search_fields =['name' , 'price']
    # list_filter = ["price" , 'color']
    # fields=['name' , 'description'] #=> b3d ma bd5ol 3leha 3shan a3dl details
admin.site.register(models.Project , CarAdmin)
# admin.site.register(models.Employee)