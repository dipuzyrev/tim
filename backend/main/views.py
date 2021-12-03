from rest_framework import status, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import ParseError, NotFound
from django.core import serializers
import json


from .models import *


class FetchProjectsAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        projects = serializers.serialize('json', Project.objects.all())

        response = {
          'projects': json.loads(projects),
        }

        return Response(response, status=status.HTTP_200_OK)


class CustomProjectRequestAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        pain = request.data.get('pain')
        problem = request.data.get('problem')
        what_if = request.data.get('what_if')
        why = request.data.get('why')
        whose_pain = request.data.get('whose_pain')
        period = request.data.get('period')
        tried = request.data.get('tried')
        contacts = request.data.get('contacts')

        CustomProjectRequest.objects.create(
          user=request.user,
          pain=pain,
          problem=problem,
          what_if=what_if,
          why=why,
          whose_pain=whose_pain,
          period=period,
          tried=tried,
          contacts=contacts
        )

        return Response(status=status.HTTP_200_OK)


class SelectProjectAPI(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        id = request.data.get('id')

        project = Project.objects.filter(id=id).first()
        if not project:
            raise NotFound('Project not found')

        SelectProjectRequest.objects.create(
            user=request.user,
            project=project,
        )

        return Response(status=status.HTTP_200_OK)