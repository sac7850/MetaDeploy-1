# Generated by Django 2.2.15 on 2020-09-03 18:48

import django.db.models.deletion
import hashid_field.field
from django.db import migrations, models

ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0092_merge_20200826_1452"),
    ]

    operations = [
        migrations.CreateModel(
            name="ScratchOrgJob",
            fields=[
                (
                    "id",
                    hashid_field.field.HashidAutoField(
                        alphabet=ALPHABET,
                        min_length=7,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("email", models.EmailField(max_length=254)),
                ("enqueued_at", models.DateTimeField(null=True)),
                ("job_id", models.UUIDField(null=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("edited_at", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("started", "started"),
                            ("complete", "complete"),
                            ("failed", "failed"),
                            ("canceled", "canceled"),
                        ],
                        default="started",
                        max_length=64,
                    ),
                ),
                (
                    "canceled_at",
                    models.DateTimeField(
                        help_text=(
                            "The time at which the Job canceled itself, likely just a "
                            "bit after it was told to cancel itself."
                        ),
                        null=True,
                    ),
                ),
                (
                    "plan",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.Plan"
                    ),
                ),
            ],
            options={"abstract": False},
        ),
    ]
