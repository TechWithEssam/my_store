from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Profile, Subscribe
from .forms import AdminCreate
# Register your models here.


admin.site.register(Subscribe)
class CustomAdmin(UserAdmin) :
    model       = User
    add_form    = AdminCreate
    fieldsets   = (
        *UserAdmin.fieldsets,
        (
            "Additonal Info",
            {
                'fields':(
                    "date_of_birth",
                    "gender"
                )
            }
        )
    )
admin.site.register(User, CustomAdmin)

admin.site.register(Profile)