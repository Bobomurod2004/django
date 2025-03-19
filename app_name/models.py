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

class Company(models.Model):
    income = models.CharField("Yillik darmodni kiritish",max_length=255)
    warehouse = models.CharField("Omborxoniani metr kv",max_length=255)
    exhibition_hall = models.CharField("Ko'rgazma zali maydoni",max_length=255)
    installed_equipment = models.CharField("O'rnatilgan uskunalar soni",max_length=255)
    region = models.CharField("Viloyatlar",max_length=255)
    years = models.DateTimeField('Yillar')
    text = models.TextField('Erishilgan yutuqlar matni')
    name = models.CharField("Erishgan yutuqlar texti ",max_length=255)
    iconka = models.ImageField()
    class Meta:
        verbose_name = "Kampaniya"
        verbose_name_plural = "Kampaniya"

class Achievements(models.Model):
    short_text = models.CharField("Qisqa nomlanishi",max_length=255)
    text = models.TextField("Asosiy textlari",)
    image = models.ImageField("Yutuqlar rasmlari",)
    achievement_name = models.CharField(max_length=255)
    image_name = models.ImageField("Yutuqlar nomi")
    partner_image = models.ImageField("Hamkorlar rasmlari")
    class Meta:
        verbose_name = "Yutuqlar"
        verbose_name_plural = "Yutuqlar"

class The_team(models.Model):
    short_text = models.CharField("Qisq nomlash",max_length=255)
    text = models.TextField("Uzun textlar yozish",)
    image = models.ImageField("Rasmlarni kirtinsh",)
    full_name = models.CharField("To'liq ism familiyasi",max_length=255)
    role = models.CharField("Lavozimi",max_length=255)
    employee_image = models.ImageField("Xodimlarning rasmlari",)
    class Meta:
        verbose_name = "Jamoa a'zosi"
        verbose_name_plural = "Jamoa a'zolari"

class Galereya(models.Model):
    name = models.CharField("Rasm nomi",max_length=255)
    image = models.ImageField("Rasmlar")
    url = models.URLField("Video urli")
    class Meta:
        verbose_name = "Galeriya"
