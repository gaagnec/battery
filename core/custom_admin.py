from django.contrib import admin
from django.urls import path
from django.template.response import TemplateResponse
from django.core.paginator import Paginator
from datetime import date

from .models import (
    Client, BatteryType, Battery,
    RentalAgreement, RentalItem, Payment, BatteryMovement
)


class CustomAdminSite(admin.AdminSite):
    site_header = "BatteryRental Admin"
    site_title = "BatteryRental"
    index_title = "Администрирование"

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path("batteries/", self.admin_view(self.battery_view), name="battery_list"),
            path("rentalagreements/", self.admin_view(self.rental_agreements_view), name="rental_agreement_list"),
        ]
        return custom_urls + urls

    def battery_view(self, request):
        batteries = Battery.objects.all()
        context = dict(
            self.each_context(request),
            title="Список батарей",
            batteries=batteries,
        )
        return TemplateResponse(request, "admin/batteries_list.html", context)

    def rental_agreements_view(self, request):
        agreements = RentalAgreement.objects.select_related("client").all()

        paginator = Paginator(agreements, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        # Обогащаем данные для шаблона
        agreements_data = []
        for agreement in page_obj:
            end = agreement.end_date or None
            duration = (end or date.today()) - agreement.start_date
            agreements_data.append({
                "client_name": agreement.client.name,
                "start_date": agreement.start_date,
                "end_date": agreement.end_date,
                "days": duration.days,
                "status": agreement.status,
            })

        context = dict(
            self.each_context(request),
            title="Список договоров аренды",
            agreements=agreements_data,
            paginator=paginator,
            page_obj=page_obj,
        )
        return TemplateResponse(request, "admin/rental_agreements_list.html", context)
    
    


# создаем экземпляр
custom_admin_site = CustomAdminSite(name="custom_admin")

# Регистрируем модели в кастомной админке:
custom_admin_site.register(Client)
custom_admin_site.register(BatteryType)
custom_admin_site.register(Battery)
custom_admin_site.register(RentalAgreement)
custom_admin_site.register(RentalItem)
custom_admin_site.register(Payment)
custom_admin_site.register(BatteryMovement)
