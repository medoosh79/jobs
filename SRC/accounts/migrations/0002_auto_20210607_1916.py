# Generated by Django 3.2.4 on 2021-06-07 16:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='aboutskills',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='About Skills'),
        ),
        migrations.AddField(
            model_name='person',
            name='address',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='person',
            name='bg_pic',
            field=models.ImageField(default='defualt.jpg', upload_to='background/'),
        ),
        migrations.AddField(
            model_name='person',
            name='bio',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Describe yourself'),
        ),
        migrations.AddField(
            model_name='person',
            name='biopro',
            field=models.TextField(blank=True, max_length=200, null=True, verbose_name='Your Vision'),
        ),
        migrations.AddField(
            model_name='person',
            name='birthday',
            field=models.DateField(blank=True, null=True, verbose_name='Birthday'),
        ),
        migrations.AddField(
            model_name='person',
            name='career',
            field=models.CharField(blank=True, max_length=70, null=True, verbose_name='Career'),
        ),
        migrations.AddField(
            model_name='person',
            name='certification',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Certification '),
        ),
        migrations.AddField(
            model_name='person',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='date_update',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='person',
            name='degree',
            field=models.CharField(blank=True, choices=[('Student', 'Student'), ('Medium_Level', 'Medium_Level'), ('Bachelor', 'Bachelor'), ('Master', 'Master'), ('Doctorate', 'Doctorate')], max_length=15, null=True, verbose_name='Degree'),
        ),
        migrations.AddField(
            model_name='person',
            name='fb',
            field=models.URLField(blank=True, null=True, verbose_name='Face Book'),
        ),
        migrations.AddField(
            model_name='person',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female'), ('NO Preference', 'NO Preference')], default=1, max_length=15, verbose_name='Gender'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='graduation_year',
            field=models.DateField(blank=True, null=True, verbose_name='Graduation Year '),
        ),
        migrations.AddField(
            model_name='person',
            name='instagram',
            field=models.URLField(blank=True, null=True, verbose_name='Instagram '),
        ),
        migrations.AddField(
            model_name='person',
            name='job_type',
            field=models.CharField(choices=[('Full Time', 'Full Time'), ('Part Time', 'Part Time'), ('Remote', 'Remote'), ('Freelance', 'Freelance')], default=1, max_length=15, verbose_name='Job Type'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='person',
            name='linkedin',
            field=models.URLField(blank=True, null=True, verbose_name='Linkedin '),
        ),
        migrations.AddField(
            model_name='person',
            name='mobile',
            field=models.IntegerField(blank=True, null=True, verbose_name='Mobile'),
        ),
        migrations.AddField(
            model_name='person',
            name='nameskill1',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='First Skill'),
        ),
        migrations.AddField(
            model_name='person',
            name='profile_pic',
            field=models.ImageField(default='defualt.jpg', upload_to='user/'),
        ),
        migrations.AddField(
            model_name='person',
            name='state',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='State'),
        ),
        migrations.AddField(
            model_name='person',
            name='tw',
            field=models.URLField(blank=True, null=True, verbose_name='Twitter '),
        ),
        migrations.AddField(
            model_name='person',
            name='valueskill1',
            field=models.IntegerField(blank=True, null=True, verbose_name='Value Skill1'),
        ),
        migrations.AddField(
            model_name='person',
            name='zip',
            field=models.CharField(blank=True, max_length=25, null=True, verbose_name='ZIP'),
        ),
    ]
