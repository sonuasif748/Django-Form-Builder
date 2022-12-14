# Generated by Django 3.2.8 on 2021-11-02 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forms', '0006_auto_20211102_1122'),
    ]

    operations = [
        migrations.AddField(
            model_name='form',
            name='intro',
            field=models.TextField(blank=True, verbose_name='Intro'),
        ),
        migrations.AddField(
            model_name='form',
            name='redirect_url',
            field=models.CharField(blank=True, help_text='An alternate URL to redirect to after form submission', max_length=200, null=True, verbose_name='Redirect url'),
        ),
        migrations.AddField(
            model_name='form',
            name='response',
            field=models.TextField(blank=True, verbose_name='Response'),
        ),
    ]
