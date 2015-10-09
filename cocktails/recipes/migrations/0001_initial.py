# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Component',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('amount', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('name', models.CharField(max_length=255)),
                ('measurement', models.CharField(blank=True, choices=[('ounce', 'Ounce(s)'), ('tsp', 'Teaspoon(s)'), ('tbsp', 'Tablespoon(s)'), ('dash', 'Dash(es)')], max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, verbose_name='ID', auto_created=True)),
                ('text', models.TextField()),
                ('drink', models.ForeignKey(to='recipes.Drink', related_name='steps')),
            ],
        ),
        migrations.AddField(
            model_name='drink',
            name='components',
            field=models.ManyToManyField(related_name='drinks', to='recipes.Ingredient', through='recipes.Component'),
        ),
        migrations.AddField(
            model_name='component',
            name='drink',
            field=models.ForeignKey(to='recipes.Drink', related_name='+'),
        ),
        migrations.AddField(
            model_name='component',
            name='ingredient',
            field=models.ForeignKey(to='recipes.Ingredient', related_name='+'),
        ),
        migrations.AlterOrderWithRespectTo(
            name='step',
            order_with_respect_to='drink',
        ),
    ]
