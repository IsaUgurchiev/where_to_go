# Generated by Django 3.2.13 on 2022-05-22 14:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_placeimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='place_id',
            field=models.CharField(max_length=200, null=True, verbose_name='Идентификатор места'),
        ),
        migrations.AlterField(
            model_name='placeimage',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='places.place', verbose_name='Место'),
        ),
    ]
