# Generated by Django 2.1 on 2018-09-07 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20180807_1203'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('decription', models.TextField()),
                ('count', models.IntegerField(default=0)),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-update_date', '_id']},
        ),
        migrations.AddField(
            model_name='answer',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.Post'),
        ),
    ]
