from django.shortcuts import render
import requests
from rest_framework.views import APIView, Response


class ConValView(APIView):
    def get(self, request):
        val1 = self.request.query_params.get('from', None)
        val2 = self.request.query_params.get('to', None)
        cnt = self.request.query_params.get('value', None)
        url = f'https://api.exchangerate.host/convert?from={val1}&to={val2}&amount={cnt}'
        response = requests.get(url)
        data = response.json()
        return Response(
            {'success': data['success'], 'query': data['query'], 'info': data['info'], 'result': data['result']})
