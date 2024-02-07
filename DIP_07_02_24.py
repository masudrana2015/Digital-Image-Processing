#!/usr/bin/env python
# coding: utf-8

# In[1]:


import glob
files = glob.glob("*.txt")
print(files)


# In[8]:


import cv2
arr=[]
path="*.*"

for i in glob.glob(path):
    print(i)
    a=cv2.imread(i)
    arr.append(a)
    
from matplotlib import pyplot as plt
plt.imshow(arr[13])


# In[11]:


import cv2
a=cv2.imread("p.jpg")
t=1
cv2.imwrite("Color_image"+str(t)+".jpg",a)


# In[15]:


import os


directory_path = r"C:\Users\User\Downloads\images"


files = os.listdir(directory_path)


for file_name in files:
   
    current_path = os.path.join(directory_path, file_name)

    
    new_file_name = "new_prefix_" + file_name 
    new_path = os.path.join(directory_path, new_file_name)

    
    os.rename(current_path, new_path)

print("Files renamed successfully.")


# In[20]:


import os
import cv2

def rename_and_convert(directory_path):
    files = os.listdir(directory_path)

    for file_name in files:
        if file_name.endswith(('.jpg', '.png', '.jpeg')):
            new_name = "new_" + file_name

            old_path = os.path.join(directory_path, file_name)
            new_path = os.path.join(directory_path, new_name)

            
            print(f"Old path: {old_path}")
            print(f"New path: {new_path}")

            
            os.rename(old_path, new_path)

            
            bgr_image = cv2.imread(new_path)

            
            if bgr_image is not None:
                
                rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

                
                cv2.imwrite(new_path, rgb_image)
                print(f"Conversion successful for {new_path}")
            else:
                print(f"Failed to load image: {new_path}")

if __name__ == "__main__":
    directory_path = r"C:\Users\User\Downloads\images"
    rename_and_convert(directory_path)


# In[22]:


import os
path=r"C:\Users\User\Downloads\images"
print(os.listdir(path))

for l in os.listdir(path):
   print(l)


# In[29]:


import os
print(os.walk("."))

for root,dirs,fiels in os.walk("."):
    path=root.split(os.sep)
    
print((len(path) - 1) * '---', os.path.basename(root))


for file in files:
    print(len(path)*'--',file)


# In[30]:


import os
for root,subdir,files in os.walk("."):
    
    for name in dirs:
        print(os.path.join(root,name))
    for name in files:
        print(os.path.join(root,name))
        


# In[32]:


from skimage import data, io, color, transform
from skimage.transform import rescale, resize , downscale_local_mean

img=io.imread('p.jpg')
plt.imshow(img)


# In[33]:


img_rescaled=rescale(img,1.0/4.0,anti_aliasing=False)
plt.imshow(img_rescaled)


# In[34]:


img_resized=resize(img,(200,200))
plt.imshow(img_resized)


# In[ ]:




