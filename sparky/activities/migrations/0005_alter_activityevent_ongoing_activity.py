# Generated by Django 4.2.6 on 2023-11-16 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("activities", "0004_activityevent_delete_activitycompletion_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activityevent",
            name="ongoing_activity",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="events",
                to="activities.ongoingactivity",
                verbose_name="Ongoing activity",
            ),
        ),
    ]
