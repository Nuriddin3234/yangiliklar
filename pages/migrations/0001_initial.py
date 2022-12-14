# Generated by Django 4.1.3 on 2022-11-23 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Murojatlar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ism', models.CharField(max_length=15)),
                ('familya', models.CharField(max_length=25)),
                ('tel_raqam', models.PositiveIntegerField(max_length=9)),
                ('murojatlar', models.TextField()),
                ('vaqt', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('summery', models.CharField(max_length=200)),
                ('photo', models.ImageField(upload_to='images/')),
                ('data', models.DateTimeField()),
                ('admin', models.CharField(choices=[('Shahzod', 'Shahzod'), ('Anvar', 'Anvar'), ('Qobil', 'Qobil'), ('Davron', 'Davron')], max_length=10)),
            ],
        ),
    ]
