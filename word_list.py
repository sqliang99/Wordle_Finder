#!/usr/bin/env python
# coding: utf-8

# In[8]:


import urllib
url = "https://gist.githubusercontent.com/cfreshman/a03ef2cba789d8cf00c08f767e0fad7b/raw/5d752e5f0702da315298a6bb5a771586d6ff445c/wordle-answers-alphabetical.txt"
file = urllib.request.urlopen(url)

word_list = [line.decode("utf-8")[:-1] for line in file]


# In[ ]:




