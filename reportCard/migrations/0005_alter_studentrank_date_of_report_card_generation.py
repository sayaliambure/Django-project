# Generated by Django 4.2.9 on 2024-02-02 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("reportCard", "0004_rename_student_rank_studentrank_student_rank_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="studentrank",
            name="date_of_report_card_generation",
            field=models.DateField(auto_now_add=True),
        ),
    ]
