# Generated by Django 4.0.2 on 2022-02-26 12:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sections', '0004_remove_section_parentsection_section_parent'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='section', to=settings.AUTH_USER_MODEL),
        ),
    ]
