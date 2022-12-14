from bs4 import *
import requests
import os

def folder_create(images, folder_name):
    try:
   
        os.mkdir(f'{folder_name}\imgs')
 
    except:
        print("Folder Exist with that name!")
        folder_create()
 
   
    download_images(images, folder_name)
 
 

def download_images(images, folder_name):
   
   
    count = 0
 
   
    print(f"Total {len(images)} Image Found!")
 
  
    if len(images) != 0:
        for i, image in enumerate(images):
       
            try:
                
                image_link = image["data-srcset"]
                 
            
            except:
                try:
                 
                    image_link = image["data-src"]
                except:
                    try:
                      
                        image_link = image["data-fallback-src"]
                    except:
                        try:
                            image_link = image["src"]
 
                     
                        except:
                            pass
 
            try:
                r = requests.get(image_link).content
                try:
 
                    
                    r = str(r, 'utf-8')
 
                except UnicodeDecodeError:
 
                   
                    with open(f"{folder_name}/imgs/images{i+1}.jpg", "wb+") as f:
                        f.write(r)
 
                  
                    count += 1
            except:
                pass
 
       
        if count == len(images):
            print("All Images Downloaded!")
             
      
        else:
            print(f"Total {count} Images Downloaded Out of {len(images)}")
 

def main(url, folder_name):
   
  
    r = requests.get(url)
 
  
    soup = BeautifulSoup(r.text, 'html.parser')

    images = soup.findAll('img')
 
    folder_create(images, folder_name)
 
