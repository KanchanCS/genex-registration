# Generated by Django 4.1.5 on 2023-01-22 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="country",
            field=models.CharField(
                blank=True, choices=[("In", "India"), ("En", "England")], max_length=100
            ),
        ),
    ]
