from mastodon import Mastodon

# Register app - only once!

Mastodon.create_app(
     'mastrss',
     api_base_url = 'https://glitch.social',
     to_file = 'mastrss_clientcred.secret'
     )
