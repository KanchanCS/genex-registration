# Generated by Django 4.1.5 on 2023-01-24 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0003_alter_account_country"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="account",
            name="username",
        ),
        migrations.AlterField(
            model_name="account",
            name="gender",
            field=models.CharField(
                choices=[("M", "Male"), ("F", "Female")], default="Mail", max_length=20
            ),
        ),
    ]
