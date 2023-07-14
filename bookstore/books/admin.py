from django.contrib import admin
from .models import Book,User
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'description','author','price']

admin.site.register(Book,BookAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['username', 'first_name','last_name','password','email']

admin.site.register(User,UserAdmin)