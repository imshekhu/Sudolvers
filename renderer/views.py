from django.shortcuts import render
from django.views import View
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.http import HttpResponse
import json
from .sudoku import start

@method_decorator(csrf_exempt, name='dispatch')
class HomeView(View):
    #get The sudoku board in Render.
    
    def get(self, request):
        template ='sudokuboard.html'
        return TemplateResponse(request,template)
    
    
    def post(self, request):
        # print(type(request.body))
        data = json.loads (request.body)
        solved_board = start(data)
        return  HttpResponse(json.dumps(solved_board), content_type="application/json")

@method_decorator(csrf_exempt, name='dispatch')
class OwnBoardView(View):
    #get The sudoku board in Render.
    
    def get(self, request):
        template ='clearboard.html'
        return TemplateResponse(request,template)
        
    def post(self, request):
        # print(type(request.body))
        data = json.loads (request.body)
        solved_board = start(data)
        return  HttpResponse(json.dumps(solved_board), content_type="application/json")
