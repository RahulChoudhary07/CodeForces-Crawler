# Generated by Django 2.0.7 on 2020-05-30 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200530_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='chatroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Chatroom'),
        ),
    ]
