import re
from django.db import models
from myapp.exceptions import (
    NegativeCreditsException,
    InvalidEmailFormatException,
    InvalidPhoneNumberException,
    NegativeAmountException,
)


class Member(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, unique=True)
    credits = models.IntegerField(default=0)

    def add_credits(self, amount: int):
        """Add credits to the member's account."""
        if amount < 0:
            raise NegativeAmountException("Cannot add a negative amount of credits.")
        self.credits += amount
        self.save()  # Persist the change to the database

    def deduct_credits(self, amount: int):
        """Deduct credits from the member's account."""
        if amount < 0:
            raise NegativeAmountException("Cannot deduct a negative amount of credits.")
        if self.credits - amount < 0:
            raise NegativeCreditsException("Credits cannot be negative after deduction.")
        self.credits -= amount
        self.save()  # Persist the change to the database

    def __str__(self):
        return f"{self.name} ({self.email}) - Credits: {self.credits}"
