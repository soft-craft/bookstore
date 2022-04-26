# Generated by Django 3.0.6 on 2020-05-23 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_auto_20200517_0905'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='sub_category',
        ),
        migrations.AddField(
            model_name='product',
            name='academic_sub_category',
            field=models.CharField(choices=[('School Books', 'School Books'), ('High School Books', 'High School Books'), ('A Level Books', 'A Level Books'), ("Bachelor's Books", "Bachelor's Books"), ("Master's Books", "Master's Books")], default='School Book', max_length=50),
        ),
        migrations.AddField(
            model_name='product',
            name='nonacademic_sub_category',
            field=models.CharField(choices=[('Novel', 'Novel'), ('Stories', 'Stories'), ('Poetry', 'Poetry'), ('Novel', 'Novel'), ('Essay', 'Essay'), ('Biography', 'Biography'), ('Auto Biography', 'Auto Biography'), ('Article', 'Article'), ('Travelouge', 'Travelouge')], default='Novel', max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Academic', 'Academic'), ('Non-Academic', 'Non-Academic')], max_length=50),
        ),
    ]