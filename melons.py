"""Classes for melon orders."""

class AbstractMelonOrder:
    order_type = None
    tax = 0


    def __init__(self, species, qty):

        self.species = species
        self.qty = qty
        self.shipped = False
       
        


class DomesticMelonOrder(AbstractMelonOrder):
    """A melon order within the USA."""

    order_type = None
    tax = 0

    def __init__(self, species, qty):
        """Initialize melon order attributes."""
        self.qty = qty
        self.species = species

        

    def get_total(self):
        """Calculate price, including tax."""
     
        base_price = 5
        total = (1 + self.tax) * self.qty * base_price



        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""

    order_type = None
    tax = 0

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes."""

        self.country_code = country_code
        self.order_type = "international"
        self.tax = 0.17

    def get_total(self):
        """Calculate price, including tax."""
        
        total = (1 + self.tax) * self.qty * base_price

        return total

    def mark_shipped(self):
        """Record the fact than an order has been shipped."""

        self.shipped = True

    def get_country_code(self):
        """Return the country code."""

        return self.country_code



