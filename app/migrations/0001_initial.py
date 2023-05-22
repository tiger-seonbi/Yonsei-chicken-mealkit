# Generated by Django 4.2.1 on 2023-05-21 12:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=50)),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='uers_department', to='app.department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='CountChicken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('department', models.ForeignKey(db_column='department', on_delete=django.db.models.deletion.CASCADE, related_name='Department_chicken', to='app.person')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='users_chicken', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
