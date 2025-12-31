from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

CHANNEL_NAMES = [
    "Paul Sellers",
    "Woodworking for Mere Mortals",
    "Jonathan Katz-Moses",
    "Charles Dowding",
    "Epic Gardening",
    "Self Sufficient Me",
    "FreshCap Mushrooms",
    "Mossy Creek Mushrooms",
    "Southwest Mushrooms",
    "CNC Kitchen",
    "Teaching Tech",
    "Makers Muse",
    "Intuitive Tennis",
    "Essential Tennis",
    "Top Tennis Training",
    "Deb Armstrong",
    "Stomp It Tutorials",
    "Ski School by Elate Media",
    "Ben Felix",
    "The Plain Bagel",
    "Patrick Boyle",
]

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", SCOPES
    )
    credentials = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=credentials)

def find_channel_id(youtube, channel_name):
    request = youtube.search().list(
        q=channel_name,
        part="snippet",
        type="channel",
        maxResults=1
    )
    response = request.execute()
    items = response.get("items", [])
    if not items:
        return None
    return items[0]["snippet"]["channelId"]

def subscribe(youtube, channel_id):
    request = youtube.subscriptions().insert(
        part="snippet",
        body={
            "snippet": {
                "resourceId": {
                    "kind": "youtube#channel",
                    "channelId": channel_id
                }
            }
        }
    )
    request.execute()

def main():
    youtube = get_authenticated_service()

    for name in CHANNEL_NAMES:
        print(f"🔍 Searching for: {name}")
        channel_id = find_channel_id(youtube, name)

        if not channel_id:
            print(f"❌ Channel not found: {name}")
            continue

        try:
            subscribe(youtube, channel_id)
            print(f"✅ Subscribed to: {name}")
        except Exception as e:
            print(f"⚠️ Could not subscribe to {name}: {e}")

if __name__ == "__main__":
    main()

