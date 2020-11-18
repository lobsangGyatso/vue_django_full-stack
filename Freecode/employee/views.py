from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ArticleSerializer,ReporterSerializer,PublicationSerialzation
from .models import Reporter,Article,Publication
from rest_framework.response import Response
from rest_framework.parsers import FormParser, MultiPartParser,JSONParser
# Create your views here.


class EmployeeSet(APIView):
    
    def get(self,request):
        reporter = Reporter.objects.get(id=1)
        print(reporter)
        # for i in reporter:
        #     print(i.id)
        # article = Article.objects.filter(Reporter=reporter)
        # print(article[0].headline)
        # aa=article[0]
        # now i want to filter the publication try to find the does reporter reported on 
        publication = Publication.objects.filter(article=7)
        publication=publication[0]
        print(publication.article)
        # obj=[]
        # for i in publication:
        #     print(i.article.filter(Reporter=reporter))
        # for i in publication:
        #     if i.article.Reporter == reporter:
        #         print("yesssss")
            # if i.article.objects.filter(Reporter= reporter):
            #     print("yues")
            #     break
            # else:
            #     print("no")
        
    # def get_object(self,id):
    #     odj= Article.objects.get(id=id)
    #     if obj.exists():
    #         return obj
    #     else:
    #         return "not found"
    # def get(self,request):
    #     obj=Article.objects.all()
    #     # article = Article.objects.filter(Reporter = obj, headline= "about nepal")
    #     # print(article)
    #     serialized = ArticleSerializer(obj, many = True)
    #     return Response(serialized.data,status=200)
    # def post(self,request):
    #    print("we athe best")
    #    headline = request.data['headline']
    #    image = request.data['picture']
    #    print("ffff",image)
    #    data ={
    #        'headline':request.data['headline'],
    #        'picture': request.FILES['picture'],
    #        'Reporter':request.data['Reporter']
    #    }
    #    serialized = ArticleSerializer(data=request.data )
    #    if serialized.is_valid():
    #        serialized.save()
    #        return Response(serialized.data, status=200)
    #    return Response(serialized.errors, status=404)
    # def put(self,request):
    #     # first get the object 
    #     id=request.data['id']
    #     print("id is the ",id)
    #     obj=Article.objects.get(id=id)
    #     data = request.data
    #     serilaized=ArticleSerializer(obj,data=data)
    #     if serilaized.is_valid():
    #         serilaized.save()
    #         return Response(serilaized.data, status=200)
    #     else:
    #         return "not found"
       
    # def delete(self,request):
    #     id=request.data['id']
    #     print("id is the ",id)
    #     obj = Article.objects.get(id=id)
    #     obj.delete()
       
    # def put(self,request):
    #     quest_id = request.data['id']
    #     name = request.data['name']
    #     email = request.data['email']

    #     try:
    #         booking_obj= p.objects.get(id=quest_id)
    #         booking_obj.name = name

    #         booking_obj.save()
    #         message = {
    #             'message':  "bookin gdeetail updated",
    #             'status_code': 200
    #         }
    #         return Response(message)

    #     except:
    #         message ={
    #             'message':'not found',
    #             'status-code': 400
    #         }
    #         return Response(message)

    # def post(self,request):
    #     # what abt if m goon save the article
    #     reporter_id = request.data['id']
    #     headline = request.data['headline']
    #     reporter_obj = Reporter.objects.get(id=reporter_id)
    #     data ={
    #         'hadline':headline,
    #         'Reporter':reporter_obj
    #     }
    #     obj = ArticleSerializer(data= data)

    # def put(self,request,id):
    #     name= reqeust.data['name']
    #     email = reqeust.data['email']
    #     data =[
    #         'name' :name,
    #         'email': email
    #     ]
    #     obj=Article.objects.get(id=id)
    #     serilized = ArticleSerializer(obj,data=data)
    #     if serilized.is_valid():
    #         serilized.save()