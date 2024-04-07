from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request,'app/home.html')
def index(request):
    return render(request,'app/index.html')
def tkb(request):
    return render(request,'app/tkb.html')
def tgb(request):
    return render(request,'app/tgb.html')

def gt(request):
    return render(request,'app/gt.html')
def C1(request):
    return render(request, 'app/C1.html')

def C2(request):
    return render(request, 'app/C2.html')

def C3(request):
    return render(request, 'app/C3.html')

def C4(request):
    return render(request, 'app/C4.html')

def C5(request):
    return render(request, 'app/C5.html')

# Định nghĩa hàm cho A1 đến A9
def A1(request):
    return render(request, 'app/A1.html')

def A2(request):
    return render(request, 'app/A2.html')

def A3(request):
    return render(request, 'app/A3.html')

def A4(request):
    return render(request, 'app/A4.html')

def A5(request):
    return render(request, 'app/A5.html')

# Định nghĩa hàm cho B1 đến B10
def B1(request):
    return render(request, 'app/B1.html')

def B2(request):
    return render(request, 'app/B2.html')

def B3(request):
    return render(request, 'app/B3.html')

def B4(request):
    return render(request, 'app/B4.html')

def B5(request):
    return render(request, 'app/B5.html')

def xephang1(request):
    return render(request, 'app/xephang1.html')

def xephang2(request):
    return render(request, 'app/xephang2.html')

def xephang3(request):
    return render(request, 'app/xephang3.html')

def xephang4(request):
    return render(request, 'app/xephang4.html')

def xephang5(request):
    return render(request, 'app/xephang5.html')

def xephang6(request):
    return render(request, 'app/xephang6.html')

def xephang7(request):
    return render(request, 'app/xephang7.html')

def xephang8(request):
    return render(request, 'app/xephang8.html')

def xephang9(request):
    return render(request, 'app/xephang9.html')

def xephang10(request):
    return render(request, 'app/xephang10.html')

def xephang11(request):
    return render(request, 'app/xephang11.html')

def xephang12(request):
    return render(request, 'app/xephang12.html')

def xephang13(request):
    return render(request, 'app/xephang13.html')

def xephang14(request):
    return render(request, 'app/xephang14.html')

def xephang15(request):
    return render(request, 'app/xephang15.html')

def xephang16(request):
    return render(request, 'app/xephang16.html')

def xephang17(request):
    return render(request, 'app/xephang17.html')

def xephang18(request):
    return render(request, 'app/xephang18.html')

def xephang19(request):
    return render(request, 'app/xephang19.html')

def xephang20(request):
    return render(request, 'app/xephang20.html')

def xephang21(request):
    return render(request, 'app/xephang21.html')

def xephang22(request):
    return render(request, 'app/xephang22.html')

def xephang23(request):
    return render(request, 'app/xephang23.html')

def xephang24(request):
    return render(request, 'app/xephang24.html')

def xephang25(request):
    return render(request, 'app/xephang25.html')

def xephang26(request):
    return render(request, 'app/xephang26.html')

def xephang27(request):
    return render(request, 'app/xephang27.html')

def xephang28(request):
    return render(request, 'app/xephang28.html')

def xephang29(request):
    return render(request, 'app/xephang29.html')

def xephang30(request):
    return render(request, 'app/xephang30.html')

def xephang31(request):
    return render(request, 'app/xephang31.html')

def xephang32(request):
    return render(request, 'app/xephang32.html')

def xephang33(request):
    return render(request, 'app/xephang33.html')

def xephang34(request):
    return render(request, 'app/xephang34.html')

def xephang35(request):
    return render(request, 'app/xephang35.html')
from django.shortcuts import render

def generate_a1_view(index):
    def view(request):
        return render(request, f'app/a1_{index}.html')
    return view
for i in range(1, 36):
    locals()[f'a1_{i}'] = generate_a1_view(i)

def generate_a2_view(index):
    def view(request):
        return render(request, f'app/a2_{index}.html')
    return view
for i in range(1, 36):
    locals()[f'a2_{i}'] = generate_a2_view(i)

def generate_a3_view(index):
    def view(request):
        return render(request, f'app/a3_{index}.html')
    return view

for i in range(1, 36):
    locals()[f'a3_{i}'] = generate_a3_view(i)

def generate_c1_view(index):
    def view(request):
        return render(request, f'app/c1_{index}.html')
    return view

for i in range(1, 36):
    locals()[f'c1_{i}'] = generate_c1_view(i)

def generate_c3_view(index):
    def view(request):
        return render(request, f'app/c3_{index}.html')
    return view

for i in range(1, 36):
    locals()[f'c3_{i}'] = generate_c3_view(i)

def generate_c2_view(index):
    def view(request):
        return render(request, f'app/c2_{index}.html')
    return view

for i in range(1, 36):
    locals()[f'c2_{i}'] = generate_c2_view(i)

def generate_b1_view(index):
    def view(request):
        return render(request, f'app/b1_{index}.html')
    return view

for i in range(1, 36):
    locals()[f'b1_{i}'] = generate_b1_view(i)

def generate_b2_view(index):
    def view(request):
        return render(request, f'app/b2_{index}.html')
    return view

for i in range(1, 36):
    locals()[f'b2_{i}'] = generate_b2_view(i)

def generate_b3_view(index):
    def view(request):
        return render(request, f'app/b3_{index}.html')
    return view

for i in range(1, 36):
    locals()[f'b3_{i}'] = generate_b3_view(i)

def login(request):
    # Xử lý dữ liệu đăng nhập ở đây
    return render(request, 'app/login.html')

def base(request):
    # Xử lý dữ liệu đăng nhập ở đây
    return render(request, 'app/base.html')






