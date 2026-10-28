from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from json import loads

# Create your views here.
@method_decorator(csrf_exempt, name='dispatch')
class Addition_View(View):
    def post(self,request):
        request_body = request.body
        form_data = loads(request_body)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 + n2

        print(request_body)

        data ={
            "Sum" : result

        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class Subtraction_View(View):
    def post(self,request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        difference = n1 - n2

        data ={
            "Difference" : difference

        }
        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class Multiplication_View(View):
    def post(self,request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 * n2

        data = {
            "Result" :result
        }
        return JsonResponse(data)
    
@method_decorator(csrf_exempt, name='dispatch')
class Division_View(View):
    def post(self,request):
        data = request.body
        form_dta = loads(data)
        n1 =form_dta.get('num1')
        n2 =form_dta.get('num2')
        result = n1 / n2

        data = {
            "Result" :result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class Modulus_View(View):
    def post(self,request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('num1')
        n2 = form_data.get('num2')
        result = n1 % n2

        data = {
            "Result" :result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class Percentage_View(View):
    def post(self,request):
        data = request.body
        form_data = loads(data)
        n1 = form_data.get('obtained_marks')
        n2 = form_data.get('total_marks')
        result = (n1/n2) * 100

        data = {
            "Percentage" : result
        }
        return JsonResponse(data)
@method_decorator(csrf_exempt, name='dispatch')
class BMI_View(View):
    def post(self,request):
        data = request.body
        form_data = loads(data)
        w = form_data.get('weight')
        h = form_data.get('height')
        result = w/ (h/100) ** 2

        data = {
            "BMI" : result
        }
        return JsonResponse(data)

@method_decorator(csrf_exempt, name='dispatch')
class Age_Calculator_View(View):
    def post(self,request):
        data = request.body
        form_data = loads(data)
        Birth_year = form_data.get('birth_year')
        Current_year = form_data.get('current_year')
        age = Current_year - Birth_year

        data = {
            "Age" : age
        }
        return JsonResponse(data)
@method_decorator(csrf_exempt, name='dispatch')
class Interest_Calculator_View(View):
    def post(self,request):
        data = request.body
        form_data = loads(data)
        Principal = form_data.get('principal')
        Rate = form_data.get('rate')
        Time = form_data.get('time')
        interest = (Principal * Rate * Time) / 100

        data = {
            "Principal" : Principal,
            "Rate"      : Rate,
            "Time"      : Time,
            "SImple_Interest"  : interest
        }
        return JsonResponse(data)
@method_decorator(csrf_exempt,name='dispatch')
class Electricity_Calculator_View(View):
    def post(self,request):
        data = request.body
        form_data = loads(data)
        Units = form_data.get('units')
        Rate = form_data.get('rate')
        Bill = Units * Rate

        data = {
            "Units"   : Units,
            "Rate"    : Rate,
            "Bill"    : Bill
        }
        return JsonResponse(data)


