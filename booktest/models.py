from django.db import models

# Create your models here.
# 自定义模型管理器类
class BookInfoManager(models.Manager):
    # 作用
    # 1. 改变原有查询的结果集
    def all(self):
        books = super().all().filter(is_delete = False)
        return books
    # 2. 封装方法（用于操作模型类对应的数据表）
    def create_book(self, title, pub_date):
        model_cls = self.model
        book = model_cls(
            btitle = title,
            bpub_date = pub_date
        )
        book.save()

class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='图书标题')
    bpub_date = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')

    books = BookInfoManager()


    class Meta:
        # 指定表名，若不指定表名，默认为booktest_bookinfo
        db_table = 'tb_books'
        verbose_name = '图书'
        verbose_name_plural = verbose_name

#     重写str方法
    def __str__(self):
        return self.btitle

    def pub_date(self):
        return self.bpub_date.strftime('%Y年%m月%d日')

    pub_date.short_description = '发布日期'
    pub_date.admin_order_field = 'bpub_date'
    image = models.ImageField(upload_to='booktest', verbose_name='图片',null = True)


class HeroInfo(models.Model):
    GENDER_CHICES = (
        (0,'男'),
        (1,'女')
    )
    hname = models.CharField(max_length=20, verbose_name='英雄名称')
    hgender = models.SmallIntegerField(choices=GENDER_CHICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, verbose_name='描述信息')
    is_delete = models.BooleanField(default=False, verbose_name='删除标记')
    # 添加外键关联属性，生成的表的名称为hbook_id
    # on_delete=models.CASCADE 当主表被删除时，所关联的外键也会被删除
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE, verbose_name='所属图书')

    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname

    def read(self):
        return self.hbook.bread

    read.short_description = '阅读量'









