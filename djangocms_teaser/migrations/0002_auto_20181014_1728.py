# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-14 14:28
from __future__ import unicode_literals

import cms.models.fields
from django.db import migrations, models
import django.db.models.deletion
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0020_old_tree_cleanup'),
        ('djangocms_teaser', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tiser',
            name='link_attributes',
            field=djangocms_attributes_field.fields.AttributesField(blank=True, default=dict, verbose_name='Link attributes'),
        ),
        migrations.AddField(
            model_name='tiser',
            name='link_page',
            field=cms.models.fields.PageField(blank=True, help_text='Wraps the image in a link to an internal (page) URL.', null=True, on_delete=django.db.models.deletion.CASCADE, to='cms.Page', verbose_name='Internal URL'),
        ),
        migrations.AddField(
            model_name='tiser',
            name='link_target',
            field=models.CharField(blank=True, choices=[('_blank', 'Open in new window'), ('_self', 'Open in same window'), ('_parent', 'Delegate to parent'), ('_top', 'Delegate to top')], max_length=255, verbose_name='Link target'),
        ),
        migrations.AddField(
            model_name='tiser',
            name='link_url',
            field=models.URLField(blank=True, help_text='Wraps the image in a link to an external URL.', max_length=2040, verbose_name='External URL'),
        ),
    ]
