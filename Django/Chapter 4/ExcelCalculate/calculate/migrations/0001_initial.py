# Generated by Django 3.2.4 on 2021-08-11 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_upload_file', models.FileField(upload_to='user_upload_files/%Y%m%d/')),
            ],
        ),
    ]
