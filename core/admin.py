from django.contrib import admin
from .models import Project, WorkExperience, Education, Skill, Hobby, Contact
# Register your models here.

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'image', 'url']
    search_fields = ['title', 'desription']
    list_filter = ['title']
    list_per_page = 10

@admin.register(WorkExperience)
class WorkExperienceAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'company', 'start_date', 'end_date']
    search_fields = ['title', 'description', 'company']
    list_filter = ['title', 'company']
    list_per_page = 10

@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'education_level', 'start_date', 'end_date']
    search_fields = ['title', 'description', 'education_level']
    list_filter = ['title', 'education_level']
    list_per_page = 10

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['title', 'level']
    search_fields = ['title', 'level']
    list_filter = ['title', 'level']
    list_per_page = 10

@admin.register(Hobby)
class HobbyAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']
    list_per_page = 10

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'subject', 'message']
    search_fields = ['email', 'subject', 'message']
    list_filter = ['email', 'subject']
    list_per_page = 10