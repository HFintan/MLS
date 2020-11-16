import requests
import re
# Grab page content as string
page = requests.get("https://apod.nasa.gov/htmltest/gifcity/sqrt2.1mil").text

# Get rid of newlines
page = page.replace("\n","")

# Search for string beginning with 1.4 and grab the following 99 digits
# group(0) just takes the actual string as opposed to the object
real_sqrttwo_value = re.search("1.4\d{99}", page).group(0)
print(real_sqrttwo_value)
