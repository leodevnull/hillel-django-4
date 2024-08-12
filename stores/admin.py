from django.contrib import admin

from stores.models import Store, Inventory


class InventoryInline(admin.TabularInline):
    model = Inventory
    extra = 0

    fields = ('product', 'quantity')


@admin.register(Store)
class StoreAdmin(admin.ModelAdmin):
    inlines = [InventoryInline]

    list_display = ('name', 'address')
