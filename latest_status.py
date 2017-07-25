#!/usr/bin/python3
from mastodon import Mastodon
from stripogram import html2safehtml
#from set_instance import instance
from doing_something import mastrss, acid

instance = "glitch.social"
#acid=412
pull_limit=input("How many statuses would you like to retrieve? ")

#mastrss = Mastodon(
    #client_id = 'mastrss_clientcred.secret',
    #access_token = 'mastrss_usercred.secret',
    #api_base_url = "https://" + instance
#    )

toots=mastrss.account_statuses(acid,limit=pull_limit)
#pulled=toots[pull_limit:]
#this_content=pulled['content'];

for x in toots:
    this_content = x['content']
    this_content_clean_html = html2safehtml(this_content,valid_tags=())
    print(this_content_clean_html)

#print("The last status posted by {u[username]} was:".format(u=mastrss.account(acid)))
# using the format option above enabled me to remove unwanted spaces that I found when doing a simple print instruction mixing strings and variables
