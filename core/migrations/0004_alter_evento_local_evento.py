# Generated by Django 5.0.3 on 2024-03-13 13:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_evento_local_evento'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento',
            name='local_evento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
