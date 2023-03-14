from django.contrib import admin

from .models import Question, Survay, Personal, UserImage, ChartModel, MessageModel
# Register your models here.


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ("title", "answer_1", "answer_2", "answer_3",
                    "answer_4", "slug_name", "slug_title",)
    prepopulated_fields = {"slug_title": ("title",)}


class SurvaysAdmin(admin.ModelAdmin):
    list_display = ("question", "answer", "user",)


class PersonalsAdmin(admin.ModelAdmin):
    list_display = ("work", "university", "city",
                    "country", "love", "phone", "user",)


class UserImagesAdmin(admin.ModelAdmin):
    list_display = ("image", "user",)


class ChartAdmin(admin.ModelAdmin):
    list_display = ("current_type",)


class MessageAdmin(admin.ModelAdmin):
    list_display = ("user_name",)


admin.site.register(Question, QuestionsAdmin)
admin.site.register(Survay, SurvaysAdmin)
admin.site.register(Personal, PersonalsAdmin)
admin.site.register(UserImage, UserImagesAdmin)
admin.site.register(ChartModel, ChartAdmin)
admin.site.register(MessageModel, MessageAdmin)
