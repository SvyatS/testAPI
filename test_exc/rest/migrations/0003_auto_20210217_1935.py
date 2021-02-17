# Generated by Django 2.2.1 on 2021-02-17 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rest', '0002_auto_20210217_1828'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='answer',
            options={'verbose_name': 'Ответ пользователя', 'verbose_name_plural': 'Ответы пользователей'},
        ),
        migrations.RemoveField(
            model_name='answer',
            name='answe_choice',
        ),
        migrations.AlterField(
            model_name='answer',
            name='answer_text',
            field=models.TextField(verbose_name='Ответ'),
        ),
        migrations.DeleteModel(
            name='AnswerQuestion',
        ),
    ]
