# Generated by Django 4.2.4 on 2023-08-31 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lotusedt', '0006_remove_course_instructor_course_instructors'),
    ]

    operations = [
        migrations.CreateModel(
            name='Enrollment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('enrollment_date', models.DateField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotusedt.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lotusedt.studentmodel')),
            ],
        ),
    ]
