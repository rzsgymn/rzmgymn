# Generated by Django 4.1 on 2022-08-20 20:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0012_alter_teacher_person'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='mass',
            field=models.SmallIntegerField(default=0, help_text='ранг має бути унікальним для кожногї категорії', verbose_name='ранг'),
            preserve_default=False,
        ),
    ]
