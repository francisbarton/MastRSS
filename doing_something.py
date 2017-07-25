#!/usr/bin/python3
from mastodon import Mastodon
from set_instance import instance

# instance = "glitch.social"

mastrss = Mastodon(
    client_id = 'mastrss_clientcred.secret',
    access_token = 'mastrss_usercred.secret',
    api_base_url = "https://" + instance
    )

#print(mastodon.instance() ['description'])

acid = input("Please enter the account ID: ")
#acid=412

#this_username = mastrss.account(acid) ['username'];
#this_statuses = mastrss.account(acid) ['statuses_count'];

#print("This is:"),this_username,(", statuses posted:"),this_statuses

print("That ID belongs to {u[username]} ({u[display_name]}), who has posted {u[statuses_count]} statuses so far.".format(u=mastrss.account(acid)))

#print("This is ", this_username[-1], " with ", this_statuses, " statuses posted so far.")
