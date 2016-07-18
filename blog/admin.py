from django.contrib import admin
from blog.models import *

# Register your models here.
admin.site.register(Entries)
admin.site.register(Categories)
admin.site.register(TagModel)


