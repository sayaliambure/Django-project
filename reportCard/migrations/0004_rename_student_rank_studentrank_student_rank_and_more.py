# Generated by Django 4.2.9 on 2024-02-02 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("reportCard", "0003_studentrank"),
    ]

    operations = [
        migrations.RenameField(
            model_name="studentrank", old_name="Student_rank", new_name="student_rank",
        ),
        migrations.AlterUniqueTogether(
            name="studentrank",
            unique_together={("student_rank", "date_of_report_card_generation")},
        ),
    ]
