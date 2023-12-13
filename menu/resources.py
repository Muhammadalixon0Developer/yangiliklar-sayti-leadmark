from import_export import resources
from menu.models import News


class NewsResources(resources.ModelResource):
    class Meta:
        model = News
        # fields = ['cat_id', 'id', 'title'] # modeldagi shu fieldlarni oladi
        exclude = ['id', 'content'] # bu holatda idni olmaydi qolganini o'ladi