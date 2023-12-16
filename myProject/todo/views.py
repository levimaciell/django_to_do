from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from todo.serializers import TodoSerializer
from todo.models import Todo

# Create your views here.

# Todo.objects.create(task = 'Olá, isso é um mock! 3')
# Todo.objects.create(Todo(2, 'Olá, isso é um mock!'))
# Todo.objects.create(Todo(13, 'Olá, isso é um mock!'))


@api_view(['GET', 'POST'])
def todo_endpoint(request):
    if request.method == 'GET':
        return todo_get(request)
    
    elif request.method == 'POST':
        return todo_post(request)
    

@api_view(['PUT', 'DELETE'])
def todo_endpoint_id(request, id):
    if request.method == 'PUT':
        return todo_update(request, id)
    elif request.method == 'DELETE':
        return todo_delete(request, id)
    

def todo_get(request):
    
    serializer = TodoSerializer(Todo.objects.all(), many = True)
    return Response(serializer.data)


def todo_post(request):

    serializer = TodoSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)


def todo_update(request, id):
    
    try:
        todo = Todo.objects.get(id=id)

    except Todo.DoesNotExist:
        return Response({'detail': f'Todo with id {id} not found'}, status = status.HTTP_404_NOT_FOUND)
    
    #Serializer com instância todo: Update. Sem: criação
    serializer = TodoSerializer(todo, request.data)

    if serializer.is_valid():

        serializer.save()
        return Response(serializer.data, status = status.HTTP_200_OK)
    
    return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)

def todo_delete(request, id):
    try:
        todo = Todo.objects.get(id = id)
        todo.delete()
        return Response(status=status.HTTP_200_OK)

    except Todo.DoesNotExist: 
        return Response({'details': f'Todo with id {id} not found'}, status=status.HTTP_404_NOT_FOUND)
