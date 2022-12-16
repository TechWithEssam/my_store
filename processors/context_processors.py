from users.models import Profile
from store.models import Brand, Category, Product


def profile_context_processors_view(request) :
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        context = {"profile":profile}
        return context
    return {}

def category_product_view(request) :
    qs = Category.objects.filter().order_by("?")[:10]
    context = {
        "catrogrys":qs
    }
    return context

def brand_product_view(request) :
    qs = Product.objects.filter().order_by("?")[:10]
    context = {
        "brands":qs
    }
    return context