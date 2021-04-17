from django.contrib import admin
from .models import Education, WorkExperience, ProfessionalSkills, Interest


# Register your models here.
admin.site.register(Education)
admin.site.register(WorkExperience)
admin.site.register(ProfessionalSkills)
admin.site.register(Interest)