from datetime import datetime
from dateutil.relativedelta import relativedelta
import json

# Sample JSON input with multiple start dates and an end date
json_input = '''
{
    "start_dates": [
    "2016-01-28T00:00:00",  
    "1992-11-09T07:20:00",
    "1993-05-09T07:20:00",
    "1992-09-18T08:20:00",
    "2024-11-09T00:00:00",
    "2030-12-31T00:00:00",
    "2025-01-01T00:00:00",
    "2025-04-01T00:00:00"],
    
    "end_date": "2024-10-12T00:00:00"
}
'''

# Parse the JSON input
data = json.loads(json_input)

# Extract end date from JSON and convert to datetime object
end_date = datetime.strptime(data['end_date'], '%Y-%m-%dT%H:%M:%S')

# Initialize a list to store the results
results = []

# Loop through all start dates and calculate the difference with the end date
for start_date_str in data['start_dates']:
    # Convert the start date string to a datetime object
    start_date = datetime.strptime(start_date_str, '%Y-%m-%dT%H:%M:%S')

    # Calculate the difference between the start date and end date
    difference = relativedelta(end_date, start_date)

    # Append the result to the list
    results.append({
        "start_date": start_date_str,
        "years": difference.years,
        "months": difference.months,
        "days": difference.days,
        "hours": difference.hours
    })

# Output the results
for result in results:
    print(f"Start date: {result['start_date']}")
    print(
        f"Difference: {result['years']} years, {result['months']} months, {result['days']} days, {result['hours']} hours\n")