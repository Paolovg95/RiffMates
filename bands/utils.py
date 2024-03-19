# Random alphanumeric ID generator
import secrets
import string
# To create Slugs from title
from django.utils.text import slugify

def slugify_musician(instance, save=False, new_slug=None):
    slug = slugify(instance.first_name) + "-" + slugify(instance.last_name) + "-" + str(instance.id)
    instance.slug = slug
    if save:
        instance.save()
    return slug

def get_items_per_page(request):
# Determine how many items to show per page, disallowing <1 or >50
    items_per_page = int(request.GET.get("items_per_page", 10))
    if items_per_page < 1:
        items_per_page = 10
    if items_per_page > 50:
        items_per_page = 50

    return items_per_page

def get_page_num(request, paginator):
    # Get current page number for Pagination, using reasonable defaults
    page_num = int(request.GET.get("page", 1))

    if page_num < 1:
        page_num = 1
    elif page_num > paginator.num_pages:
        page_num = paginator.num_pages

    return page_num
