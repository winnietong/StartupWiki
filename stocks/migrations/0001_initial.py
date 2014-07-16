# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'User'
        db.create_table(u'stocks_user', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=128)),
            ('last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('is_superuser', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('username', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('is_staff', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('date_joined', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=12)),
            ('balance', self.gf('django.db.models.fields.IntegerField')(default=100, max_length=10)),
        ))
        db.send_create_signal(u'stocks', ['User'])

        # Adding M2M table for field groups on 'User'
        m2m_table_name = db.shorten_name(u'stocks_user_groups')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'stocks.user'], null=False)),
            ('group', models.ForeignKey(orm[u'auth.group'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'group_id'])

        # Adding M2M table for field user_permissions on 'User'
        m2m_table_name = db.shorten_name(u'stocks_user_user_permissions')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('user', models.ForeignKey(orm[u'stocks.user'], null=False)),
            ('permission', models.ForeignKey(orm[u'auth.permission'], null=False))
        ))
        db.create_unique(m2m_table_name, ['user_id', 'permission_id'])

        # Adding model 'Category'
        db.create_table(u'stocks_category', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=20)),
        ))
        db.send_create_signal(u'stocks', ['Category'])

        # Adding model 'Company'
        db.create_table(u'stocks_company', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=120)),
            ('founded', self.gf('django.db.models.fields.DateField')(null=True)),
            ('address1', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('funding', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(max_length=100, null=True, blank=True)),
        ))
        db.send_create_signal(u'stocks', ['Company'])

        # Adding M2M table for field followers on 'Company'
        m2m_table_name = db.shorten_name(u'stocks_company_followers')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm[u'stocks.company'], null=False)),
            ('user', models.ForeignKey(orm[u'stocks.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'user_id'])

        # Adding M2M table for field category on 'Company'
        m2m_table_name = db.shorten_name(u'stocks_company_category')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('company', models.ForeignKey(orm[u'stocks.company'], null=False)),
            ('category', models.ForeignKey(orm[u'stocks.category'], null=False))
        ))
        db.create_unique(m2m_table_name, ['company_id', 'category_id'])

        # Adding model 'Comment'
        db.create_table(u'stocks_comment', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['stocks.User'])),
            ('post', self.gf('django.db.models.fields.related.ForeignKey')(related_name='comments', to=orm['stocks.Company'])),
        ))
        db.send_create_signal(u'stocks', ['Comment'])

        # Adding model 'FundingRound'
        db.create_table(u'stocks_fundinground', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('series', self.gf('django.db.models.fields.CharField')(max_length=20)),
            ('raised', self.gf('django.db.models.fields.IntegerField')()),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('company', self.gf('django.db.models.fields.related.ForeignKey')(related_name='funding_round', to=orm['stocks.Company'])),
        ))
        db.send_create_signal(u'stocks', ['FundingRound'])


    def backwards(self, orm):
        # Deleting model 'User'
        db.delete_table(u'stocks_user')

        # Removing M2M table for field groups on 'User'
        db.delete_table(db.shorten_name(u'stocks_user_groups'))

        # Removing M2M table for field user_permissions on 'User'
        db.delete_table(db.shorten_name(u'stocks_user_user_permissions'))

        # Deleting model 'Category'
        db.delete_table(u'stocks_category')

        # Deleting model 'Company'
        db.delete_table(u'stocks_company')

        # Removing M2M table for field followers on 'Company'
        db.delete_table(db.shorten_name(u'stocks_company_followers'))

        # Removing M2M table for field category on 'Company'
        db.delete_table(db.shorten_name(u'stocks_company_category'))

        # Deleting model 'Comment'
        db.delete_table(u'stocks_comment')

        # Deleting model 'FundingRound'
        db.delete_table(u'stocks_fundinground')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'stocks.category': {
            'Meta': {'object_name': 'Category'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'stocks.comment': {
            'Meta': {'object_name': 'Comment'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'post': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['stocks.Company']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'comments'", 'to': u"orm['stocks.User']"})
        },
        u'stocks.company': {
            'Meta': {'object_name': 'Company'},
            'address1': ('django.db.models.fields.CharField', [], {'max_length': '150'}),
            'category': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'company'", 'blank': 'True', 'to': u"orm['stocks.Category']"}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            'followers': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'company'", 'blank': 'True', 'to': u"orm['stocks.User']"}),
            'founded': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            'funding': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '120'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        u'stocks.fundinground': {
            'Meta': {'object_name': 'FundingRound'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'funding_round'", 'to': u"orm['stocks.Company']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'raised': ('django.db.models.fields.IntegerField', [], {}),
            'series': ('django.db.models.fields.CharField', [], {'max_length': '20'})
        },
        u'stocks.user': {
            'Meta': {'object_name': 'User'},
            'balance': ('django.db.models.fields.IntegerField', [], {'default': '100', 'max_length': '10'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '12'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        }
    }

    complete_apps = ['stocks']