# Generated by Django 3.1.1 on 2020-09-09 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sample_x509', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ca',
            name='common_name',
            field=models.CharField(
                blank=True, max_length=64, verbose_name='common name'
            ),
        ),
        migrations.AlterField(
            model_name='cert',
            name='common_name',
            field=models.CharField(
                blank=True, max_length=64, verbose_name='common name'
            ),
        ),
        migrations.AlterField(
            model_name='customcert',
            name='common_name',
            field=models.CharField(
                blank=True, max_length=64, verbose_name='common name'
            ),
        ),
    ]
