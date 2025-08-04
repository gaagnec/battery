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
        
        # Фильтрация по статусу
        status_filter = request.GET.get("status", "")
        if status_filter:
            agreements = agreements.filter(status=status_filter)
            
        # Получаем все соглашения и рассчитываем дни аренды
        agreements_data = []
        for agreement in agreements:
            end = agreement.end_date or None
            duration = (end or date.today()) - agreement.start_date
            agreements_data.append({
                "id": agreement.id,  # Сохраняем ID для возможных действий
                "client_name": agreement.client.name,
                "start_date": agreement.start_date,
                "end_date": agreement.end_date,
                "days": duration.days,
                "status": agreement.status,
            })
        
        # Сортировка
        order_param = request.GET.get("o", "start_date")
        # Проверяем, если поле начинается с "-", значит сортировка в обратном порядке
        reverse_order = order_param.startswith("-")
        order = order_param[1:] if reverse_order else order_param  # Убираем "-" из имени поля
        
        # Обработка сортировки по дням аренды (которая не может быть выполнена на уровне БД)
        if order == "days":
            agreements_data = sorted(agreements_data, key=lambda x: x["days"], reverse=reverse_order)
        elif order == "client_name":
            agreements_data = sorted(agreements_data, key=lambda x: x["client_name"], reverse=reverse_order)
        elif order == "end_date":
            # Сортировка с учетом None значений
            agreements_data = sorted(agreements_data, 
                                    key=lambda x: (x["end_date"] is None, x["end_date"]), 
                                    reverse=reverse_order)
        elif order == "status":
            agreements_data = sorted(agreements_data, key=lambda x: x["status"], reverse=reverse_order)
        else:
            # По умолчанию сортируем по дате начала
            agreements_data = sorted(agreements_data, key=lambda x: x["start_date"], reverse=reverse_order)
        
        # Пагинация уже отсортированных данных
        paginator = Paginator(agreements_data, 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

        context = dict(
            self.each_context(request),
            title="Список договоров аренды",
            agreements=page_obj,
            paginator=paginator,
            page_obj=page_obj,
            status_filter=status_filter,
            order=order,
            order_param=order_param,
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
