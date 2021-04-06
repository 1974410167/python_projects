# Generated by Django 3.0.4 on 2020-08-19 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('case1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='user',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=24)),
                ('file', models.FileField(upload_to='uploads/')),
                ('image', models.ImageField(upload_to='uploads/')),
            ],
        ),
    ]