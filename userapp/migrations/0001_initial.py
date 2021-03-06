# Generated by Django 2.0.6 on 2020-09-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=40)),
                ('password', models.CharField(max_length=40)),
                ('phone', models.CharField(blank=True, max_length=11, null=True)),
                ('gender', models.SmallIntegerField(choices=[(0, 'male'), (1, 'female'), (2, 'other')], default=0)),
                ('pic', models.ImageField(default='pic/1.jpg', upload_to='pic')),
            ],
            options={
                'verbose_name': '员工',
                'verbose_name_plural': '员工',
                'db_table': 'db_employee',
            },
        ),
    ]
