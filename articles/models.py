from django.conf import settings
from django.contrib.auth import get_user_model  # مدل یوزری را بر میگرداند که در حال حاضر استفاده می شود
from django.db import models
from django.urls import reverse


class Article(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
         از آنجا که در آدرس یو آر ال یک پرایمری کی برای دسترسی به آبجکت وارد می کنیم،
          این متد براساس آیدی هر آبجکت یک یو آر ال یکتا ایجاد می کند که دسترسی به آن را در دیتابیس فراهم می کند.

        :return: یک یوآر ال یکتا به ازای هر آبجکت
        """
        return reverse('article_detail', args=[str(self.id)])
