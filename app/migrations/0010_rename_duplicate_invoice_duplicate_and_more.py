# Generated by Django 4.1.4 on 2023-05-31 09:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_invoice_item_name_alter_invoice_printing_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='invoice',
            old_name='duplicate',
            new_name='Duplicate',
        ),
        migrations.RenameField(
            model_name='invoice',
            old_name='empty',
            new_name='Triplicate',
        ),
    ]