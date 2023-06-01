# Generated by Django 4.1.4 on 2023-05-31 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_alter_invoice_gst_type_alter_invoice_item_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoice',
            name='item_name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='invoice',
            name='printing_type',
            field=models.CharField(choices=[('A4', 'A4'), ('A3', 'A3')], max_length=100),
        ),
    ]