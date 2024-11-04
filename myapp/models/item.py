import uuid
from django.db import models
from .member import Member
from myapp.exceptions import NegativeCostException


class Item(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    owner = models.ForeignKey(Member, on_delete=models.SET_NULL, null=True, related_name="items")
    name = models.CharField(max_length=100)
    cost = models.PositiveIntegerField()

    def set_cost(self, new_cost: int):
        """Set the item's cost, ensuring it is non-negative."""
        if new_cost < 0:
            raise NegativeCostException("Cost cannot be negative.")
        self.cost = new_cost
        self.save()  # Persist the change to the database

    def __str__(self):
        owner_name = self.owner.name if self.owner else "No Owner"
        return f"Item(Name: {self.name}, Cost: {self.cost}, Owner: {owner_name})"
