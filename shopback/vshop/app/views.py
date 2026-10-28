from django.shortcuts import render

# 1
def home(request):
    menu =[
    {
        "title":"home",
        "url":"http://127.0.0.1:8000/",
    },
    {
        "title":"login",
        "url":"http://127.0.0.1:8000/login",
    },
    {
        "title":"product_list",
        "url":"http://127.0.0.1:8000/product_list/",
    },
    {
        "title":"supermarket",
        "url":"http://127.0.0.1:8000/supermarket",
    },
    {
        "title":"checkout",
        "url":"http://127.0.0.1:8000/checkout",
    },
    {
        "title":"categories",
        "url":"http://127.0.0.1:8000/categories",
    },
    {
        "title":"user",
        "url":"http://127.0.0.1:8000/user",
    },
    ]




    return render(request,'pages/index.html',{"menu":menu})

# 2
def about(request):
    return render (request,"'pages/about.html")
# درباره ما

# 3
def product_list(request):
    return render (request,'pages/product_list.html')
# محصولات پرفروش

# 4
def contanct_use (request):
    return render (request ,"pages/contanct_use.html")
# تماس با ما

# 5
def supermarket(request):
    return render (request,"pages/supermarket.html")
# اخبار

# 6
def login(request):
    return render (request,"pages/login.html")
# ورود کاربر

# 7
def profile(request):
    prof = [
            {
                "title":"orders",
                "url":"http://127.0.0.1:8000/orders",
            },
            {
                "title":"comments",
                "url":"http://127.0.0.1:8000/comments",
            },
            {
                "title":"favorites",
                "url":"http://127.0.0.1:8000/favorites/",
            },
            {
                "title":"addresses",
                "url":"http://127.0.0.1:8000/addresses",
            },
            {
                "title":"user",
                "url":"http://127.0.0.1:8000/user",
            },
            {
                "title":"logout",
                "url":"http://127.0.0.1:8000/logout",
            },

    ]


    return render (request,"pages/profile.html",{"menu":prof})
# پس از ورود کاربر

# 8
def orders(request):
    return render (request ,"pages/orders.html")
# سفارشات

# 9
def comments(request):
    return render (request ,"pages/comments.html")
# کامنت ها

# 10
def favorites(request):
    return render (request,"pages/favorites.html")
# علاقه مندی ها

# 11
def ticketing_modal(request):
    return render (request ,"pages/ticketing_modal.html")
# پشتیبانی

# 12
def checkout(request):
    return render (request ,"pages/checkout.html")
# سبد خرید

# 13
def categories (request):

    cates =[
        {
            "title":"digital",
            "url":"http://127.0.0.1:8000/digital",
        },
        {
            "title":"art_culture",
            "url":"http://127.0.0.1:8000/art_culture",
        },
        {
            "title":"fashion",
            "url":"http://127.0.0.1:8000/fashion/",
        },
        # {
        #     "title":"supermarket",
        #     "url":"http://127.0.0.1:8000/supermarket",
        # },
        # {
        #     "title":"checkout",
        #     "url":"http://127.0.0.1:8000/checkout",
        # },
        # {
        #     "title":"categories",
        #     "url":"http://127.0.0.1:8000/categories",
        # },
        # {
        #     "title":"user",
        #     "url":"http://127.0.0.1:8000/user",
        # },
        ]

    return render (request ,"pages/categories.html",{"menu":cates})
# کتگوری ها

# 14
def  digital(request):
    return render (request ,"pages/digital.html")
# کتگوری دیجیتال

# 15
def art_culture(request):
    return render (request ,"pages/art_culture.html")
#  فرهنگی


# 16
def fashion (request):
    return render (request,"pages/fashion.html")
# لباس و پوشاک

# 17
def addresses (request):
    return render (request ,"pages/addresses.html")
# آدرس های من

# 18
def user (request):
    return render (request,"pages/user.html")
# مشخصات کاربر (بخش تغییر مشخصات)

# 19
def logout (request):
    return render (request,"pages/logout.html")
#  خروج از حساب کاربری

# 20
def rules_and_conditions (request):
    return render (request ,"pages/rules_and_conditions.html")
#  قوانین و شرایط استفاده