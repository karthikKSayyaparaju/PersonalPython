import requests

# Replace these with your LinkedIn API credentials
access_token = "https://www.linkedin.com/oauth/v2/authorization?response_type=code&client_id=78c8irqzrl2q4i&redirect_uri=YOUR_REDIRECT_URI&scope=r_liteprofile%20r_emailaddress%20w_member_social&state=YOUR_UNIQUE_STATE_VALUE"

# LinkedIn Jobs API endpoint
url = 'https://api.linkedin.com/v2/jobSearch'

# Define query parameters
params = {
    'keywords': 'Data Engineer',
    'location': 'San Francisco, CA',
    'count': 10
}

# Set up headers with the access token
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Make the GET request to LinkedIn API
response = requests.get(url, headers=headers, params=params)

# Check if the request was successful
if response.status_code == 200:
    jobs = response.json()
    for job in jobs['elements']:
        print(f"Job Title: {job['title']}")
        print(f"Company: {job['companyName']}")
        print(f"Location: {job['location']}")
        print(f"Job ID: {job['id']}")
        print("----------")
else:
    print(f"Failed to retrieve jobs: {response.status_code}, {response.text}")