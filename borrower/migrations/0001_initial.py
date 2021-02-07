# Generated by Django 3.1.4 on 2021-02-05 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Borrower',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('realname', models.CharField(max_length=32, verbose_name='姓名')),
                ('identify', models.CharField(max_length=255, verbose_name='身分')),
                ('email', models.EmailField(max_length=254, verbose_name='電子信箱')),
                ('work', models.CharField(max_length=255, verbose_name='職稱')),
                ('subject', models.CharField(max_length=255, verbose_name='任教科目')),
                ('tel', models.IntegerField(max_length=10, verbose_name='連絡電話')),
                ('state', models.CharField(max_length=3, verbose_name='狀態')),
            ],
        ),
    ]
