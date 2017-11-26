#change url parameter

base_url = "http://www.pythonchallenge.com/pc/def/0.html"
print("Base url is " + base_url)
basics_url=base_url[0:-6]
print("basic url without html is " + basics_url)
another_page = "1.html"
navigate_url = basics_url + another_page
print("new url is " + navigate_url)

