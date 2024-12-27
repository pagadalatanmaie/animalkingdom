from django.contrib import admin
from .models import *
# Register your models here.


# for cat model===============
class catAdmin(admin.ModelAdmin):
    list_display = ['image','name','description','sound',]
admin.site.register(cat,catAdmin)


# for bird model===============
class birdAdmin(admin.ModelAdmin):
    list_display = ['image','name','description','sound',]
admin.site.register(bird,birdAdmin)

# for snake model===============
class snakeAdmin(admin.ModelAdmin):
    list_display = ['image','name','description','sound',]
admin.site.register(snake,snakeAdmin)


# ===
class bearAdmin(admin.ModelAdmin):
    list_display = ['img_b1','name','description','sound',]
admin.site.register(bear,bearAdmin)

class chickenAdmin(admin.ModelAdmin):
    list_display = ['image','name','description','sound',]
admin.site.register(chicken,chickenAdmin)

class turtleAdmin(admin.ModelAdmin):
    list_display = ['image','name','description','sound',]
admin.site.register(turtle,turtleAdmin)