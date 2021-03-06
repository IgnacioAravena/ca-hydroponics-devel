# Generated by Django 2.1.4 on 2018-12-09 21:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_backend', '0004_auto_20181206_2357'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='static/img/farm/')),
            ],
        ),
        migrations.RemoveField(
            model_name='farm',
            name='description',
        ),
        migrations.RemoveField(
            model_name='farm',
            name='image',
        ),
        migrations.AddField(
            model_name='farm',
            name='seed',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app_backend.Seed'),
        ),
    ]
