from django.shortcuts import render

import requests
from django.http import JsonResponse
from rest_framework.response import Response


def get_environmental_news(request):
    api_key = "YOUR_NEWS_API_KEY"

    city = request.GET.get("city")
    state = request.GET.get("state")
    country = request.GET.get("country")
    key = "a594258f-1e29-4a9c-8009-5d8a896ac58d"

    api_url = f"http://api.airvisual.com/v2/city?city={city}&state={state}&country={country}&key={key}"

    try:
        response = requests.get(api_url)
        data = response.json()
        print(data)
        if data["status"] != "success":
            return JsonResponse({"error": "please be sure from data you entered"},status=400)

        return JsonResponse(data, status=200)

    except requests.RequestException as e:
        return JsonResponse(
            {"error": f"Failed to fetch news data: {str(e)}"}, status=500
        )
