
# coding: utf-8

# In[7]:

users = [{'id' : 0, "name" : "p1"},
{'id' : 1, "name" : "p2"},
{'id' : 2, "name" : "p3"},
{'id' : 3, "name" : "p4"},
{'id' : 4, "name" : "p5"},
{'id' : 5, "name" : "p6"},
{'id' : 6, "name" : "p7"},
{'id' : 7, "name" : "p8"},
{'id' : 8, "name" : "p9"},
{'id' : 9, "name" : "p10"}]


# In[8]:

friendships = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4), (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]


# In[9]:

for user in users: user["friends"] = []


# In[10]:

for i, j in friendships:
    users[i]["friends"].append(users[j]);
    users[j]["friends"].append(users[i]);


# In[11]:

def number_of_friends(user):
    return len(user["friends"])


# In[12]:

total_connections = sum(number_of_friends(user) for user in users)
from __future__ import division
num_users = len(users)
avg = total_connections/num_users
avg


# In[13]:

num_friends = [(user["name"], number_of_friends(user)) for user in users]


# In[14]:

sorted(num_friends, key = lambda (user_name, num_friends): num_friends, reverse = True)


# In[15]:

def foaf_id(user):
    return [foaf["id"] for friend in user["friends"] for foaf in friend["friends"]]


# In[16]:

def not_the_same(user, other_user):
    return user["id"] != other_user["id"]


# In[17]:

def not_friends(user, other_user):
    return all(not_the_same(friend, other_user) for friend in user["friends"]) 


# In[18]:

from collections import Counter
def foaf_id_2(user):
    return Counter(foaf["id"] 
           for friend in user["friends"] 
           for foaf in friend["friends"]
           if not_the_same(user, foaf) and 
           not_friends(user, foaf))


# In[21]:

foaf_id_2(users[3])


# In[ ]:



