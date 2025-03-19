from django.db import models


class Customers(models.Model):
    full_name = models.CharField(max_length=255, null=True, blank=True)
    position = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField()
    description = models.CharField(max_length=255, null=True, blank=True)


class Partner(models.Model):
    image = models.ImageField(upload_to="")
    url = models.CharField(max_length=255, blank=True)
    order = models.IntegerField(default=0)


class Application(models.Model):

    class ApplicationChoices(models.TextChoices):
        main_page = ("main_page", "Main Page")
        service = ("service", "Service")
        get_tt = ("get_tt", "Get_tt")
        partner = ("partner", "Partner")
        order = ("order", "Order")

    full_name = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    product = models.CharField(max_length=255, blank=True)
    status = models.CharField(
        max_length=255,
        choices=ApplicationChoices.choices,
        default=ApplicationChoices.main_page
    )

class Product(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(
        "Category", related_name="products",
        on_delete=models.CASCADE,
        null=True
    )

class ProductImage(models.Model):
    image = models.ImageField()
    product =models.ForeignKey(
        Product, related_name="product_images", on_delete=models.CASCADE
    )

class ProductCharacteristic(models.Model):
    key = models.CharField(max_length=255)
    valur = models.CharField(max_length=255)
    oreder = models.IntegerField(default=0)
    product = models.ForeignKey(
        Product, related_name="prod_characters", on_delete=models.CASCADE
    )

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField()
    order = models.IntegerField(default=1)