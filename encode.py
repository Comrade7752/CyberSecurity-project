#!/usr/bin/env python
# coding: utf-8

# In[1]:


def hex(n):
    dic={0:'0',1:'1',2:'2',3:'3',4:'4',5:'5',6:'6',7:'7',8:'8',9:'9',10:'a',11:'b',12:'c',13:'d',14:'e',15:'f'}
    s=""
    while(n>0):
        s+=dic[n%16]
        n=n//16
    while len(s)<2:
        s+="0"
    return s[::-1]


# In[2]:


width=96


# In[3]:


height=48


# In[4]:


file1=open("data.txt","r+")
data=file1.read()
print(data)


# In[5]:


res=len(data)%3
while res!=0:
    data+=' '
    res+=1
    res=res%3
cipher=[]
secret="my_secret_key"
ind=0
for i in range(len(data)):
    cipher.append(ord(data[i])^ord(secret[ind]))
    ind+=1
    ind=ind%len(secret)
print(cipher)


# In[6]:


arr=[]


# In[7]:


for i in range(0,len(cipher),3):
    a,b,c=hex(cipher[i]),hex(cipher[i+1]),hex(cipher[i+2])
    arr.append("#"+a+b+c)
n=len(arr)
m=n%(width*height)
while m!=0:
    arr.append('#000000')
    m+=1
    m=m%(width*height)
print(len(arr))


# In[8]:


print(arr)


# In[9]:


from PIL import Image
import numpy as np

def hex_to_rgb(hex_code):
    hex_code = hex_code.lstrip("#")
    return tuple(int(hex_code[i:i + 2], 16) for i in (0, 2, 4))

def hex_array_to_image(hex_array, width, height):
    image_data = [hex_to_rgb(hex_code) for hex_code in hex_array]
    image_array = np.array(image_data, dtype=np.uint8).reshape(height, width, 3)
    image = Image.fromarray(image_array)
    return image


# In[10]:


k=1
for i in range(0,len(arr),(width*height)):
    aux=arr[i:i+(width*height)]
    result_image = hex_array_to_image(aux, width, height)
    filename="output"+str(k)+".png"
    k+=1
    result_image.save(filename)


# In[ ]:




