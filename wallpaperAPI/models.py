from django.db import models

# Create your models here.
'''
热门壁纸
'''


class Rank(models.Model):
    ACTIVE_STATUS = (
        ('1', '激活'),
        ('0', '去激活'),
    )
    BEFORE_AFTER = (
        ('1', '前取'),
        ('-1', '后取'),
    )
    IMAGE_TYPE = (
        ('1', '静态图片'),
        ('2', '动态图片'),
        ('0', '全部'),
    )
    type = models.CharField('图片类型', choices=IMAGE_TYPE, max_length=2, blank=True, null=True)  # 1静态图片，2动态图片，0全部
    start = models.IntegerField('起始图片id', blank=True, null=True)  # 列表起始图片id，默认最新的id
    length = models.IntegerField('获取图片数量', blank=True, null=True)  # 要获取的图片数量,默认24张,范围[1,50],超出范围自动转换为默认值
    model = models.CharField('前/后取', choices=BEFORE_AFTER, max_length=2, blank=True,
                             null=True)  # 1:标示向前取length张;-1:表示向后取length张
    rank_id = models.IntegerField('缓存排行ID', blank=True, null=True)  # 当前客户端上缓存的排行快照的ID
    active_status = models.CharField(max_length=2, choices=ACTIVE_STATUS, )
    address = models.CharField('链接地址', max_length=500)

    class Meta:
        ordering = ['active_status']


class TopicList(models.Model):
    ACTIVE_STATUS = (
        ('1', '激活'),
        ('0', '去激活'),
    )
    IMAGE_TYPE = (
        (1, '只获取有壁纸的专题'),
        (2, '只获取有link的专题'),
        (3, '获取所有类型专题'),
    )
    ORDER_TYPE = (
        (1, '热度值倒序（desc）'),
        (2, '热度值升序（asc）')
    )
    num = models.IntegerField('获取topic数量', blank=True, null=True)
    type = models.IntegerField('图片类型', choices=IMAGE_TYPE, blank=True, null=True)
    offset = models.IntegerField('偏移量', blank=True, null=True)
    ordertype = models.IntegerField('排序方式', choices=ORDER_TYPE, blank=True, null=True)
    active_status = models.CharField(max_length=2, choices=ACTIVE_STATUS, )
    address = models.CharField('链接地址', max_length=500)

    class Meta:
        ordering = ['active_status']


'''
最新壁纸hoempage
'''


class Homepage(models.Model):
    ACTIVE_STATUS = (
        ('1', '激活'),
        ('0', '去激活'),
    )
    length = models.IntegerField('获取图片数量', blank=True, null=True)  # 要获取的图片数量,默认24张,范围[1,50],超出范围自动转换为默认值
    page = models.IntegerField('页数', blank=True, null=True)  # 获取页数
    active_status = models.CharField(max_length=2, choices=ACTIVE_STATUS, )
    address = models.CharField('链接地址', max_length=500)

    class Meta:
        ordering = ['active_status']


'''
猜你喜欢
'''


class Guess(models.Model):
    ACTIVE_STATUS = (
        ('1', '激活'),
        ('0', '去激活'),
    )
    length = models.IntegerField('获取图片数量', blank=True, null=True)  # 要获取的图片数量,默认24张,范围[1,50],超出范围自动转换为默认值
    imei = models.CharField('imei', max_length=18)
    active_status = models.CharField(max_length=2, choices=ACTIVE_STATUS, )
    address = models.CharField('链接地址', max_length=500)

    class Meta:
        ordering = ['active_status']


'''
壁纸分类
'''


class Category(models.Model):
    ACTIVE_STATUS = (
        ('1', '激活'),
        ('0', '去激活'),
    )
    TOTAL = (
        (1, '是'),
        (0, '否')
    )
    total = models.IntegerField('获取全部', choices=TOTAL, blank=True, null=True)  # 是否获取全部 1-是 0-否
    hot = models.IntegerField('获取热门', choices=TOTAL, blank=True, null=True)  # 是否获取热门类型 1-是 0--否
    length = models.IntegerField('获取类别个数', blank=True, null=True)  # 获取图片类别个数，默认12，超出总个数则返回全部
    offset = models.IntegerField('偏移量', blank=True, null=True)  # 获取偏移量，类似翻页
    active_status = models.CharField(max_length=2, choices=ACTIVE_STATUS, )
    address = models.CharField('链接地址', max_length=500)

    class Meta:
        ordering = ['active_status']
