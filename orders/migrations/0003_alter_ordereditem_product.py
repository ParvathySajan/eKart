# Generated by Django 4.2.1 on 2024-06-07 15:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('orders', '0002_order_total_price_alter_order_order_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordereditem',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='addeditems', to='products.product'),
        ),
    ]