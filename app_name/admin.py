from django.contrib import admin
from .models import Customers,Application,Partner,Product,ProductImage,ProductCharacteristic,Category,The_team,Company,Galereya,Achievements



admin.site.register(Customers)
admin.site.register(Category)
admin.site.register(ProductCharacteristic)
admin.site.register(Application)
admin.site.register(Product)
admin.site.register(Partner)
admin.site.register(ProductImage)

@admin.register(The_team)
class TheTeamAdmin(admin.ModelAdmin):
    list_display = ("short_text","text",'full_name', 'role')  # Jadvalda ko‘rinadigan ustunlar
    search_fields = ('full_name', 'role')  # Qidiruv maydonchalari
    list_filter = ('role',)  # Yon tarafda filter bo‘lishi uchun

admin.site.register(Company)
admin.site.register(Galereya)
admin.site.register(Achievements)