from django.contrib import admin
from .models import Sponsor, University, Student, SponsorIntroduction, SponsorsToTheStudent
# Register your models here.
admin.site.register(Sponsor)
admin.site.register(University)
admin.site.register(Student)
admin.site.register(SponsorIntroduction)
admin.site.register(SponsorsToTheStudent)