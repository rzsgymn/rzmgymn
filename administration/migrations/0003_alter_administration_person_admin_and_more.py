# Generated by Django 4.1 on 2022-08-20 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0018_alter_person_photo'),
        ('administration', '0002_alter_typeofadministrativeposition_type_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administration',
            name='person_admin',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff.person', verbose_name='працівник'),
        ),
        migrations.AlterField(
            model_name='administration',
            name='position',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='administration.typeofadministrativeposition', verbose_name='посада'),
        ),
    ]
