# Generated by Django 4.0.4 on 2022-06-20 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Soen', '0017_alter_specialeducationm_image1'),
    ]

    operations = [
        migrations.AlterField(
            model_name='licencem',
            name='man',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='soenmemberLicence', to='Soen.soenmemberm'),
        ),
        migrations.AlterField(
            model_name='skillm',
            name='man',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='soenmemberSkill', to='Soen.soenmemberm'),
        ),
        migrations.AlterField(
            model_name='specialeducationm',
            name='man',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='soenmemberEducation', to='Soen.soenmemberm'),
        ),
    ]
