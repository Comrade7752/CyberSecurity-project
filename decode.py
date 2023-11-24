#!/usr/bin/env python
# coding: utf-8

# In[1]:


from PIL import Image

def rgb_to_hex(rgb):
    return "#{:02x}{:02x}{:02x}".format(rgb[0], rgb[1], rgb[2])

def image_to_hex_array(image_path):
    image = Image.open(image_path)
    width, height = image.size
    pixel_data = list(image.getdata())

    hex_array = [rgb_to_hex(pixel) for pixel in pixel_data]

    return hex_array, width, height

image_path = "output1.png"

hex_array, image_width, image_height = image_to_hex_array(image_path)


# In[2]:


dic={"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"a":10,"b":11,"c":12,"d":13,"e":14,"f":15}
def convert(s):
    return dic[s[0]]*16+dic[s[1]]


# In[7]:


arr=[]
secret="my_secret_key"
ind=0
for i in hex_array:
    if (i=="#000000"):
        break
    aux=i[1:]
    a,b,c=aux[0:2],aux[2:4],aux[4:6]
    arr.append(convert(a)^ord(secret[ind]))
    ind+=1
    ind%=len(secret)
    arr.append(convert(b)^ord(secret[ind]))
    ind+=1
    ind%=len(secret)
    arr.append(convert(c)^ord(secret[ind]))
    ind+=1
    ind%=len(secret)


# In[8]:


data=""
for i in arr:
    data+=chr(i)
print(data)


# In[ ]:




