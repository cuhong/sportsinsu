import uuid

from django.db import models


class Event(models.Model):
    class Meta:
        verbose_name = '행사'
        verbose_name_plural = verbose_name
        ordering = ('-register_at',)

    id = models.UUIDField(default=uuid.uuid4, null=False, blank=False, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=300, null=False, blank=False, unique=True, verbose_name='행사명')
    register_at = models.DateTimeField(auto_now_add=True, verbose_name='생성일')
    main_image = models.ImageField(null=False, blank=False, verbose_name='행사 대표 이미지')
    event_start = models.DateTimeField(null=False, blank=False, verbose_name='행사 시작일시')
    event_end = models.DateTimeField(null=False, blank=False, verbose_name='행사 종료일시')
    insu_rgst_start = models.DateTimeField(null=False, blank=False, verbose_name='보험가입 시작일시')
    insu_rgst_end = models.DateTimeField(null=False, blank=False, verbose_name='보험가입 종료일시')
    description = models.TextField(null=False, blank=False, verbose_name='행사설명')
    attendants = models.ManyToManyField('event.Attendant', through='event.EventAttendantThrough')


class EventAttendantThrough(models.Model):
    event = models.ForeignKey(Event, null=False, blank=False, on_delete=models.PROTECT, verbose_name='이벤트')
    attendant = models.ForeignKey('event.Attendant', null=False, blank=False, on_delete=models.PROTECT,
                                  verbose_name='참가자')


class Attendant(models.Model):
    class Meta:
        verbose_name = '참가자'
        verbose_name_plural = verbose_name

    id = models.UUIDField(default=uuid.uuid4, null=False, blank=False, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='성명')
    cellphone = models.CharField(max_length=11, null=False, blank=False, verbose_name='휴대전화')
    birthdate = models.DateField(null=True, blank=True, verbose_name='생년월일')
