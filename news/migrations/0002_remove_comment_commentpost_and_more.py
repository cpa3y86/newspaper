# Generated by Django 4.1.3 on 2023-01-25 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='commentPost',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='commentUser',
        ),
        migrations.RemoveField(
            model_name='post',
            name='PostCategory',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='categoryTrough',
        ),
        migrations.RemoveField(
            model_name='postcategory',
            name='postThrouhgh',
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
        migrations.DeleteModel(
            name='PostCategory',
        ),
    ]
