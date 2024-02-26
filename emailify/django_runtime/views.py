# views.py

import re
import requests
import json
from django.shortcuts import render
from django.http import JsonResponse

# Returns the index.html page
def index_view(request):
    return render(request, 'website/index.html')

# Returns the result.html, else return a JSON error
def result_view(request):
    if request.method == 'GET':
        # Retrieve emails from query parameters
        emails_str = request.GET.get('emails')
        if emails_str:
            emails = json.loads(emails_str)
        else:
            emails = []

        # Render the result.html template with emails
        return render(request, 'website/result.html', {'emails': emails})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)


# This function is used by the WebUI.
# It makes a GET request to the URL provided by the user and
# searches for any email provided in it.
def check_website(request):
    if request.method == 'POST':
        url = request.POST.get('url')

        if url:

            # Check if the URL has a protocol, if not, prepend 'http://' as default
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url

            try:
                response = requests.get(url)
                response.raise_for_status()
                html = response.text

                # Extract emails from the HTML response using regex
                emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)

                # Remove duplicates by converting the list to a set and back to a list
                unique_emails = list(set(emails))

                if request.content_type == 'application/json':
                    # If it's an API request, return JSON response
                    return JsonResponse({'emails': unique_emails})
                else:
                    # If it's a form submission, redirect to the result page with emails as query parameter
                    return JsonResponse({'emails': unique_emails}, status=200)
            except requests.RequestException as e:
                return JsonResponse({'error': str(e)}, status=400)
        else:
            return JsonResponse({'error': 'URL not provided'}, status=400)
    elif request.method == 'GET':
        # For GET requests, render the index.html page
        return index_view(request)
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

# This function is used by the API.
# It makes a GET request to the URL provided by the user and
# searches for any email provided in it.
def api_check_website(request):
    if request.method == 'GET':
        url = request.GET.get('url')

        if url:

            # Check if the URL has a protocol, if not, prepend 'http://' as default
            if not url.startswith('http://') and not url.startswith('https://'):
                url = 'http://' + url

            try:
                response = requests.get(url)
                response.raise_for_status()
                html = response.text

                # Extract emails from the HTML response using regex
                emails = re.findall(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}', html)

                # Remove duplicates by converting the list to a set and back to a list
                unique_emails = list(set(emails))

                if emails:
                    # Return success response with extracted emails
                    return JsonResponse({'status': 'success', 'emails': unique_emails}, status=200)
                else:
                    # Return error response for no email address found
                    return JsonResponse({'status': 'error', 'message': 'No email address found'}, status=404)
            except requests.RequestException as e:
                # Return error response for request exception
                return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
        else:
            # Return error response for missing URL parameter
            return JsonResponse({'status': 'error', 'message': 'URL not provided'}, status=400)
    else:
        # Return error response for disallowed method
        return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)
