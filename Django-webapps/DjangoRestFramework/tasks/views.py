from django.shortcuts import render
from tasks.models import Tasks,State
from tasks.serializers import TaskSerializer,StateSerializer # convert datbase objects to JSON
from django.http.response import JsonResponse # to send json response
from rest_framework.parsers import JSONParser # to parse json data in POST requests
from rest_framework import status # for http status code
from rest_framework.decorators import api_view

# Create your views here.
# Create your views here.
@api_view(['GET','POST'])
def task_list(request):
    if request.method =='GET':
        tasks = Tasks.objects.all() # fetch all users from the database

        tasks_serializer = TaskSerializer(tasks,many=True) # serialize them into json
        return JsonResponse(tasks_serializer.data,safe =False)   # return the serialized data as JSON
    
    elif request.method =='POST':

        tasks_data = JSONParser().parse(request) #parse incoming data
        tasks_serializer =TaskSerializer(data=tasks_data) # deserialize data into a user object
        if tasks_serializer.is_valid():
            tasks_serializer.save() # save user to database  
            return JsonResponse(tasks_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(tasks_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
def state_list(request):
    if request.method == 'GET':
        states = State.objects.all()  #fetch all the states from database
        state_serializer = StateSerializer(states, many =True)  
        return JsonResponse(state_serializer.data, safe =False)  # return the serialized data as Json
    
    elif request.method =='POST':
        state_data =JSONParser().parse(request) # parse incoming data
        state_serializer = StateSerializer(data=state_data) # deserialize data into a user object
        if state_serializer.is_valid():
            state_serializer.save()
            return JsonResponse(state_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(state_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    
    





@api_view(['GET','PUT','DELETE'])
def task_details(request,pk):
    try:
        task = Tasks.objects.get(pk=pk)
    except:
        return JsonResponse({'message':'User does not exist'},
                             status = status.HTTP_400_BAD_REQUEST)
                    
    if request.method =='GET':
        tasks_serializer= TaskSerializer(task)
        return JsonResponse(tasks_serializer.data)
    
    elif request.method =='PUT':
        tasks_data = JSONParser().parse(request)
        tasks_serializer = TaskSerializer(task,data= tasks_data)
        if tasks_serializer.is_valid():
            tasks_serializer.save()
            return JsonResponse(tasks_serializer.data)
    
    elif request.method == 'DELETE':
        task.delete()
        return JsonResponse({'msg':'User deleted successfully'},
                            status =status.HTTP_204_NO_CONTENT)

            
