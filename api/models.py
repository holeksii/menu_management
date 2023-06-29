from django.db import models
from django.core.validators import MinValueValidator, RegexValidator


class Restaurant(models.Model):
    name = models.CharField(max_length=100)


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    date = models.DateField()


class Ingredient(models.Model):
    MEASUREMENT_CHOICES = [
        ("grams", "Grams"),
        ("kilograms", "Kilograms"),
        ("liters", "Liters"),
        ("milliliters", "Milliliters"),
        ("ounces", "Ounces"),
        ("pounds", "Pounds"),
        ("teaspoons", "Teaspoons"),
        ("tablespoons", "Tablespoons"),
        ("cups", "Cups"),
    ]

    name = models.CharField(max_length=100, blank=False)
    measurement = models.CharField(max_length=15, choices=MEASUREMENT_CHOICES)
    menu_item = models.ForeignKey("MenuItem", on_delete=models.CASCADE)


class MenuItem(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True, blank=False)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0.0)]
    )
    total_weight = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[MinValueValidator(0.0)]
    )
    description = models.TextField(
        validators=[
            RegexValidator(
                r"^[a-zA-Z]{10,4000}$",
                message="Description must be between 10 and 4000 characters long",
            ),
        ]
    )


class Employee(models.Model):
    first_name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                r"^[a-zA-Z]{2,100}$",
                message="First name must be between 2 and 100 characters long"
                " and contain no numbers",
            )
        ],
    )
    last_name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                r"^[a-zA-Z]{2,100}$",
                message="Last name must be between 2 and 100 characters long"
                " and contain no numbers",
            )
        ],
    )


class Vote(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
