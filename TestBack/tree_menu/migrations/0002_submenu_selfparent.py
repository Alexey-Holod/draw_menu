# Generated by Django 5.0.7 on 2024-07-26 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tree_menu', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='submenu',
            name='selfparent',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.SET_DEFAULT, to='tree_menu.submenu', verbose_name='Вложить в'),
        ),
    ]
