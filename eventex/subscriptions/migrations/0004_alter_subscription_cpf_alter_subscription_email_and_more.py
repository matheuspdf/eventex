# Generated by Django 5.0.3 on 2024-05-30 18:36

import eventex.subscriptions.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0003_alter_subscription_paid"),
    ]

    operations = [
        migrations.AlterField(
            model_name="subscription",
            name="cpf",
            field=models.CharField(
                max_length=11,
                validators=[eventex.subscriptions.validators.validate_cpf],
                verbose_name="CPF",
            ),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="email",
            field=models.EmailField(blank=True, max_length=254, verbose_name="e-mail"),
        ),
        migrations.AlterField(
            model_name="subscription",
            name="phone",
            field=models.CharField(blank=True, max_length=20, verbose_name="telefone"),
        ),
    ]
