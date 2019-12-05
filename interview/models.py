from django.db import models


class Issue(models.Model):
    id_issue = models.AutoField(db_column='idIssue', primary_key=True)  # Field name made lowercase.
    site = models.ForeignKey('Site', models.DO_NOTHING, db_column='Site')  # Field name made lowercase.
    panel = models.ForeignKey('Panel', models.DO_NOTHING, db_column='Panel')  # Field name made lowercase.
    comment = models.TextField(db_column='Comment', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Issue'


class Panel(models.Model):
    id_panel = models.IntegerField(db_column='idPanel', primary_key=True)  # Field name made lowercase.
    brand = models.CharField(db_column='Brand', max_length=45)  # Field name made lowercase.
    model = models.CharField(db_column='Model', max_length=45)  # Field name made lowercase.
    power = models.IntegerField(db_column='Power')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Panel'


class Site(models.Model):
    id_site = models.IntegerField(db_column='idSite', primary_key=True)  # Field name made lowercase.
    site_name = models.CharField(db_column='SiteName', max_length=45)  # Field name made lowercase.
    state = models.CharField(db_column='State', max_length=45)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Site'
