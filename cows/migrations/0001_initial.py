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
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('crotal_number', models.CharField(max_length=50, db_index=True)),
                ('name', models.CharField(null=True, blank=True, max_length=200)),
                ('sex', models.CharField(choices=[('M', 'Macho'), ('H', 'Hembra')], max_length=1)),
                ('raze', models.CharField(max_length=50)),
                ('birth_date', models.DateField()),
                ('explotation_code', models.CharField(max_length=50)),
                ('date_register_as_mother_or_father', models.DateField(null=True, blank=True)),
                ('date_of_send_to_feeding', models.DateField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Earnings',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=200)),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('date', models.DateField()),
                ('type', models.CharField(max_length=200)),
                ('price', models.DecimalField(max_digits=20, decimal_places=2)),
                ('quantity', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CowDrop',
            fields=[
                ('cow', models.OneToOneField(serialize=False, primary_key=True, to='cows.Cow')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='InExplotationDeath',
            fields=[
                ('cowdrop_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, primary_key=True, to='cows.CowDrop')),
                ('reason', models.TextField()),
            ],
            bases=('cows.cowdrop',),
        ),
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('cowdrop_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, primary_key=True, to='cows.CowDrop')),
                ('explotation_code', models.CharField(max_length=50)),
                ('sell_price', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
            bases=('cows.cowdrop',),
        ),
        migrations.CreateModel(
            name='SentToSlaughterhouse',
            fields=[
                ('cowdrop_ptr', models.OneToOneField(serialize=False, auto_created=True, parent_link=True, primary_key=True, to='cows.CowDrop')),
                ('weight', models.DecimalField(max_digits=20, decimal_places=3)),
                ('sell_price', models.DecimalField(max_digits=20, decimal_places=2)),
            ],
            bases=('cows.cowdrop',),
        ),
    ]
