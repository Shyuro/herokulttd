# Generated by Django 4.0.4 on 2022-05-07 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='photo',
            field=models.ImageField(default=1, upload_to='pics'),
            preserve_default=False,
        ),
    ]
