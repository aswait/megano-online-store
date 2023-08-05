from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

from myauth.models import Profile


def image_directory_path(instance: "Image", file_name: str) -> str:
    return "app_users/images/{filename}".format(
        pk=instance.pk,
        filename=file_name,
    )


class Specification(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    value = models.CharField(max_length=100, verbose_name="Значение")

    class Meta:
        verbose_name = "Спецификация"
        verbose_name_plural = "Спецификации"


class Tag(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")

    class Meta:
        verbose_name = "Тэг"
        verbose_name_plural = "Тэги"


class Image(models.Model):
    src = models.ImageField(
       upload_to=image_directory_path,
       verbose_name="Ссылка",
    )

    alt = models.CharField(
        max_length=128,
        verbose_name="Описание"
    )

    class Meta:
        verbose_name = "Изображение"
        verbose_name_plural = "Изображения"


class Subcategory(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Изображение",
    )
    archived = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"


class Category(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")

    image = models.ForeignKey(
        Image,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Изображение",
    )

    subcategories = models.ManyToManyField(Subcategory, verbose_name="Подкатегория")
    archived = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Review(models.Model):
    author = models.CharField(max_length=100, verbose_name="Автор")
    text = models.TextField(max_length=400, null=True, blank=True, verbose_name="Текст")
    email = models.EmailField(verbose_name="Почта")
    rate = models.IntegerField(
        default=1,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1)
        ],
        verbose_name="Рейтинг"
    )
    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class Product(models.Model):
    category = models.OneToOneField(
        Category,
        on_delete=models.CASCADE,
        verbose_name="Категория"
    )

    price = models.DecimalField(
        blank=True,
        null=True,
        verbose_name="Цена",
        decimal_places=2,
        max_digits=8
    )

    count = models.PositiveIntegerField(
        blank=True,
        null=True,
        verbose_name="Количество"
    )

    title = models.TextField(max_length=100, verbose_name="Название")
    description = models.CharField(
        max_length=100,
        verbose_name="Описание",
        blank=True,
        null=True
    )
    fullDescription = models.CharField(
        max_length=400,
        verbose_name="Полное описание",
        blank=True,
        null=True,
    )

    date = models.DateTimeField(auto_now_add=True, verbose_name="Дата")
    freeDelivery = models.BooleanField(verbose_name="Бесплатная доставка")
    archived = models.BooleanField(default=False)

    rating = models.DecimalField(
        blank=True,
        null=True,
        verbose_name="Рейтинг",
        decimal_places=1,
        max_digits=8,
    )

    tags = models.ManyToManyField(Tag, verbose_name="Метки")
    specifications = models.ManyToManyField(Specification, verbose_name="Спецификации")
    reviews = models.ManyToManyField(Review, verbose_name="Отзывы", null=True, blank=True)
    images = models.ManyToManyField(Image, verbose_name="Изображение", null=True, blank=True)

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
