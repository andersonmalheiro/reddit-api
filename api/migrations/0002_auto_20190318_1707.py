# Generated by Django 2.1.7 on 2019-03-18 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.CharField(max_length=300, verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=50, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='subreddit',
            name='description',
            field=models.CharField(max_length=500, verbose_name='Description'),
        ),
        migrations.AlterField(
            model_name='subreddit',
            name='name',
            field=models.CharField(max_length=50, verbose_name='Name'),
        ),
    ]
