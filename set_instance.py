# import sys
from mastodon import Mastodon

# print(sys.version_info)
instance = "glitch.social"
instance = raw_input("Please enter the Mastodon instance address: ")
print("Using https://" + instance + " as the current instance")
