from idlelib.textview import ViewWindow

from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeTaxi.as_view(), name='home'),

    # Admin
    path('admin_list/', views.AdminListView.as_view(), name='admin_list'),
    path('add_admin/', views.AddAdminView.as_view(), name='add_admin'),

    # Driver
    path('driver_list/', views.DriverListView.as_view(), name='driver_list'),
    path('add_driver/', views.AddDriverView.as_view(), name='add_driver'),
    path('driver/update/<int:pk>/', views.DriverUpdateView.as_view(), name='update_driver'),
    path('driver/delete/<int:pk>/', views.DriverDeleteView.as_view(), name='delete_driver'),


    # Mijoz
    path('mijoz_list/', views.MijozListView.as_view(), name='mijoz_list'),
    path('add_mijoz/', views.AddMijozView.as_view(), name='add_mijoz'),
    path('update_mijoz/<int:pk>/', views.UpdateMijozView.as_view(), name='update_mijoz'),
    path('delete_mijoz/<int:pk>/', views.DeleteMijozView.as_view(), name='delete_mijoz'),

    # Shartnoma
    path('shartnoma_list/', views.ShartnomaListView.as_view(), name='shartnoma_list'),
    path('add_shartnoma/', views.AddShartnomaView.as_view(), name='add_shartnoma'),
    path('shartnoma/update/<int:pk>/', views.ShartnomaUpdateView.as_view(), name='update_shartnoma'),  # bu qator kerak
    path('shartnoma/delete/<int:pk>/', views.ShartnomaDeleteView.as_view(), name='delete_shartnoma'),

    # Tolov
    path('tolov_list/', views.TolovListView.as_view(), name='tolov_list'),
    path('add_tolov/', views.AddTolovView.as_view(), name='add_tolov'),

    # Comment (Cament)
    path('comment_list/', views.CommentListView.as_view(), name='comment_list'),
    path('add_comment/', views.AddCommentView.as_view(), name='add_comment'),

    # # Statistika
    path('Static/', views.StatistikaListView.as_view(), name='Static'),
    # path('add_statistika/', views.AddStatistikaView.as_view(), name='add_statistika'),
]
