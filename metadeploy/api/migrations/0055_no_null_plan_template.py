# Generated by Django 2.1.7 on 2019-02-28 18:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0054_make_plan_template_required")]

    operations = [
        migrations.AlterField(
            model_name="plan",
            name="plan_template",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT, to="api.PlanTemplate"
            ),
        )
    ]
