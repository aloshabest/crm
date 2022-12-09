from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    country = models.CharField(max_length=100, blank=True, verbose_name='Страна')
    address = models.CharField(max_length=200, blank=True, verbose_name='Адрес')
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='Номер')

    def __str__(self):
      return self.username


class Lead(models.Model):
    first_name = models.CharField(max_length=50, blank=True, verbose_name='Имя')
    last_name = models.CharField(max_length=50, blank=True, verbose_name='Фамилия')
    age = models.IntegerField(default=0, verbose_name='Возраст')
    phone_number = models.CharField(max_length=15, blank=True, verbose_name='Номер')
    active = models.BooleanField(default=False)
    profile_picture = models.ImageField(blank=True, null=True, verbose_name='Фото')
    category = models.ForeignKey("Category", null=True, blank=True, on_delete=models.SET_NULL, verbose_name='Статус')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    description = models.TextField(verbose_name='Описание')
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True, blank=True, related_name='leads')

    def __str__(self):
        return self.first_name

    @property
    def has_agent(self):
        return self.agent is not None


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='agent')

    def __str__(self):
        return self.user.username


class Category(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title