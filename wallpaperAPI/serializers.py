from rest_framework import serializers
from .models import Rank, TopicList, Homepage, Guess,Category

'''
热门壁纸
'''


class RankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rank
        fields = '__all__'


'''
topic list
'''


class TopicListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicList
        fields = '__all__'


'''
最新壁纸hoempage
'''


class HomepageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Homepage
        fields = '__all__'


'''
猜你喜欢
'''


class GuessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Guess
        fields = '__all__'

'''
获取分类
'''
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__'
