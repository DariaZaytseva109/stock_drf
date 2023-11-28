# Generated by Django 4.2.6 on 2023-11-21 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stock_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='usergroup',
            options={'verbose_name': 'Тип пользователя', 'verbose_name_plural': 'Типы пользователя'},
        ),
        migrations.RemoveField(
            model_name='apiuser',
            name='usertype',
        ),
        migrations.AddField(
            model_name='apiuser',
            name='user_group',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='apiusers', to='stock_app.usergroup'),
        ),
        migrations.AlterField(
            model_name='usergroup',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Тип пользователя'),
        ),
    ]