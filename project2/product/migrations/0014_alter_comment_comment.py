# Generated by Django 4.2.3 on 2023-08-19 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_alter_comment_comment_alter_comment_rate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(max_length=100),
        ),
    ]
