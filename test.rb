require 'open-uri'
require 'net/http'

url="https://www.aswechange.com/buy-cheeky-physique-sublime-bust-volumizing-bust-serum-359889"
url1="https://www.ulta.com/perfect-setting-powder?productId=xlsImpprod15931151"
url2="https://abcwarehouse.com/hotpoint-by-ge-htx24easkws"
url3="https://www.acehardware.com/departments/outdoor-living/grills-and-smokers/gas-grills/8895344"
url="https://www.abt.com/product/79448/Samsung-French-Door-Stainless-Steel-Bottom-Freezer-Refrigerator-With-Food-ShowCase-Fridge-Door-RF28HDEDBSR.html#tab2"

# res = Net::HTTP.get_response(URI.parse(url).host, URI.parse(url).path)
# # puts r
#
# # res = Net::HTTP.get_response(url3)
#
# # # Headers
# # res['Set-Cookie']            # => String
# # res.get_fields('set-cookie') # => Array
# # res.to_hash['set-cookie']    # => Array
# # puts "Headers: #{res.to_hash.inspect}"
#
# # Status
# puts res.code       # => '200'
# puts res.message    # => 'OK'
# puts res.class.name # => 'HTTPOK'
#
# # Body
# puts res.body if res.response_body_permitted?

if open(url)
fh = open(url)
html = fh.read
matched = html.match(/POWERREVIEWS.display.render/)
if matched == nil
  puts "Not in source code"
else
  puts matched.post_match[0..1000]
end
end
