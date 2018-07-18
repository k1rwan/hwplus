# Generated by Django 2.0.4 on 2018-07-18 12:00

import data.models
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(auto_now_add=True, null=True)),
                ('bupt_id', models.CharField(default=data.models.default_bupt_id, max_length=10, unique=True)),
                ('name', models.TextField(default='')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('phone', models.CharField(default=data.models.default_phone, max_length=11, unique=True)),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=6)),
                ('usertype', models.CharField(choices=[('student', 'student'), ('teacher', 'teacher'), ('assistant', 'assistant')], default='student', max_length=20)),
                ('class_number', models.CharField(default='noClass', max_length=10)),
                ('wechat', models.TextField(default='')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='HWFAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reviewed', models.BooleanField(default=False)),
                ('score', models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='HWFAssignment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('deadline', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='HWFCourseClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('join_code', models.TextField(max_length=512)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='creator_course', to=settings.AUTH_USER_MODEL)),
                ('students', models.ManyToManyField(related_name='students_course', to=settings.AUTH_USER_MODEL)),
                ('teaching_assistants', models.ManyToManyField(related_name='teaching_assistants_course', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HWFFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.FileField(upload_to='')),
                ('hashcode', models.TextField(unique=True)),
                ('initial_upload_time', models.DateTimeField(editable=False)),
            ],
        ),
        migrations.CreateModel(
            name='HWFFileAnswerValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('value', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.HWFFile')),
            ],
        ),
        migrations.CreateModel(
            name='HWFQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auto_score', models.BooleanField(default=False)),
                ('question_text', models.TextField()),
                ('description', models.TextField()),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='HWFReview',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('is_graph_review', models.BooleanField(default=False)),
                ('graph_value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HWFReviewTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HWFSelectAnswerValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='HWFSelectQuestionChoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('value', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='HWFSubmission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submit_time', models.DateTimeField()),
                ('description', models.TextField()),
                ('score', models.FloatField()),
                ('assignment', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.HWFAssignment')),
                ('submitter', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HWFSupportFileExtension',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('extension_regex', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='HWFFileAnswer',
            fields=[
                ('hwfanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.HWFAnswer')),
                ('values', models.ManyToManyField(to='data.HWFFileAnswerValue')),
            ],
            bases=('data.hwfanswer',),
        ),
        migrations.CreateModel(
            name='HWFFileQuestion',
            fields=[
                ('hwfquestion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.HWFQuestion')),
                ('support_extensions', models.ManyToManyField(to='data.HWFSupportFileExtension')),
            ],
            bases=('data.hwfquestion',),
        ),
        migrations.CreateModel(
            name='HWFSelectAnswer',
            fields=[
                ('hwfanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.HWFAnswer')),
                ('values', models.ManyToManyField(to='data.HWFSelectAnswerValue')),
            ],
            bases=('data.hwfanswer',),
        ),
        migrations.CreateModel(
            name='HWFSelectQuestion',
            fields=[
                ('hwfquestion_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.HWFQuestion')),
                ('is_multiple_choices', models.BooleanField(default=False)),
                ('correct_answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data.HWFSelectAnswer')),
            ],
            bases=('data.hwfquestion',),
        ),
        migrations.CreateModel(
            name='HWFTextAnswer',
            fields=[
                ('hwfanswer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='data.HWFAnswer')),
                ('values', models.TextField()),
            ],
            bases=('data.hwfanswer',),
        ),
        migrations.AddField(
            model_name='hwfreview',
            name='answer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.HWFAnswer'),
        ),
        migrations.AddField(
            model_name='hwfreview',
            name='mark_review',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.HWFReviewTag'),
        ),
        migrations.AddField(
            model_name='hwfreview',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='reviewer_review', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hwfquestion',
            name='assignment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.HWFAssignment'),
        ),
        migrations.AddField(
            model_name='hwffile',
            name='extension',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.HWFSupportFileExtension'),
        ),
        migrations.AddField(
            model_name='hwffile',
            name='initial_upload_user',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='hwfassignment',
            name='course_class',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.HWFCourseClass'),
        ),
        migrations.AddField(
            model_name='hwfanswer',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.HWFQuestion'),
        ),
        migrations.AddField(
            model_name='hwfanswer',
            name='submission',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.HWFSubmission'),
        ),
        migrations.AddField(
            model_name='hwfselectquestionchoice',
            name='question',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='data.HWFSelectQuestion'),
        ),
        migrations.AddField(
            model_name='hwffilequestion',
            name='values',
            field=models.ManyToManyField(to='data.HWFFile'),
        ),
    ]
