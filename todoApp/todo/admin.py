from django.contrib import admin
from .models import Cases, Todo, Stories, Counsellors, Cases, Officers
# Register your models here.

admin.site.register(Todo)
admin.site.register(Stories)
admin.site.register(Counsellors)
admin.site.register(Cases)
admin.site.register(Officers)
