# coding:utf-8
from .models import Rank, TopicList, Homepage, Guess,Category
from .serializers import RankSerializer, TopicListSerializer, HomepageSerializer, GuessSerializer,CategorySerializer
from .utilTool import ReadOnlyOneObjectViewSet

'''
热门壁纸
'''


class RankViewSet(ReadOnlyOneObjectViewSet):
    queryset = Rank.objects.filter(active_status='1')[:1]
    serializer_class = RankSerializer


'''
topic list
'''


class TopicListViewSet(ReadOnlyOneObjectViewSet):
    queryset = TopicList.objects.filter(active_status='1')[:1]
    serializer_class = TopicListSerializer


'''
最新壁纸hoempage
'''


class HomepageViewSet(ReadOnlyOneObjectViewSet):
    queryset = Homepage.objects.filter(active_status='1')[:1]
    serializer_class = HomepageSerializer


'''
猜你喜欢
'''


class GuessViewSet(ReadOnlyOneObjectViewSet):
    queryset = Guess.objects.filter(active_status='1')[:1]
    serializer_class = GuessSerializer


'''
获取分类
'''

class CategoryViewSet(ReadOnlyOneObjectViewSet):
    queryset = Category.objects.filter(active_status='1')[:1]
    serializer_class = CategorySerializer
