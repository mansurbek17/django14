from django.views.generic import *
from django.urls import reverse_lazy
from .models import *
from .forms import *


class HomeTaxi(ListView):
    model = Admin
    template_name = 'index.html'
    context_object_name = 'news'
    extra_context = {'title': 'TAXI TITLE'}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        # qo'shimcha o'zgaruvchilar kerak bo'lsa shu yerda qo'shish mumkin
        return context


class AdminListView(ListView):
    model = Admin
    template_name = 'admin_list.html'
    context_object_name = 'admins'
    extra_context = {"title": "Adminlar Ro'yxati"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class AddAdminView(CreateView):
    model = Admin
    form_class = AdminForm
    template_name = 'add_admin.html'
    success_url = reverse_lazy('admin_list')


class DriverListView(ListView):
    model = Driver
    template_name = 'driver_list.html'
    context_object_name = 'drivers'
    extra_context = {"title": "Driverlar Ro'yxati"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class AddDriverView(CreateView):
    model = Driver
    form_class = DriverForm
    template_name = 'add_driver.html'
    success_url = reverse_lazy('driver_list')


class MijozListView(ListView):
    model = Mijoz
    template_name = 'mijoz_list.html'
    context_object_name = 'mijozlar'
    extra_context = {"title": "Mijozlar Ro'yxati"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class AddMijozView(CreateView):
    model = Mijoz
    form_class = MijozForm
    template_name = 'add_mijoz.html'
    success_url = reverse_lazy('mijoz_list')


class ShartnomaListView(ListView):
    model = Shartnoma
    template_name = 'shartnoma_list.html'
    context_object_name = 'shartnomalar'
    extra_context = {"title": "Shartnomalar Ro'yxati"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class AddShartnomaView(CreateView):
    model = Shartnoma
    form_class = ShartnomaForm
    template_name = 'add_shartnoma.html'
    success_url = reverse_lazy('shartnoma_list')


class TolovListView(ListView):
    model = Tolov
    template_name = 'tolov_list.html'
    context_object_name = 'tolovlar'
    extra_context = {"title": "To'lovlar Ro'yxati"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class AddTolovView(CreateView):
    model = Tolov
    form_class = TolovForm
    template_name = 'add_tolov.html'
    success_url = reverse_lazy('tolov_list')


class CommentListView(ListView):
    model = Cament
    template_name = 'Cament_list.html'
    context_object_name = 'comments'
    extra_context = {"title": "Izohlar"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class AddCommentView(CreateView):
    model = Cament
    form_class = CamentForm
    template_name = 'add_comment.html'
    success_url = reverse_lazy('comment_list')


class StatistikaListView(ListView):
    model = Static
    template_name = 'Static.html'
    context_object_name = 'statistikalar'
    extra_context = {"title": "Statistika"}

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context


class AddStatistikaView(CreateView):
    model = Static
    form_class = StaticForm
    template_name = 'add_statistika.html'
    success_url = reverse_lazy('statistika_list')

class DriverUpdateView(UpdateView):
    model = Driver
    form_class = DriverForm
    template_name = 'update_driver.html'
    success_url = reverse_lazy('driver_list')


class DriverDeleteView(DeleteView):
    model = Driver
    template_name = 'delete_driver.html'
    success_url = reverse_lazy('driver_list')

class UpdateMijozView(UpdateView):
    model = Mijoz
    form_class = MijozForm
    template_name = 'update_mijoz.html'
    success_url = reverse_lazy('mijoz_list')

class DeleteMijozView(DeleteView):
    model = Mijoz
    template_name = 'delete_mijoz.html'
    success_url = reverse_lazy('mijoz_list')

class AdminCreateView(CreateView):
    model = Admin
    form_class = AdminForm
    template_name = 'add_admin.html'
    success_url = reverse_lazy('admin_list')




class ShartnomaUpdateView(UpdateView):
    model = Shartnoma
    form_class = ShartnomaForm
    template_name = 'update_shartnoma.html'
    success_url = reverse_lazy('shartnoma_list')


class ShartnomaDeleteView(DeleteView):
    model = Shartnoma
    template_name = 'delete_shartnoma.html'
    success_url = reverse_lazy('shartnoma_list')
