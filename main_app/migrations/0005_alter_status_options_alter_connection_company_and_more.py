# Generated by Django 4.2.8 on 2024-01-09 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_alter_status_date_alter_status_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='status',
            options={'ordering': ['date']},
        ),
        migrations.AlterField(
            model_name='connection',
            name='company',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='connection',
            name='email',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='connection',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='connection',
            name='phone',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='connection',
            name='url',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='bookmarked',
            field=models.BooleanField(default=False, verbose_name='Add Bookmark'),
        ),
        migrations.AlterField(
            model_name='job',
            name='connections',
            field=models.ManyToManyField(blank=True, to='main_app.connection'),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='job',
            name='notes',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.IntegerField(blank=True),
        ),
    ]
