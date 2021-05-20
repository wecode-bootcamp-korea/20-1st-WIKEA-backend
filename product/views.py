import json

from random import uniform

from django.views           import View
from django.http            import JsonResponse
from django.core.exceptions import ValidationError

from product.models         import Product, Category, SubCategory, Comment
from user.utils             import authorize
from user.models            import User
class CommentView(View):
    @authorize
    def post(self, request):
        try:
            data    = json.loads(request.body)
            product = Product.objects.get(id=int(data['product']))
            user    = request.user

            Comment.objects.create(
                user=user,
                product=product,
                rating=data['star'],
                content=data['content']
            )
            return JsonResponse({'massage':'success'},status=200)

        except KeyError:
            return JsonResponse({'massage':'keyerror'},status=404)

    def get(self, request):
        product_id = request.GET.get('product')

        if not Product.objects.filter(id=product_id).exists():
            return JsonResponse({'massage':'fail'},status=404)

        product = Product.objects.get(id=product_id)
        if product:
            comments = Comment.objects.filter(product=product)

            result = [{
                        'rating'  : comment.rating,
                        'content' : comment.content,
                     } for comment in comments]
            return JsonResponse({'comment':result},status=200)

class RecommendedView(View):
    def get(self, request):
        RECOMMENDED_COUNT = 10
        products = Product.objects.all().order_by('-stock')[:RECOMMENDED_COUNT]
        
        recommended_product= [
                {
                    'is_new'           : product.is_new,
                    'english_name'     : product.english_name,
                    'korean_name'      : product.korean_name,
                    'price'            : product.price,
                    'sub_category_name': product.sub_category.korean_name,
                    'star'             : uniform(1.0,5.0),
                    'image'            : [
                            image.url
                            for image in product.image.all()[:2]]
                }
                for product in products]
        
        return JsonResponse({'recommended_product':recommended_product}, status=200)

class CategoryView(View):
    def get(self, request):
        category_list     = []
        categorys         = Category.objects.all()

        category_list = [
            {
                'id'          : category.id,
                'korean_name' : category.korean_name,
                'english_name': category.english_name,
                'sub_category': [
                    {
                    'id'          : sub_category.id,
                    'korean_name' : sub_category.korean_name,
                    'english_name': sub_category.english_name
                    }
                for sub_category in SubCategory.objects.filter(category=category)]
            }
            for category in categorys]

        return JsonResponse({'category':category_list}, status=200)