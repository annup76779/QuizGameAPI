# Generated by Django 4.2.18 on 2025-02-06 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SubjectArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('dateCreated', models.DateTimeField(auto_now=True)),
                ('status', models.IntegerField(choices=[('1', 'Draft'), ('2', 'Published'), ('3', 'Closed')])),
                ('subjectID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizGame.subjectarea')),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('questionText', models.TextField()),
                ('score', models.IntegerField()),
                ('correctAnswer', models.TextField()),
                ('testID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizGame.test')),
            ],
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answerText', models.TextField()),
                ('questionID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quizGame.questions')),
            ],
        ),
    ]
