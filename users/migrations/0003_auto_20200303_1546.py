# Generated by Django 3.0.2 on 2020-03-03 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20200228_1039'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodAllergies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'foodallergies',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='allergies_list',
            options={'managed': False},
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='city',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='contact_number',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='social_accounts',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='state',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='zip_code',
        ),
        migrations.AddField(
            model_name='customuser',
            name='activity',
            field=models.CharField(blank=True, choices=[(1, 'Sedentary'), (2, 'Lightly Active'), (3, 'Moderately Active'), (4, 'Active')], default='', max_length=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.CharField(blank=True, choices=[(1, '15-20'), (2, '20-25'), (3, '25-30'), (4, '30-35'), (5, '35-40'), (6, '40-45'), (7, '45-50')], default='', max_length=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, choices=[(1, 'Male'), (2, 'Female')], default='', max_length=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='height',
            field=models.CharField(blank=True, choices=[(1, '4\'0" - 4\'11"'), (2, '5\'0" - 5\'11"'), (3, '6\'0" - 6\'11"'), (4, '7\'0" - 7\'11"')], default='', max_length=1),
        ),
        migrations.AddField(
            model_name='customuser',
            name='weight',
            field=models.CharField(blank=True, choices=[(1, 'Below 150lb'), (2, '150lb to 200lb'), (3, 'Over 200lb')], default='', max_length=1),
        ),
    ]
