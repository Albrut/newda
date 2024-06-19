from django.contrib import admin
from .models import Sweet, Order

@admin.register(Sweet)
class SweetAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name',)
    list_filter = ('price',)

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('sweet', 'quantity', 'address', 'ordered_at', 'status', 'user')
    search_fields = ('sweet__name', 'address', 'user__username')
    list_filter = ('status', 'ordered_at', 'user')
    raw_id_fields = ('sweet', 'user')
    date_hierarchy = 'ordered_at'
