# Generated by Django 4.2.1 on 2023-06-08 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=120, unique=True, verbose_name='Название категории')),
                ('slug', models.SlugField(blank=True, max_length=120, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, verbose_name='Описание продукта')),
                ('phone_sender', models.CharField(max_length=13)),
                ('phone_receiver', models.CharField(max_length=13)),
                ('address_sender', models.CharField(max_length=100)),
                ('address_receiver', models.CharField(max_length=100)),
                ('price', models.IntegerField(default=200)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='orders.category', verbose_name='Категория')),
            ],
        ),
    ]
