# Generated by Django 2.2.16 on 2020-09-30 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0097_optional_preflight_user"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="job",
            name="uuid",
        ),
        migrations.RemoveField(
            model_name="preflightresult",
            name="uuid",
        ),
        migrations.RemoveField(
            model_name="scratchorgjob",
            name="canceled_at",
        ),
        migrations.AddField(
            model_name="scratchorgjob",
            name="org_id",
            field=models.CharField(blank=True, max_length=18, null=True),
        ),
    ]
