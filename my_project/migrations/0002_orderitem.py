# Generated by Django 3.0.8 on 2020-07-29 14:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('my_project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('completed', models.BooleanField()),
                ('delivered', models.CharField(choices=[('pending', 'pending'), ('delivered', 'delivered')], max_length=10)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('items', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='my_project.Product')),
            ],
        ),
    ]