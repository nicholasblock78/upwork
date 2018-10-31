import urllib.request

#ruby doesnt work
url = 'https://www.acehardware.com/departments/outdoor-living/grills-and-smokers/gas-grills/8895344'
#no source code
url1="https://www.ulta.com/perfect-setting-powder?productId=xlsImpprod15931151"
#yes source code
url2="https://www.aswechange.com/buy-cheeky-physique-sublime-bust-volumizing-bust-serum-359889"
url="https://www.abt.com/product/79448/Samsung-French-Door-Stainless-Steel-Bottom-Freezer-Refrigerator-With-Food-ShowCase-Fridge-Door-RF28HDEDBSR.html#tab2"

response = urllib.request.urlopen(url)
webContent = response.read()
match = webContent.decode("utf-8").find('POWERREVIEWS.display.render')
# match equals index of first match occurence
#-1 means not found
print(match)


# print(webContent.decode("utf-8"))
