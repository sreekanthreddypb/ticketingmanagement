# Generated by Django 4.0.3 on 2022-04-30 04:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_ticket'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.customer'),
        ),
    ]
