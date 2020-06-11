from rest_framework.response import Response
from rest_framework.views import APIView
from .models import New, Comment, Upvote
from datetime import date
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
import json


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        return request.method in SAFE_METHODS


class News(APIView):

    permission_classes = [IsAuthenticated | ReadOnly]

    def get(self, request):
        """
        Get chunk of news objects.
        page, count, and JSON web token necessary.
        Returns dict of news.
        """
        try:
            page = int(request.GET['page'])
            count = int(request.GET['count'])
        except (ValueError, KeyError):
            return Response({'msg': 'invalid params'}, status=400)

        if page <= 0 or count <= 0:
            return Response({'msg': 'page and count must be positive'}, status=400)

        news = New.objects.order_by('-date').all()[(page * count - count):(page * count)]
        data = []
        today = date.today()

        if len(news) > 0:
            for new in news:
                data.append({
                    'id': new.id,
                    'title': new.title,
                    'author': new.author.username,
                    'link': new.link,
                    'creation date': new.date,
                    'upvotes': len(Upvote.objects.filter(new=new.id, date__range=(
                        "{} 00:00:00.000000+00:00".format(today),
                        "{} 23:59:59.999999+00:00".format(today)
                    )).all()),
                    'comments': len(Comment.objects.filter(news=new.id).all())
                })
        return Response(data, status=200)

    def post(self, request):
        """
        Create a new.
        title, link, and JSON web token necessary.
        Returns message OK in dict.
        """
        body = json.loads(request.body)
        if 'title' not in body or 'link' not in body:
            return Response({'msg': "invalid JSON body"}, status=400)
        else:
            New.objects.create(
                title=str(body['title']),
                link=str(body['link']),
                author=request.user
            )
            return Response({'msg': 'OK'}, status=200)

    def delete(self, request):
        """
        Delete a new.
        id and JSON web token necessary.
        Returns message OK in dict.
        """
        body = json.loads(request.body)
        if 'id' not in body:
            return Response({'msg': "invalid JSON body"}, status=400)
        else:
            try:
                id = int(body['id'])
            except (ValueError, KeyError):
                return Response({'msg': 'invalid params'}, status=400)

            new = New.objects.filter(id=id, author=request.user).first()
            if new:
                new.delete()
                return Response({'msg': 'OK'}, status=200)
            else:
                return Response({'msg': "Not found"}, status=404)


class Upvotes(APIView):

    def post(self, request):
        """
        Vote up for the news.
        id and JSON web token necessary.
        Returns message OK in dict.
        """
        body = json.loads(request.body)
        if 'id' not in body:
            return Response({'msg': "invalid JSON body"}, status=400)
        else:
            try:
                id = int(body['id'])
            except (ValueError, KeyError):
                return Response({'msg': 'invalid params'}, status=400)

            today = date.today()
            new = New.objects.filter(id=id).first()
            upvote = Upvote.objects.filter(new_id=id, user_id=request.user.id, date__range=(
                "{} 00:00:00.000000+00:00".format(today),
                "{} 23:59:59.999999+00:00".format(today))
                                           ).first()
            if new:
                if upvote is None:
                    Upvote.objects.create(
                        new_id=new.id,
                        user_id=request.user.id
                    )
                    new.votes += 1
                    new.save()
                    return Response({'msg': 'OK'}, status=200)
                else:
                    return Response({'msg': "You cant vote for this new today"}, status=403)

            return Response({'msg': "Not found"}, status=404)


class Comments(APIView):

    def get(self, request):
        """
        Get chunk of comments objects.
        id, page, count and JSON web token necessary.
        Returns dict of comments.
        """
        try:
            id = int(request.GET['id'])
            page = int(request.GET['page'])
            count = int(request.GET['count'])
        except (ValueError, KeyError):
            return Response({'msg': 'invalid params'}, status=400,)

        if page <= 0 or count <= 0:
            return Response({'msg': 'page and count must be positive'}, status=400)

        new = New.objects.filter(id=id).first()
        if New:
            data = []
            comments = Comment.objects.filter(news=new).all()[(page * count - count):(page * count)]
            if len(comments) > 0:
                for comment in comments:
                    data.append({
                        'text': comment.text,
                        'author': comment.user.username,
                        'date': comment.date
                    })
            return Response(data, status=200)
        else:
            return Response({'msg': "Not found"}, status=404)

    def post(self, request):
        """
         Create a comment object.
         id, text and JSON web token necessary.
         Returns message OK in dict.
         """
        body = json.loads(request.body)

        if 'text' in body and 'id' in body:
            try:
                text = str(body['text'])
                id = int(body['id'])
            except (ValueError, KeyError):
                return Response({'msg': 'invalid params'}, status=400)

            news = New.objects.filter(id=id).first()
            if news:
                Comment.objects.create(text=text, user=request.user, news=news)
                return Response({'msg': 'OK'}, status=200)

            else:
                return Response({'msg': "New not found"}, status=404)
        else:
            return Response({'msg': "invalid JSON body"}, status=400)
