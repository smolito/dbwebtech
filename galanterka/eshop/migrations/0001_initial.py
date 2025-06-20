# Generated by Django 5.2.1 on 2025-06-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produkt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazev', models.CharField(max_length=100)),
                ('popis', models.TextField(blank=True)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=8)),
                ('datum_pridani', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
