# Generated by Django 2.2.12 on 2020-07-02 16:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='image/about')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'about',
            },
        ),
        migrations.CreateModel(
            name='Carousol',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='image/carousol')),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'carousol',
                'verbose_name_plural': 'carousols',
            },
        ),
        migrations.CreateModel(
            name='SiteInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slogan', models.CharField(max_length=255)),
                ('logo', models.ImageField(upload_to='logo/site')),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.IntegerField()),
                ('date_add', models.DateTimeField(auto_now_add=True)),
                ('date_update', models.DateTimeField(auto_now=True)),
                ('status', models.BooleanField(default=True)),
                ('carousol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousol_site', to='website.Carousol')),
            ],
            options={
                'verbose_name': 'site info',
                'verbose_name_plural': 'sites infos',
            },
        ),
    ]
