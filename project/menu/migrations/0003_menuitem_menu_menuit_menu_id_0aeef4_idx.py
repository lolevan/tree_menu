# Generated by Django 5.0.7 on 2024-07-26 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_initial_data'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='menuitem',
            index=models.Index(fields=['menu', 'parent', 'order'], name='menu_menuit_menu_id_0aeef4_idx'),
        ),
    ]
