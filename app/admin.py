from django.contrib import admin
from .models import Customers,Application,Partner,Product,ProductImage,ProductCharacteristic,Category



admin.site.register(Customers)
admin.site.register(Category)
admin.site.register(ProductCharacteristic)
admin.site.register(Application)
admin.site.register(Product)
admin.site.register(Partner)
admin.site.register(ProductImage)

