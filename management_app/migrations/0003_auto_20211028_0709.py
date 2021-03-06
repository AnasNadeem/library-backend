# Generated by Django 3.2.8 on 2021-10-28 07:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0002_auto_20211028_0517'),
        ('management_app', '0002_alter_application_enrol_num'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='BookSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_status', models.CharField(choices=[('pending', 'pending'), ('issued', 'issued'), ('due', 'due'), ('returned', 'returned')], max_length=55)),
                ('issued_at', models.DateField(auto_now_add=True)),
                ('returned_at', models.DateField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library_app.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management_app.application')),
            ],
        ),
    ]
