# Generated by Django 2.0.5 on 2022-03-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_encrypted_kycdata'),
    ]

    operations = [
        migrations.AddField(
            model_name='encrypted_kycdata',
            name='panencrypted_data',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='encrypted_kycdata',
            name='voterencrypted_data',
            field=models.CharField(default='', max_length=300),
            preserve_default=False,
        ),
    ]