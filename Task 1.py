#!/usr/bin/env python
# coding: utf-8

# # Task 1 : Getting to Philosophy

# In[1]:


import requests
from bs4 import BeautifulSoup as bs
import time


# In[2]:


#Here I store the links that have been accessed by the method
links_clicked = []
#It is the text to be added (concatinated) to the first link selected from the main body
wiki_text = "https://en.wikipedia.org"
#The string of the Philosophy page
philosophy_url = "https://en.wikipedia.org/wiki/Philosophy"

#The Method had (max_iter) as a parameter in order to give the user more flexbility to 
#determine the maximum number of links to be accessed to avoid infinite loops
def reach_philosophy(url, max_iter):
    global links_clicked
    links_clicked.append(url)
#A condition to check if the Philosophy page is reached
    if url == philosophy_url:
        print "Philosophy Page Reached"
        print links_clicked
        links_clicked = []
#A condition to check if maximam iterations reached        
    elif max_iter == 1:
        print "Maximam Iterations Reached"
        print links_clicked
        links_clicked = []
        
    else:
        global web_url
        try:
            #Access the link given
            web_url = requests.get(url).text
        #An except statement to avoid error if there is a failed connection 
        #due to multiple requests made on Wikipedia    
        except requests.exceptions.ConnectionError:
            print "Connection Failed"
        except requests.exceptions.HTTPError as err:
            print err
        #Using BeautifulSoup to get the Html source code
        web_soup = bs(web_url, "lxml")
        #Selecting the links found in the paragraphs of the articles
        links = web_soup.select("body p > a")
        #A condition to check if there are any links in the current article
        if len(links) == 0:
            print "No Links Found"
            print links_clicked
            links_clicked = []
        else:
            #Check if the first link is a Wikipedia link
            use_link = links[0]
            for link in links:
                if ("/wiki/" in str(link)):
                    use_link = link
                    break
                else:
                    continue
            #Selecting the link that is contained in the "href"
            new_link = use_link.get("href")
            #Concatination of the strings of the main domain of Wikipedia 
            #with the first link found in the article
            new_link_conc = wiki_text + new_link
            time.sleep(0.5)
            reach_philosophy(new_link_conc, max_iter-1)


# In[3]:


reach_philosophy("https://en.wikipedia.org/wiki/Special:Random", 20)

