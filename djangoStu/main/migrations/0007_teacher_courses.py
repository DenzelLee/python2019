# Generated by Django 2.0.4 on 2019-09-27 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_teacher_courses'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(related_name='course_teacher', to='main.Course'),
        ),
    ]