from django.contrib import admin
from king.models import ProductID, ProductPage, Customers, UserProfileInfo

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('p_title',)}

admin.site.register(ProductID)
admin.site.register(ProductPage, ProductAdmin)
admin.site.register(Customers)
admin.site.register(UserProfileInfo)
# Register your models here.
