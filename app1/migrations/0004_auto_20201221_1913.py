# Generated by Django 3.1.4 on 2020-12-22 01:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20201221_1707'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quote',
            name='users',
        ),
        migrations.AddField(
            model_name='quote',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='quotes', to='app1.user'),
        ),
    ]
