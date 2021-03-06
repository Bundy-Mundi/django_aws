from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

@admin.register(models.User)
class UserAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
    (
        "Custom Fields",
      {
          "fields":("bio", "date_of_birth", "gender",)
      }
    ),
  )
