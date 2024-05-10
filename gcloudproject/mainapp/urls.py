from django.urls import path
from . import views

app_name = 'mainapp'
urlpatterns = [
    path("",views.home,name="home"),
    path("temp_view/<int:template_card_id>/",views.temp_view,name="temp_view"),
    path('viewmore',views.viewMore,name="viewMore"),
    # path("morenormal",views.moreNormal,name="morenormal"),
    # path("morepremium",views.morePremium,name="morepremium"),
    path('pay/<int:template_id>/',views.pay,name='pay'),
    path("coupen/<int:id>/",views.coupen,name='coupen'),
    path("delcoupen/<int:template_id>/",views.delcoupen,name='delcoupen'),
    path("checkout/<int:id>/",views.checkout,name='checkout'),
    path("success/",views.success,name="success"),
    path('failed/',views.paymentfailed,name="failed"),
    path('somethingwentwrong/',views.somethingwentwrong,name="somethingwentwrong"),
    path('privacypolicy',views.Privacypolicy,name="privacypolicy"),
    path('about',views.about,name="about"),

    path('get_states/',views.get_states,name="get_states"),
    path('get_cities/',views.get_cities,name="get_cities"),

    # path('showPaymentDeatil',views.showPaymentDetail,name="showPaymentDeatil"),

]