from django.contrib import admin

# Register your models here.
from .models import Rank, TopicList, Homepage, Guess,Category


@admin.register(Rank)
class RankAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'start', 'length', 'model', 'rank_id', 'active_status')
    fields = ('type', 'start', 'length', 'model', 'rank_id', 'address', 'active_status')


@admin.register(TopicList)
class TopicListAdmin(admin.ModelAdmin):
    list_display = ('id', 'num','type', 'offset', 'ordertype', 'active_status')
    fields = ('type','num', 'offset', 'ordertype', 'active_status', 'address')


@admin.register(Homepage)
class HompageAdmin(admin.ModelAdmin):
    list_display = ('id', 'length', 'page', 'address', 'active_status')
    fields = ('length', 'page', 'address', 'active_status')


@admin.register(Guess)
class GuessAdmin(admin.ModelAdmin):
    list_display = ('id', 'length', 'imei', 'address', 'active_status')
    fields = ('length', 'imei', 'address', 'active_status')
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'length','total','hot','offset','address', 'active_status')
    fields = ('length','total','hot','offset','address', 'active_status')