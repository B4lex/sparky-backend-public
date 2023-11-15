# Generated by Django 4.2.6 on 2023-11-15 18:59

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("activities", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="ongoingactivity",
            name="enabled",
            field=models.BooleanField(default=True, verbose_name="Enabled"),
        ),
        migrations.AlterField(
            model_name="activitycompletion",
            name="completion_time",
            field=models.DateTimeField(
                blank=True,
                help_text="Describes whether and when activity has been completed for scheduled date",
                null=True,
                verbose_name="Completion time",
            ),
        ),
    ]
