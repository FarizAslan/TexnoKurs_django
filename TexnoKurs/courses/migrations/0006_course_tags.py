# Generated by Django 4.0.4 on 2022-04-21 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='courses.tag'),
        ),
    ]