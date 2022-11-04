# Generated by Django 4.1.2 on 2022-10-17 06:06
import sys

from django.db import migrations

import os
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('shop', '0002_alter_baseitems_created_at_and_more'),
    ]

    def create_items(apps, schema_editor):
        from core.utils import csv_to_json_data_migration
        from shop import models
        files = (
            "Ammo", "Weapons",
            "Droids", "Devices", "Engines", "Resources", "Ships", "ItemsType")
        bs = csv_to_json_data_migration(os.path.join('apps', 'shop', 'migrations', 'data', 'BaseItems.csv'))
        for file in files:
            p = os.path.join('apps', 'shop', 'migrations', 'data', file + ".csv")
            data = csv_to_json_data_migration(p)
            for data_ in data:
                if file != "ItemsType":
                    n = int(data_.pop('baseitems_ptr_id')) - 1
                    data_.update(bs[n])
                    if file == "Weapons":
                        if data_['weapon_ammo_id']:
                            data_['weapon_ammo_id'] = models.Ammo.objects.values_list('id', flat=True).get(class_number=data_['weapon_ammo_id'])
                        else:
                            data_['weapon_ammo_id'] = None
                    elif file == "Droids":
                        if data_['droid_weapon_id']:
                            data_['droid_weapon_id'] = models.Weapons.objects.values_list('id', flat=True).get(class_number=data_['droid_weapon_id'])
                        else:
                            data_['droid_weapon_id'] = None

                model = getattr(models, file)
                model(**data_).save()

    operations = [
        migrations.RunPython(create_items),
    ]
