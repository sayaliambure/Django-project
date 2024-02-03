# Generated by Django 4.2.9 on 2024-02-02 14:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("reportCard", "0002_subject_subjectmarks"),
    ]

    operations = [
        migrations.CreateModel(
            name="StudentRank",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_of_report_card_generation", models.DateField(auto_created=True)),
                ("Student_rank", models.IntegerField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="studentReportCard",
                        to="reportCard.student",
                    ),
                ),
            ],
        ),
    ]