from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        'title': 'GeekShop',
        'header': 'GeekShop Store',
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'GeekShop - Каталог',
        'header': 'GeekShop',
        'products': [
            {
                'title': 'Худи черного цвета с монограммами adidas Originals',
                'description': 'Мягкая ткань для свитшотов. Стиль и комфорт – это образ жизни.',
                'image': 'vendor/img/products/Adidas-hoodie.png',
                'price': 6090
            },
            {
                'title': 'Синяя куртка The North Face',
                'description': 'Гладкая ткань. Водонепроницаемое покрытие. Легкий и теплый пуховый наполнитель.',
                'image': 'vendor/img/products/Blue-jacket-The-North-Face.png',
                'price': 23725
            },
            {
                'title': 'Коричневый спортивный oversized-топ ASOS DESIGN',
                'description': 'Материал с плюшевой текстурой. Удобный и мягкий.',
                'image': 'vendor/img/products/Brown-sports-oversized-top-ASOS-DESIGN.png',
                'price': 3390
            },
            {
                'title': 'Черный рюкзак Nike Heritage',
                'description': 'Плотная ткань. Легкий материал.',
                'image': 'vendor/img/products/Black-Nike-Heritage-backpack.png',
                'price': 2340
            },
            {
                'title': 'Черные туфли на платформе с 3 парами люверсов Dr Martens 1461 Bex',
                'description': 'Гладкий кожаный верх. Натуральный материал.',
                'image': 'vendor/img/products/Black-Dr-Martens-shoes.png',
                'price': 13590
            },
            {
                'title': 'Темно-синие широкие строгие брюки ASOS DESIGN',
                'description': 'Легкая эластичная ткань сирсакер Фактурная ткань.',
                'image': 'vendor/img/products/Dark-blue-wide-leg-ASOs-DESIGN-trousers.png',
                'price': 2890
            }
        ]
    }
    return render(request, 'products/products.html', context)
