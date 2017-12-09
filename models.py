# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Admin(models.Model):
    adm_id = models.AutoField(db_column='ADM_ID', primary_key=True)  # Field name made lowercase.
    adm_emaill = models.IntegerField(db_column='ADM_Emaill', blank=True, null=True)  # Field name made lowercase.
    adm_password = models.IntegerField(db_column='ADM_Password', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin'


class AdminCategory(models.Model):
    adminadm = models.ForeignKey(Admin, models.DO_NOTHING, db_column='AdminAdm_id', primary_key=True)  # Field name made lowercase.
    categorycat = models.ForeignKey('Category', models.DO_NOTHING, db_column='CategoryCat_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_category'
        unique_together = (('adminadm', 'categorycat'),)


class AdminKeyWords(models.Model):
    adminadm = models.ForeignKey(Admin, models.DO_NOTHING, db_column='AdminAdm_id', primary_key=True)  # Field name made lowercase.
    key_wordskeyw = models.ForeignKey('KeyWords', models.DO_NOTHING, db_column='Key_WordsKeyw_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'admin_key_words'
        unique_together = (('adminadm', 'key_wordskeyw'),)





class AcceptedAdvertisement(models.Model):
   accept_date = models.DateField(null=False)
   advertiser = models.ForeignKey('Advertiser', models.DO_NOTHING)



class RejectedAdvertisement(models.Model):
    reason = models.CharField(max_length=255, null=False)
    date = models.DateField(null=False)
    advertiser = models.ForeignKey('Advertiser', models.DO_NOTHING)



class AdvertiserAdvertising(models.Model):
    advr = models.ForeignKey(Advertiser, models.DO_NOTHING, db_column='Advr_id', primary_key=True)  # Field name made lowercase.
    avd = models.ForeignKey(Advertisement, models.DO_NOTHING, db_column='Avd_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'advertiser_advertising'
        unique_together = (('advr', 'avd'),)


class AdvertisingKeyWords(models.Model):
    avd = models.ForeignKey(Advertisement, models.DO_NOTHING, db_column='Avd_id', primary_key=True)  # Field name made lowercase.
    key = models.ForeignKey('KeyWords', models.DO_NOTHING, db_column='Key_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'advertising_key_words'
        unique_together = (('avd', 'key'),)





class Entity(models.Model):
    advertisingavd = models.ForeignKey(Advertisement, models.DO_NOTHING, db_column='AdvertisingAvd_id')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'entity'


class KeyWords(models.Model):
    key_id = models.AutoField(db_column='Key_id', primary_key=True)  # Field name made lowercase.
    target_words = models.CharField(db_column='Target_Words', max_length=255, blank=True, null=True)  # Field name made lowercase.





class ResponseAdvertisment(models.Model):
    res_id = models.AutoField(db_column='RES_ID', primary_key=True)  # Field name made lowercase.
    column = models.IntegerField(db_column='Column', blank=True, null=True)  # Field name made lowercase.
    adm_ip = models.CharField(db_column='ADM_IP', max_length=10, blank=True, null=True)  # Field name made lowercase.
    adm = models.ForeignKey(Admin, models.DO_NOTHING, db_column='ADM_ID')  # Field name made lowercase.
    is_accepted = models.TextField(db_column='Is_Accepted', blank=True, null=True)  # Field name made lowercase. This field type is a guess.
    acceptance = models.ForeignKey(AdvertisementAcceptance, models.DO_NOTHING, db_column='Acceptance_ID')  # Field name made lowercase.
    rej = models.ForeignKey(AdvertisementRejection, models.DO_NOTHING, db_column='REJ_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'response_advertisment'


class ThemesPhotoThemes(models.Model):
    themesth = models.ForeignKey(Themes, models.DO_NOTHING, db_column='ThemesTH_id', primary_key=True)  # Field name made lowercase.
    photo_themespht = models.ForeignKey(PhotoThemes, models.DO_NOTHING, db_column='Photo_ThemesPHT_ID')  # Field name made lowercase.

    class Meta:
        unique_together = (('themesth', 'photo_themespht'),)


