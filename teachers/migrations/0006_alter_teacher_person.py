# Generated by Django 4.1 on 2022-08-20 12:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0018_alter_person_photo'),
        ('teachers', '0005_alter_category_options_alter_lesson_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='staff.person', verbose_name='Працівник'),
        ),
    ]
