from django.shortcuts import HttpResponse, render, redirect
from datetime import datetime
from django.views.generic import ListView, CreateView, View
from product.constans import PAGINATION_LIMIT
from product.forms import ProductCreateForm
from product.models import Product


# Create your views here.


# def hello_view(request):
#     if request.method == 'GET':
#         return HttpResponse("Hello! It's my project")
class HelloCBV(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse("Hello! It's my project")


# def gb_view(request):
#     if request.method == 'GET':
#         return HttpResponse('Goodby user!')

class GoodbyCBV(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Goodby user!')


# def now_date_view(request):
#     if request.method == 'GET':
#         current_time = datetime.now()
#         return HttpResponse(current_time)

class NowdateCBV(View):
    def get(self, request, *args, **kwargs):
        current_time = datetime.now()
        return HttpResponse(current_time)


# def main_view(request):
#     if request.method == 'GET':
#         return render(request, 'layouts/index.html')

class MainCBV(ListView):
    model = Product
    template_name = 'layouts/index.html'


# def products_view(request):
#     if request.method == 'GET':
#         products = Product.objects.all()
#         search = request.GET.get('search')
#         page = int(request.GET.get('page', 1))
#
#         '''starts_with, ends_with, icontains'''
#
#         if search:
#             products = products.filter(name__icontains=search) | products.filter(description__icontains=search)
#
#         max_page = products.__len__() / PAGINATION_LIMIT
#         max_page = round(max_page) + 1 if round(max_page) < max_page else round(max_page)
#
#         '''products splice'''
#         products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]
#
#         context = {
#             'products': products,
#             'user': request.user,
#             'pages': range(1, max_page + 1)
#         }
#         return render(request, 'products/products.html', context=context)

class ProductsCBV(ListView):
    model = Product
    template_name = 'products/products.html'

    def get(self, request, **kwargs):
        products = self.model.objects.all()
        search = request.GET.get('search')
        page = int(request.GET.get('page', 1))

        '''starts_with, ends_with, icontains'''

        if search:
            products = products.filter(name__icontains=search) | products.filter(description__icontains=search)

        max_page = products.__len__() / PAGINATION_LIMIT
        max_page = round(max_page) + 1 if round(max_page) < max_page else round(max_page)

        '''products splice'''
        products = products[PAGINATION_LIMIT * (page - 1): PAGINATION_LIMIT * page]

        context = {
            'products': products,
            'user': request.user,
            'pages': range(1, max_page + 1)
        }
        return render(request, self.template_name, context=context)


# def product_create_view(request):
#     if request.method == 'GET':
#         context = {
#             'form': ProductCreateForm
#         }
#         return render(request, 'products/create.html', context=context)
#
#     if request.method == 'POST':
#         form = ProductCreateForm(request.POST, request.FILES)
#
#         if form.is_valid():
#             Product.objects.create(
#                 name=form.cleaned_data.get('name'),
#                 description=form.cleaned_data.get('description'),
#                 price=form.cleaned_data.get('price'),
#                 image=form.cleaned_data.get('image')
#             )
#             return redirect('/products/')
#         return render(request, 'products/create.html', context={
#             'form': form
#         })
#

class ProductCreateCBV(ListView, CreateView):
    model = Product
    template_name = 'products/create.html'

    def get(self, request, **kwargs):
        context = {
            'form': ProductCreateForm
        }
        return render(request, self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = ProductCreateForm(request.POST, request.FILES)

        if form.is_valid():
            self.model.objects.create(
                name=form.cleaned_data.get('name'),
                description=form.cleaned_data.get('description'),
                price=form.cleaned_data.get('price'),
                image=form.cleaned_data.get('image')
            )
            return redirect('/products/')
        return render(request, self.template_name, context={
            'form': form
        })


# def products_detail_view(request, id):
#     if request.method == 'GET':
#         product = Product.objects.get(id=id)
#         context = {
#             'product': product,
#             'review': product.review_set.all(),
#             'user': request.user
#         }
#         return render(request, 'products/detail.html', context=context)


class ProductDetailCBV(ListView):
    model = Product
    template_name = 'products/detail.html'

    def get(self, request, **kwargs):
        product = self.model.objects.get(id=id)
        context = {
            'product': product,
            'review': product.review_set.all(),
            'user': request.user
        }
        return render(request, self.template_name, context=context)
