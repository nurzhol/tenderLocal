# Generated by Django 3.0.3 on 2020-03-01 06:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_delete_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=30, verbose_name='Название')),
                ('price', models.FloatField(null=True, verbose_name='Цена')),
            ],
            options={
                'verbose_name': 'Тариф',
                'verbose_name_plural': 'Тарифы',
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='profile',
            name='tarif',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='users.Price', verbose_name='Тариф'),
        ),
    ]