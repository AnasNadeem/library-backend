# Generated by Django 3.2.8 on 2021-10-28 05:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='course_id',
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.course')),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='branch_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='library_app.branch'),
            preserve_default=False,
        ),
    ]
