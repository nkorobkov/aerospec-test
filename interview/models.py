from django.db import models


class Issue(models.Model):
    id_issue = models.AutoField(db_column='idIssue', primary_key=True)
    site = models.ForeignKey('Site', models.DO_NOTHING, db_column='Site')
    panel = models.ForeignKey('Panel', models.DO_NOTHING, db_column='Panel')
    comment = models.TextField(db_column='Comment', blank=True, null=True,  max_length=199)

    class Meta:
        managed = False
        db_table = 'Issue'


class Panel(models.Model):
    id_panel = models.IntegerField(db_column='idPanel', primary_key=True)
    brand = models.CharField(db_column='Brand', max_length=45)
    model = models.CharField(db_column='Model', max_length=45)
    power = models.IntegerField(db_column='Power')

    def __str__(self):
        return '{} ({})'.format(self.model, self.brand)

    class Meta:
        managed = False
        db_table = 'Panel'


class Site(models.Model):
    id_site = models.IntegerField(db_column='idSite', primary_key=True)
    site_name = models.CharField(db_column='SiteName', max_length=45)
    state = models.CharField(db_column='State', max_length=45)

    def __str__(self):
        return '{} ({})'.format(self.site_name, self.state)

    class Meta:
        managed = False
        db_table = 'Site'
