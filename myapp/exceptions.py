# models/exceptions.py

class EmailExistsException(Exception):
    """Raised when the email already exists in the repository."""
    pass

class PhoneExistsException(Exception):
    """Raised when the phone number already exists in the repository."""
    pass

class NegativeCreditsException(Exception):
    """Raised when credits are negative."""
    pass

class NegativeAmountException(Exception):
    """Raised when an amount is negative."""
    pass

class NegativeCostException(Exception):
    """Raised when the cost of an item is negative."""
    pass

class InvalidEndDateException(Exception):
    """Raised when the end date is before the start date."""
    pass

class IdExistsException(Exception):
    """Raised when the ID already exists in the repository."""
    pass

class InvalidEmailFormatException(Exception):
    """Raised when the email format is invalid."""
    pass

class InvalidPhoneNumberException(Exception):
    """Raised when the phone number format is invalid."""
    pass

class ItemNotFoundException(Exception):
    """Raised when an item is not found in the repository."""
    pass

class BorrowerNotFoundException(Exception):
    """Raised when a borrower is not found in the repository."""
    pass

class ContractConflictException(Exception):
    """Raised when there's a conflicting contract."""
    pass

class InsufficientCreditsException(Exception):
    """Raised when a member does not have enough credits."""
    pass

class InvalidDateFormatException(Exception):
    """Raised when the date format is invalid."""
    pass

class ContractNotFoundException(Exception):
    """Raised when a contract is not found in the repository."""
    pass

class MemberNotFoundException(Exception):
    """Raised when a member is not found in the repository."""
    pass

class OwnerNotFoundException(Exception):
    """Raised when an owner is not found in the repository."""
    pass
