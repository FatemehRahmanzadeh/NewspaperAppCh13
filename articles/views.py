# لاگین شو تا اگه یوزر درستی بودی بتونی تغییر ایجاد کنی
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy
from .models import Article


class ArticleListView(LoginRequiredMixin, ListView):
    """
    برای ایجاد صفحه نمایش لیست مقاله ها

    :model: مدلی که جدول آن در دیتابیس موجود است و جزییات مقاله از فیلدهای آن خوانده می شود
    :template_name: صفحه ای که این ویو در آن رندر می شود!!!
    """
    model = Article
    template_name = 'articles/article_list.html'


class ArticleDetailView(LoginRequiredMixin, DetailView):
    """
    نمایش جزییات هر مقاله

    :model: مدلی که جدول آن در دیتابیس موجود است و جزییات مقاله از فیلدهای آن خوانده می شود
    :template_name: صفحه ای که این ویو در آن رندر می شود!!!
    """
    model = Article
    template_name = 'articles/article_detail.html'


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    ویوی ویرایش مقاله انتخابی را ایجاد می کند

    :model: مدلی که جدول آن در دیتابیس موجود است و جزییات مقاله از فیلدهای آن خوانده می شود
    :template_name: صفحه ای که این ویو در آن رندر می شود!!!
    :fields: فیلدهای قابل ویرایش (منطقی نیست که کاربر آن برای ویرایش در دسترس باشد.)
    """
    model = Article
    fields = ('title', 'body',)
    template_name = 'articles/article_edit.html'

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """
    ویوی حذف مقاله انتخابی را ایجاد می کند

    :model: مدلی که جدول آن در دیتابیس موجود است و جزییات مقاله از فیلدهای آن خوانده می شود
    :template_name: صفحه ای که این ویو در آن رندر می شود!!!
    :success_url: آدرس صفحه ای که بعد موفق بودن حذف کاربر به آن منتقل می شود
    """
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('article_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleCreateView(LoginRequiredMixin, CreateView):
    """
    ایجاد مقاله جدید
    :model: مدلی که جدول آن در دیتابیس موجود است و جزییات مقاله از فیلدهای آن خوانده می شود
    :template_name: صفحه ای که این ویو در آن رندر می شود!!!

    """
    model = Article
    template_name = 'articles/article_new.html'
    # fields = ('title', 'body', 'author',)
    fields = ('title', 'body')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
