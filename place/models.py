from django.db import models
import uuid
from book.models import Book
from django.db.models.signals import post_save, post_delete
from  django.dispatch import receiver
# Create your models here.

class Sede(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=250)

    def __str__(self):
        return self.name_address

    @property
    def name_address(self) -> str:
        return f"{self.name} || {self.address}"


class Rack(models.Model):
    number = models.IntegerField(null=False)
    uuid = models.UUIDField(default=uuid.uuid4())
    sede = models.ForeignKey(Sede, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def __str__(self):
        return  f"{self.sede.name} | {self.number}"

    @property
    def name_uuid(self) -> dict:
        return {
            "number": self.number,
            "id": self.uuid
        }


class RackItem(models.Model):
    rack = models.ForeignKey(Rack, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
 

    def __str__(self):
        return f"{self.id} | {self.book.isbn} | {self.book.author.name} "

@receiver(post_save, sender=RackItem)
def update_status_rack(sender, instance, created, **kwargs):
    if created:
        rack_item = instance
        rack_id = rack_item.rack.id
        rack = Rack.objects.get(pk=rack_id)
        print(instance)
        print(rack)
        rack.status = False
        rack.save()

@receiver(post_delete, sender=RackItem)
def update_status_rack(sender, instance, **kwargs):
    rack_item = instance
    rack_id = rack_item.rack.id
    rack = Rack.objects.get(pk=rack_id)
    rack.status = True
    rack.save()