from django.contrib import admin

# Register your models here.
from .models import Question


# building the model for the admin site
class QuestionAdmin(admin.modelAdmin):
    fields = ['pub_date','question_text']

admin.site.register(Question,QuestionAdmin)
