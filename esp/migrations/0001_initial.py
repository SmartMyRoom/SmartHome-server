# Generated by Django 4.2 on 2023-05-06 12:29

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ESP',
            fields=[
                ('name', models.TextField()),
                ('esp_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('api_key', models.UUIDField(default=uuid.uuid4)),
                ('is_connected', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Mood',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Key',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pin_name', models.TextField(default='')),
                ('name', models.TextField()),
                ('current', models.BooleanField(default=False)),
                ('last_updater_is_esp', models.BooleanField(default=False)),
                ('owner_esp', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='esp.esp')),
            ],
        ),
        migrations.AddField(
            model_name='esp',
            name='keys',
            field=models.ManyToManyField(blank=True, default=None, to='esp.key'),
        ),
    ]
