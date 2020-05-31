# Generated by Django 2.2.12 on 2020-05-27 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='имя')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('is_active', models.BooleanField(default=True, verbose_name='категория активна')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True, verbose_name='Url')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='имя продукта')),
                ('slug', models.SlugField(max_length=255, unique=True, verbose_name='Url')),
                ('content', models.TextField(blank=True, verbose_name='описание продукта')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='дата добавления в каталог')),
                ('photo', models.ImageField(blank=True, upload_to='products_images')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='цена продукта')),
                ('quantity', models.DecimalField(decimal_places=0, default=0, max_digits=5, verbose_name='Продуктов в наличии')),
                ('is_active', models.BooleanField(default=True, verbose_name='категория активна')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.ProductCategory')),
            ],
            options={
                'ordering': ['-created_at'],
            },
        ),
    ]
