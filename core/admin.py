from django.contrib import admin
from django.core.paginator import Paginator
from django.utils.html import format_html
from django.urls import reverse, path
from django.shortcuts import render
from .models import Battery, RentalAgreement

from datetime import date


# Админ для батарей
@admin.register(Battery)
class BatteryAdmin(admin.ModelAdmin):
    list_display = ('serial_number', 'status', 'note', 'edit_link')
    search_fields = ('serial_number', 'note')
    list_filter = ('status',)
    ordering = ('serial_number',)

    def edit_link(self, obj):
        url = reverse('admin:core_battery_change', args=[obj.pk])
        return format_html('<a href="{}">Редактировать</a>', url)
    edit_link.short_description = 'Действия'


# Свойство для подсчета дней аренды — в models.py у RentalAgreement:
# @property
# def rental_days(self):
#     end = self.end_date or date.today()
#     return (end - self.start_date).days

# Кастомная админ-панель
class CustomAdminSite(admin.AdminSite):
    site_header = "BatteryRental Admin"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('batteries/', self.admin_view(self.battery_list), name='battery_list'),
            path('rentalagreements/', self.admin_view(self.rental_agreement_list), name='rental_agreement_list'),
        ]
        return custom_urls + urls

    def battery_list(self, request):
        qs = Battery.objects.all()
        search_query = request.GET.get('q', '')
        if search_query:
            qs = qs.filter(serial_number__icontains=search_query)

        status_filter = request.GET.get('status', '')
        if status_filter:
            qs = qs.filter(status=status_filter)

        order = request.GET.get('o', 'serial_number')
        qs = qs.order_by(order)

        paginator = Paginator(qs, 10)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)

        context = dict(
            self.each_context(request),
            title="Список батарей",
            batteries=page_obj,
            search_query=search_query,
            status_filter=status_filter,
            order=order,
            paginator=paginator,
            page_obj=page_obj,
        )
        return render(request, 'admin/batteries_list.html', context)

    def rental_agreement_list(self, request):
        qs = RentalAgreement.objects.select_related('client').all()

        status_filter = request.GET.get('status', '')
        if status_filter:
            qs = qs.filter(status=status_filter)

        order = request.GET.get('o', 'start_date')
        qs = qs.order_by(order)

        paginator = Paginator(qs, 10)
        page_num = request.GET.get('page')
        page_obj = paginator.get_page(page_num)

        context = dict(
            self.each_context(request),
            title="Список договоров аренды",
            rental_agreements=page_obj,
            status_filter=status_filter,
            order=order,
            paginator=paginator,
            page_obj=page_obj,
        )
        return render(request, 'admin/rental_agreements_list.html', context)


admin_site = CustomAdminSite(name='custom_admin')
