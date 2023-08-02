from django.db import models

# Create your models here.
CATEGORY= (
    ('Stationary', 'Stationary'),
    ('Electronics', 'Electronics'),
    ('Food', 'Food'),
    ('Household Cleaning Products', 'Household Cleaning Products'),
    ('Health Drinks and suppliments', 'Health Drinks and suppliments'),
    ('Cosmetics', 'Cosmetics'),
    ('Soap and Detergents', 'Soap and Detergents'),

)

SUB_CATEGORY= (
    ('Dishwashing Soap', 'Dishwashing Soap'),
    ('Bathing Soap', 'Bathing Soap'),
    ('Hair Care Product', 'Hair Care Product'),
    ('Skin Care product', 'Skin Care Product'),
    ('Facewash', 'Facewash'),
    ('Clothes Detergent', 'Clothes Detergent'),
    ('Body Spray', 'Body Spray'),
    ('Shaving products', 'Shaving products'),
    
)


# class Product(models.Model):
#     name= models.CharField(max_length=100, null=True)
#     category= models.CharField(max_length=20, choices=CATEGORY, null=True)
#     qty= models.PositiveIntegerField(null=True)

    #   def __str__(self):
    #   return f'{self.name}--{self.quantity}'