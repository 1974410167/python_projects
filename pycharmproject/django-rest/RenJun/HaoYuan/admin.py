from django.contrib import admin

# Register your models here.

from .models import Student

class StudentAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "address",
    ]
    # 按照"name"字段排序
    ordering = ["name"]
    fields = [
        "name",
        "address",
    ]
    actions_on_top = False
    actions_on_bottom = True
    # actions_selection_counter = False

admin.site.register(Student,StudentAdmin)