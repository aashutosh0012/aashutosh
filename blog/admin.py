from django.contrib import admin

# Register your models here.
#Display Post Model in admin panel, Register Post class to admin
from .models import Post, Projects, visitor_ip
admin.site.register(Post)


#Register Projects Object model to Django Admin Page
from .models import Projects
admin.site.register(Projects)
admin.site.register(visitor_ip)


