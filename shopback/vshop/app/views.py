from django.shortcuts import render

# 1
def home(request):
    return render(request,'pages/index.html')

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
    return render (request,"pages/profile.html")
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
    return render (request ,"pages/categories.html")
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