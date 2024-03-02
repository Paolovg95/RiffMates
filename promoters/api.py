from ninja import Router, ModelSchema
from .models import Promoter

router = Router()

class PromoterSchema(ModelSchema):
    class Meta:
        model = Promoter
        fields = ["full_name", "famous_for", "common_name"]

@router.get("/",response=list[PromoterSchema])
def promoters(request):
    return Promoter.objects.all()
