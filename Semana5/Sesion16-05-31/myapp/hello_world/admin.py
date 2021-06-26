from django.contrib import admin
from hello_world.models import Grettings

# Register your models here.

class GreetingAdmin(admin.ModelAdmin):
    model = Grettings

admin.site.register(Grettings, GreetingAdmin)
