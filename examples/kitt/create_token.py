from livekit import api
import os

LIVEKIT_API_SECRET = 'secret'
LIVEKIT_API_KEY = 'devkey'
LIVEKIT_URL = 'ws://127.0.0.1:7880'

os.environ['LIVEKIT_API_SECRET'] = LIVEKIT_API_SECRET
os.environ['LIVEKIT_API_KEY'] = LIVEKIT_API_KEY
os.environ['LIVEKIT_URL'] = LIVEKIT_URL
# will automatically use the LIVEKIT_API_KEY and LIVEKIT_API_SECRET env vars
token = api.AccessToken() \
    .with_identity("python-bot") \
    .with_name("Python Bot") \
    .with_grants(api.VideoGrants(
    room_join=True,
    room="my-room",
)).to_jwt()
print(token)
