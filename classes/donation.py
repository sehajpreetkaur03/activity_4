class Donation:
    """A class used to represent a donation record."""

    def __init__(self, donor_name: str, amount: float, message: str = ""):
        """
        Initialize a Donation instance.

        :param donor_name: Name of the person donating
        :param amount: Donation amount
        :param message: Optional thank-you message
        """
        self.donor_name = donor_name
        self.amount = amount
        self.message = message

    def display_info(self):
        """Return a short summary of the donation."""
        return f"{self.donor_name} donated ${self.amount:.2f}. {self.message}"
