# Generated by Django 4.0.2 on 2022-03-03 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'batches',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=300)),
                ('nickname', models.CharField(max_length=100, null=True, unique=True)),
                ('email', models.CharField(max_length=100, null=True, unique=True)),
                ('phone_number', models.CharField(blank=True, max_length=100)),
                ('address', models.CharField(blank=True, max_length=100)),
                ('zipcode', models.CharField(blank=True, max_length=100)),
                ('is_wecode', models.BooleanField(default=True)),
                ('point', models.PositiveIntegerField(default=100000)),
                ('batch', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.batch')),
            ],
            options={
                'db_table': 'users',
            },
        ),
        migrations.CreateModel(
            name='WecodeUserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('thumbnail_image', models.CharField(max_length=400)),
                ('selected_image', models.CharField(max_length=400)),
                ('status_message', models.CharField(max_length=400)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'wecode_user_details',
            },
        ),
    ]
