from django.db import models

# python .\manage.py makemigrations
# python manage.py sqlmigrate produkty 0001
# python manage.py migrate

class Produkt(models.Model):
    nazev = models.CharField(max_length=100)
    popis = models.TextField(blank=True)
    cena = models.DecimalField(max_digits=8, decimal_places=2)
    datum_pridani = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nazev
