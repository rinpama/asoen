# Generated by Django 4.0.4 on 2022-05-27 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Soen', '0003_soenmemberdetailm_healthm'),
    ]

    operations = [
        migrations.CreateModel(
            name='InsuranceM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterModelOptions(
            name='genrem',
            options={'verbose_name_plural': '業者ジャンル'},
        ),
        migrations.AlterModelOptions(
            name='soenmemberdetailm',
            options={'verbose_name_plural': 'SoenMemberDetail'},
        ),
        migrations.AlterModelOptions(
            name='soenmemberm',
            options={'verbose_name_plural': 'SoenMember'},
        ),
    ]
