# Generated by Django 5.1 on 2024-09-24 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='itemname')),
                ('price', models.IntegerField(blank=True, max_length=140, verbose_name='price')),
                ('type', models.CharField(choices=[('mustitem', '必需品'), ('notmustitem', '娯楽品')], max_length=30)),
                ('date', models.DateField(max_length=1000, verbose_name='date')),
            ],
        ),
    ]
