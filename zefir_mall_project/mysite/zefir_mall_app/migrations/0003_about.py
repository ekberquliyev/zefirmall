# Generated by Django 4.0.4 on 2022-04-22 05:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zefir_mall_app', '0002_navbar_alter_infocenter_info_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
    ]
