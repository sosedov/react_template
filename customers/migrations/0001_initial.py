# Generated by Django 3.1.7 on 2021-04-06 08:42

from django.db import migrations, models

def create_data(apps, schema_editor):
    Customer = apps.get_model('customers', 'Customer')
    Customer(first_name="Customer 001", last_name="Customer 001", email="customer001@email.com", phone="00000000", address="Customer 000 Address", description= "Customer 001 description").save()

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255, verbose_name='First name')),
                ('last_name', models.CharField(max_length=255, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
            ],
        ),
    ]
