# Generated by Django 3.2.8 on 2021-10-31 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('', 'Please Select'), ('MF', 'Meat and Fish'), ('VEG', 'Vegetables')], default='', max_length=5),
        ),
    ]