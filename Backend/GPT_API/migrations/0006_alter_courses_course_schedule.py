# Generated by Django 4.2.5 on 2023-12-05 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GPT_API', '0005_alter_courses_course_schedule'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='course_schedule',
            field=models.CharField(max_length=100000),
        ),
    ]
