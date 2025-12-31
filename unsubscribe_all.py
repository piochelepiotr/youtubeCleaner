from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ["https://www.googleapis.com/auth/youtube.force-ssl"]

def get_authenticated_service():
    flow = InstalledAppFlow.from_client_secrets_file(
        "client_secret.json", SCOPES
    )
    credentials = flow.run_local_server(port=0)
    return build("youtube", "v3", credentials=credentials)

def get_all_subscriptions(youtube):
    subscriptions = []
    request = youtube.subscriptions().list(
        part="id,snippet",
        mine=True,
        maxResults=50
    )

    while request:
        response = request.execute()
        subscriptions.extend(response.get("items", []))
        request = youtube.subscriptions().list_next(request, response)

    return subscriptions

def unsubscribe(youtube, subscription_id):
    youtube.subscriptions().delete(id=subscription_id).execute()

def main():
    youtube = get_authenticated_service()

    subs = get_all_subscriptions(youtube)
    print(f"📺 Found {len(subs)} subscriptions")

    for sub in subs:
        title = sub["snippet"]["title"]
        sub_id = sub["id"]

        try:
            unsubscribe(youtube, sub_id)
            print(f"❌ Unsubscribed from: {title}")
        except Exception as e:
            print(f"⚠️ Failed to unsubscribe from {title}: {e}")

    print("✅ Done.")

if __name__ == "__main__":
    main()

