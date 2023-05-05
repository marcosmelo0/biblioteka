# Generated by Django 4.2 on 2023-05-05 14:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exemplary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('default_loan_duration', models.IntegerField(default=7)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exemplaries', to='books.book')),
            ],
        ),
    ]
