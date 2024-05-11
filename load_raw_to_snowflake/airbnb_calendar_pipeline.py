import dlt
from dlt.sources.helpers import requests

# Specify the URL of the API endpoint
url = "https://airbnb13.p.rapidapi.com/autocomplete"
headers = {
	"X-RapidAPI-Key": "e414657cbcmsh2cb79573490ff76p11d093jsn30bad1eb0932",
	"X-RapidAPI-Host": "airbnb13.p.rapidapi.com"
}
# Make a request and check if it was successful
response = requests.get(url, headers=headers)
response.raise_for_status()

pipeline = dlt.pipeline(
    pipeline_name="airbnb_calendar_pipeline",
    destination="snowflake",
    dataset_name="airbnb_calendar_data",
)
# The response contains a list of issues
load_info = pipeline.run(response.json(), table_name="autocomplete")

print(load_info)