# Generated by Django 2.2.16 on 2020-11-13 14:45

from django.db import migrations

import metadeploy.api.models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0107_productcategory_is_listed"),
    ]

    operations = [
        migrations.AlterField(
            model_name="allowedlist",
            name="description",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="plantemplatetranslation",
            name="error_message",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="plantemplatetranslation",
            name="post_install_message",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="plantemplatetranslation",
            name="preflight_message",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="plantranslation",
            name="post_install_message_additional",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="plantranslation",
            name="preflight_message_additional",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="productcategorytranslation",
            name="description",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="producttranslation",
            name="click_through_agreement",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="producttranslation",
            name="description",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="producttranslation",
            name="error_message",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="siteprofiletranslation",
            name="copyright_notice",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
        migrations.AlterField(
            model_name="siteprofiletranslation",
            name="welcome_text",
            field=metadeploy.api.models.MarkdownField(
                blank=True,
                help_text="Markdown is supported",
                property_suffix="_markdown",
            ),
        ),
    ]
