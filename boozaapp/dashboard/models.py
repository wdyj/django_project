# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Users(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(unique=True, max_length=300)
    nickname = models.CharField(max_length=45, blank=True, null=True)
    user_imgname = models.CharField(max_length=120, blank=True, null=True)
    sex = models.CharField(max_length=10, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    password_hash = models.CharField(max_length=255)
    access_token = models.CharField(max_length=70)
    deviceid = models.CharField(max_length=255, blank=True, null=True)
    hsk_device_token = models.CharField(max_length=255, blank=True, null=True)
    market = models.CharField(max_length=8)
    join_market = models.CharField(max_length=8)
    is_heavyuser = models.IntegerField()
    did_review = models.IntegerField()
    alarm_notice = models.IntegerField()
    alarm_stock = models.IntegerField()
    alarm_newsletter = models.IntegerField()
    alarm_advice = models.IntegerField()
    login_day = models.IntegerField()
    login_time = models.DateTimeField(blank=True, null=True)
    login_from = models.CharField(max_length=45, blank=True, null=True)
    modified_time = models.DateTimeField()
    created_time = models.DateTimeField(blank=True, null=True)
    is_investmenttastes = models.IntegerField(db_column='is_InvestmentTastes')  # Field name made lowercase.
    id_investmenttastes = models.IntegerField(db_column='id_InvestmentTastes')  # Field name made lowercase.
    name_investmenttastes = models.CharField(db_column='name_InvestmentTastes', max_length=45)  # Field name made lowercase.
    p_home_main = models.IntegerField(blank=True, null=True)
    p_home_strategy = models.IntegerField(blank=True, null=True)
    p_real_main = models.IntegerField(blank=True, null=True)
    joinpath = models.CharField(max_length=45, blank=True, null=True)
    purchase_count = models.IntegerField(blank=True, null=True)
    stock_firm = models.IntegerField(blank=True, null=True)
    is_tester = models.IntegerField(blank=True, null=True)
    cnt_view_smartscore = models.IntegerField(blank=True, null=True)
    cnt_limit_kakaoshare = models.IntegerField(blank=True, null=True)
    cnt_view_competition = models.IntegerField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_time = models.DateTimeField(blank=True, null=True)
    referral_id = models.CharField(max_length=45, blank=True, null=True)
    is_follow = models.IntegerField(blank=True, null=True)
    cnt_limit_stocks = models.IntegerField(blank=True, null=True)
    cnt_hsk_event01_follow = models.IntegerField(blank=True, null=True)
    hsk_kakao_share = models.IntegerField(blank=True, null=True)
    app_join_path = models.CharField(max_length=45, blank=True, null=True)
    hsk_created_time = models.DateTimeField(blank=True, null=True)
    hsk_login_time = models.DateTimeField(blank=True, null=True)
    hsk_login_cnt = models.IntegerField(blank=True, null=True)
    hsk_chat_confirm = models.IntegerField(blank=True, null=True)
    hsk_board_confirm = models.IntegerField(blank=True, null=True)
    gived_coupon = models.IntegerField()
    participated_day = models.IntegerField()
    hsk_read_noti = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'users'


class SalesInfoV2(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=300, blank=True, null=True)
    product_id = models.IntegerField(blank=True, null=True)
    product = models.CharField(max_length=45, blank=True, null=True)
    market = models.CharField(max_length=45, blank=True, null=True)
    total = models.FloatField(blank=True, null=True)
    start_time = models.DateTimeField(blank=True, null=True)
    end_time = models.DateTimeField(blank=True, null=True)
    is_expired = models.CharField(max_length=1)
    cnt_purchase = models.DecimalField(max_digits=32, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'sales_info_v2'


class ViewClientInfo(models.Model):
    user_id = models.IntegerField()
    name = models.CharField(max_length=100)
    market = models.CharField(max_length=8)
    purchase_count = models.IntegerField(blank=True, null=True)
    created_time = models.DateTimeField(blank=True, null=True)
    login_1month = models.CharField(db_column='login_1Month', max_length=1)  # Field name made lowercase.
    login_time = models.DateTimeField(blank=True, null=True)
    is_deleted = models.IntegerField(blank=True, null=True)
    deleted_time = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'view_client_info'
