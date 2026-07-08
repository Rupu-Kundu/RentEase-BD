from django.contrib import admin
from django.urls import path, include  # নিশ্চিত করুন 'include' ইমপোর্ট করা আছে

urlpatterns = [
    path('admin/', admin.site.urls),    # জ্যাঙ্গোর ডিফল্ট অ্যাডমিন প্যানেল
    path('', include('home.urls')),     # আমাদের অ্যাপের ইউআরএল রুট
]