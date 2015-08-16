# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cow',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('crotal_number', models.CharField(db_index=True, max_length=50)),
                ('name', models.CharField(null=True, blank=True, max_length=200)),
                ('sex', models.CharField(max_length=1, choices=[('M', 'Macho'), ('H', 'Hembra')])),
                ('raze', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('explotation_code', models.CharField(max_length=50)),
                ('date_register_as_mother_or_father', models.DateField(null=True, blank=True)),
                ('date_of_send_to_feeding', models.DateField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Earnings',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('quantity', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='InExplotationDeath',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('reason', models.TextField()),
                ('cow', models.ForeignKey(to='cows.Cow')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('explotation_code', models.CharField(max_length=50)),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cow', models.ForeignKey(to='cows.Cow')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SentToSlaughterhouse',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('date', models.DateField()),
                ('weight', models.DecimalField(decimal_places=3, max_digits=20)),
                ('sell_price', models.DecimalField(decimal_places=2, max_digits=20)),
                ('cow', models.ForeignKey(to='cows.Cow')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
