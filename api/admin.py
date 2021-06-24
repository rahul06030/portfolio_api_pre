from django.contrib import admin

# Register your models here.

from .models import Course, Education, Experience, Profile, Project, Skill

admin.site.register(Profile)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(Project)
admin.site.register(Course)
admin.site.register(Skill)