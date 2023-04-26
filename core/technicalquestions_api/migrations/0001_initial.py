# Generated by Django 4.1.2 on 2023-04-26 08:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizQuestion',
            fields=[
                ('question_id', models.IntegerField(auto_created=True, primary_key=True, serialize=False)),
                ('topic', models.CharField(max_length=5000)),
                ('question', models.TextField(max_length=5000)),
                ('option_a', models.CharField(max_length=5000)),
                ('option_b', models.CharField(max_length=5000)),
                ('option_c', models.CharField(max_length=5000)),
                ('option_d', models.CharField(max_length=5000)),
                ('correct_answer', models.CharField(max_length=5000)),
                ('difficulty', models.CharField(max_length=5000)),
                ('cognitive_level', models.CharField(max_length=5000)),
                ('subject', models.CharField(max_length=5000)),
            ],
        ),
        migrations.CreateModel(
            name='ResultTest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_date', models.DateTimeField(auto_now_add=True)),
                ('results', models.JSONField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
