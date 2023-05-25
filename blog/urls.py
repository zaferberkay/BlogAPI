from django.urls import path
from rest_framework.routers import DefaultRouter
from blog.views import Category_view, Post_view

router = DefaultRouter()
router.register('category', Category_view)
router.register('post', Post_view)

urlpatterns = router.urls

