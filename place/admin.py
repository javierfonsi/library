from django.contrib import admin
from .models import RackItem, Sede, Rack
#from .models import Rack
# Register your models here.

admin.site.register(Sede) 
admin.site.register(Rack) 
admin.site.register(RackItem) 