# Generated by Django 3.1.4 on 2021-03-13 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MajorDepartment',
            fields=[
                ('major', models.CharField(max_length=45, primary_key=True, serialize=False)),
                ('department', models.CharField(max_length=45)),
            ],
            options={
                'db_table': 'major_department',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SuccessTestCount',
            fields=[
                ('index', models.IntegerField(primary_key=True, serialize=False)),
                ('num_count', models.IntegerField()),
            ],
            options={
                'db_table': 'success_test_count',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestAllLecture',
            fields=[
                ('subject_num', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('subject_name', models.CharField(max_length=70)),
                ('classification', models.CharField(max_length=45)),
                ('selection', models.CharField(blank=True, max_length=45, null=True)),
                ('grade', models.IntegerField()),
            ],
            options={
                'db_table': 'test_all_lecture',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestNewLecture',
            fields=[
                ('subject_num', models.CharField(max_length=10, primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'test_new_lecture',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='TestUserInfo',
            fields=[
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=100)),
                ('year', models.IntegerField()),
                ('major', models.CharField(max_length=45)),
                ('major_status', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=45)),
                ('book', models.CharField(max_length=45)),
                ('eng', models.CharField(max_length=45)),
                ('mypage_json', models.JSONField(blank=True, null=True)),
                ('result_json', models.JSONField(blank=True, null=True)),
                ('en_result_json', models.JSONField(blank=True, null=True)),
            ],
            options={
                'db_table': 'test_user_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserGrade',
            fields=[
                ('student_id', models.CharField(max_length=10)),
                ('major', models.CharField(blank=True, max_length=45, null=True)),
                ('year', models.CharField(max_length=10)),
                ('semester', models.CharField(max_length=45)),
                ('subject_num', models.CharField(max_length=10)),
                ('subject_name', models.CharField(max_length=70)),
                ('classification', models.CharField(max_length=45)),
                ('selection', models.CharField(blank=True, max_length=45, null=True)),
                ('grade', models.IntegerField()),
                ('index', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'user_grade',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('student_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('year', models.IntegerField()),
                ('major', models.CharField(max_length=45)),
                ('name', models.CharField(max_length=45)),
                ('book', models.CharField(max_length=45)),
                ('eng', models.IntegerField()),
            ],
            options={
                'db_table': 'user_info',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='MediaUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('excel', models.FileField(upload_to='')),
            ],
        ),
    ]
