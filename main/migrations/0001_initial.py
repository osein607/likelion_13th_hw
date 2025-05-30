# Generated by Django 5.1.7 on 2025-05-02 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('pub_date', models.DateTimeField()),
                ('mbti', models.CharField(max_length=50)),
            ],
        ),
    ]
