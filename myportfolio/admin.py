from django.contrib import admin
from .models import Skill, PersonalDetail, WorkExperience, Project, Reference, Education

# Register your models here.
admin.site.register(PersonalDetail)
admin.site.register(Skill)
admin.site.register(WorkExperience)
admin.site.register(Project)
admin.site.register(Reference)
admin.site.register(Education)
