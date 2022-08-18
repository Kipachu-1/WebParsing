
import requests
import urllib.request
import urllib.parse
import re




# url = 'https://www.popsci.com/science/what-scientists-learned-when-they-tried-to-raise-a-chimp-with-a-human-baby/'
# values = {'s':'',
#           'submit':'search'}
# data = urllib.parse.urlencode(values)
# data = data.encode('utf-8')
# req = urllib.request.Request(url, data)
# resp = urllib.request.urlopen(req)
# respData = resp.read()
# paragraphs = re.findall(r'<p>(.*?)</p>',str(respData))

# clean_a = re.findall(r'<a(.*?)a>', str(paragraphs[0]))
# paragraphs_str = str(paragraphs[0])  

# cleaned_text = open('cleaned_text.txt', 'w+')
# for eachP in paragraphs:
#     clean_a = re.findall(r'<a(.*?)a>', str(eachP))
#     for part in range(len(clean_a)): 
#         clean_2 = re.findall(r'>(.*?)<', clean_a[part])
#         clean_part = clean_a[part]
#         clean_ch = clean_2[0]
#         eachP = eachP.replace(f'<a{clean_part}a>', clean_ch)
#     cleaned_text.write(f'{eachP} \n')
   
text = 'What\xe2\x80\x99s the weirdest thing you learned this week?'        
text = text.encode('utf-8', 'strict').decode()
print(text)