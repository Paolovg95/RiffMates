from django.urls import reverse_lazy

from ninja import Router, ModelSchema
from django.shortcuts import get_object_or_404
from .models import Promoter

router = Router()

class PromoterSchema(ModelSchema):
    # url:str

    class Meta:
        model = Promoter
        fields = ["full_name", "famous_for", "common_name"]

    # @staticmethod
    # def resolve_url(obj):
    #     url = reverse_lazy("api-1.0.0:index")
    #     return str(url)

@router.get("/promoters/",response=list[PromoterSchema])
def promoters(request):
    return Promoter.objects.all()

@router.get("/promoter/{promoter_id}/", response=PromoterSchema, url_name="")
def promoter(request, promoter_id):
    promoter = get_object_or_404(Promoter, id=promoter_id)
    return promoter
