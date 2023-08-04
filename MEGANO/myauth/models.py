from django.contrib.auth.models import User
from django.db import models


def avatar_directory_path(instance: "Avatar", file_name: str) -> str:
    return "app_users/avatar_{pk}/avatars/{filename}".format(
        pk=instance.pk,
        filename=file_name,
    )


# Create your models here.
class Avatar(models.Model):
    """Модель для хранения аватара пользователя"""

    src = models.ImageField(
        upload_to=avatar_directory_path,
        verbose_name="Ссылка",
    )
    alt = models.CharField(max_length=128, verbose_name="Описание")

    class Meta:
        verbose_name = "Аватар"
        verbose_name_plural = "Аватары"


class Profile(models.Model):
    """Модель профиля пользователя"""
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile'
    )
    fullName = models.CharField(max_length=128, verbose_name="Полное имя")
    phone = models.PositiveIntegerField(
        blank=True, null=True, unique=True, verbose_name="Номер телефона"
    )
    email = models.EmailField(max_length=230, blank=True, null=True)
    balance = models.DecimalField(
        decimal_places=2,
        max_digits=10,
        default=0,
        verbose_name="Баланс",
    )
    avatar = models.ForeignKey(
        Avatar,
        on_delete=models.CASCADE,
        related_name="profile",
        verbose_name="Аватар",
        null=True,
        blank=True
    )

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"