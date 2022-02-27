# Generated by Django 4.0.2 on 2022-02-24 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('parentSection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sections.section')),
            ],
        ),
    ]
