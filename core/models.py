from django.db import models
import uuid
from datetime import date

class Client(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    phone = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField()
    note = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'clients'
        managed = False

    def __str__(self):
        return self.name


class BatteryType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    capacity_ah = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'battery_types'
        managed = False

    def __str__(self):
        return self.name


class Battery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    serial_number = models.TextField(unique=True)
    type = models.ForeignKey(BatteryType, on_delete=models.DO_NOTHING, db_column='type_id')
    status = models.TextField(default='available')
    note = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'batteries'
        managed = False

    def __str__(self):
        return self.serial_number






class RentalAgreement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, db_column='client_id')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    status = models.TextField(default='active')
    weekly_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    note = models.TextField(null=True, blank=True)

    @property
    def rental_days(self):
        end = self.end_date or date.today()
        return (end - self.start_date).days

    class Meta:
        db_table = 'rental_agreements'
        managed = False

    def __str__(self):
        return f"{self.client.name} ({self.start_date})"


class RentalItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    rental = models.ForeignKey(RentalAgreement, on_delete=models.DO_NOTHING, db_column='rental_id')
    battery = models.ForeignKey(Battery, on_delete=models.DO_NOTHING, db_column='battery_id')
    rented_at = models.DateField()
    returned_at = models.DateField(null=True, blank=True)
    weekly_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'rental_items'
        managed = False


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    client = models.ForeignKey(Client, on_delete=models.DO_NOTHING, db_column='client_id')
    rental = models.ForeignKey(RentalAgreement, on_delete=models.DO_NOTHING, db_column='rental_id')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.TextField(default='rental')
    method = models.TextField(null=True, blank=True)
    paid_at = models.DateTimeField()
    note = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'payments'
        managed = False


class BatteryMovement(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    battery = models.ForeignKey(Battery, on_delete=models.DO_NOTHING, db_column='battery_id')
    status = models.TextField()
    timestamp = models.DateTimeField()
    note = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'battery_movements'
        managed = False
