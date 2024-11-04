from django.db import models
from datetime import date
from myapp.exceptions import InvalidEndDateException
from .member import Member
from .item import Item


class Contract(models.Model):
    id = models.CharField(max_length=50, primary_key=True)  # Consider UUIDField if unique IDs are important
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name="contracts")
    borrower = models.ForeignKey(Member, on_delete=models.CASCADE, related_name="borrowed_contracts")
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)

    def clean(self):
        """Custom validation to ensure end_date is after start_date."""
        if self.end_date < self.start_date:
            raise InvalidEndDateException("End date cannot be before start date.")

    def conflicts_with(self, other_contract):
        """Check for overlapping date ranges with another contract for the same item."""
        if self.item != other_contract.item:
            return False
        if not self.active or not other_contract.active:
            return False
        return not (self.end_date < other_contract.start_date or self.start_date > other_contract.end_date)

    def __str__(self):
        return (f"Contract(Item: {self.item.name}, Borrower: {self.borrower.name}, "
                f"Start Date: {self.start_date}, End Date: {self.end_date}, Active: {self.active})")
