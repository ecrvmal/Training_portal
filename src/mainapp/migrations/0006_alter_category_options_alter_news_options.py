# Generated by Django 4.2.5 on 2023-10-12 10:47

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("mainapp", "0005_course_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="news",
            options={"verbose_name": "News", "verbose_name_plural": "News"},
        ),
    ]
