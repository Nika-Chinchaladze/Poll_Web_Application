from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=500)
    answer_1 = models.CharField(max_length=200)
    answer_2 = models.CharField(max_length=200)
    answer_3 = models.CharField(max_length=200)
    answer_4 = models.CharField(max_length=200)
    slug_name = models.CharField(max_length=200, null=True, blank=True)
    slug_title = models.SlugField(max_length=600, null=True, blank=True)

    def __str__(self):
        return f"{self.title} {self.answer_1} {self.answer_2} {self.answer_3} {self.answer_4} {self.slug_name}"

    def save(self, *args, **kwargs):
        self.slug_title = slugify(self.title)
        super().save(*args, **kwargs)


class Survay(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    answer = models.CharField(max_length=200)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.question} {self.answer} {self.user}"


class Personal(models.Model):
    work = models.CharField(max_length=150)
    university = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    love = models.CharField(max_length=150)
    phone = models.CharField(max_length=150)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.work} {self.university} {self.city} {self.country} {self.love} {self.phone} {self.user}"


class UserImage(models.Model):
    image = models.ImageField(upload_to="images")
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, null=True, blank=True, related_name="images")

    def __str__(self):
        return f"{self.image} {self.user}"


class ChartModel(models.Model):
    current_type = models.CharField(max_length=100, null=True, blank=True)


class MessageModel(models.Model):
    user_name = models.CharField(max_length=100, null=True, blank=True)
