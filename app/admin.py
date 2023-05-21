from django.contrib import admin
from .models import Person, CountChicken, Department
# Register your models here.
admin.site.register(Person)
admin.site.register(CountChicken)
admin.site.register(Department)
