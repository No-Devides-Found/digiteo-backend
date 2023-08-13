from django.contrib import admin
from .models import Program, Category, Contents, Quiz, Assignment, Tag, Program_Tag_Map, Program_User_Map

admin.site.register(Program)
admin.site.register(Category)
admin.site.register(Contents)
admin.site.register(Quiz)
admin.site.register(Assignment)
admin.site.register(Tag)
admin.site.register(Program_Tag_Map)
admin.site.register(Program_User_Map)