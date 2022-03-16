#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().system('pip install pywhatkit')
get_ipython().system('pip install Flask')


# In[1]:


import pywhatkit


# In[2]:


Yourmessage = input("Enter your message: ")


# In[3]:


#hour = int(input("At what hour you want to send the message: "))


# In[ ]:


pywhatkit.sendwhatmsg("+918530744101",Yourmessage,12,46)


# In[ ]:




