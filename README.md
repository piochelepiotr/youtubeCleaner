# YouTube Feed Cleaner

A simple Python tool to take control of your YouTube experience by managing your subscriptions programmatically. This project helps you maintain a curated, intentional YouTube feed based only on your subscriptions, eliminating algorithmic distractions.

## 🎯 Philosophy

This tool is designed for people who want to:
- Clean their YouTube feed to only show subscription content
- Avoid the addictive "Home" feed with algorithmic recommendations
- Curate a deliberate list of channels using AI assistance
- Regularly reset and refine their content consumption

## 🚀 Features

- **Unsubscribe from all channels** - Start with a clean slate
- **Bulk subscribe to channels** - Add multiple channels at once from a list
- **AI-assisted curation** - Use ChatGPT to help build your channel list

## 📋 Prerequisites

- Python 3.7 or higher
- A Google account
- Google Cloud Project with YouTube Data API v3 enabled

## 🔧 Setup Instructions

### Step 1: Set Up Google Cloud Project

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project (or select an existing one)
3. Enable the **YouTube Data API v3**:
   - In the left sidebar, go to "APIs & Services" > "Library"
   - Search for "YouTube Data API v3"
   - Click on it and press "Enable"

### Step 2: Create OAuth 2.0 Credentials

1. In Google Cloud Console, go to "APIs & Services" > "Credentials"
2. Click "Create Credentials" > "OAuth client ID"
3. If prompted, configure the OAuth consent screen:
   - Choose "External" user type
   - Fill in the required app information
   - Add your email as a test user
4. For application type, select "Desktop app"
5. Name it something like "YouTube Subscription Manager"
6. Click "Create"
7. Download the credentials JSON file
8. Rename it to `client_secret.json` and place it in this project directory

### Step 3: Install Python Dependencies

```bash
# Create a virtual environment (recommended)
python3 -m venv .venv

# Activate the virtual environment
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

## 📖 Usage

### Option 1: Unsubscribe from All Channels

Start with a clean slate by unsubscribing from all your current subscriptions:

```bash
python unsubscribe_all.py
```

This script will:
- Fetch all your current subscriptions
- Unsubscribe from each one
- Display progress as it works

### Option 2: Subscribe to Curated Channels

#### Using ChatGPT to Generate Your Channel List

1. Go to [ChatGPT](https://chat.openai.com/)
2. Use a prompt like this:

```
I want to curate my YouTube subscriptions around these topics:
- Woodworking and DIY
- Gardening and self-sufficiency
- 3D printing
- Tennis
- Skiing
- Personal finance

Please suggest 20-30 high-quality YouTube channels in these areas.
Format the output as a Python list of channel names, like:
["Channel Name 1", "Channel Name 2", ...]
```

3. Copy the channel list that ChatGPT provides

#### Update the Script and Run

1. Open `subscribe_channels.py`
2. Replace the `CHANNEL_NAMES` list (lines 6-28) with your curated list
3. Run the script:

```bash
python subscribe_channels.py
```

The script will:
- Search for each channel by name
- Subscribe to channels that are found
- Report any channels that couldn't be found

**Note:** The first time you run either script, a browser window will open asking you to authorize the application to access your YouTube account.

## 🧹 Disable YouTube's Home Feed

To complete your YouTube detox and rely only on subscriptions:

### On Desktop (YouTube.com)

1. Go to [YouTube Settings](https://www.youtube.com/account)
2. Click on "Manage all history" or go directly to [myactivity.google.com](https://myactivity.google.com/myactivity)
3. On the left sidebar, click "Activity controls"
4. Find "YouTube History" and toggle it **OFF**
5. Confirm the action

**Alternative:** You can also use browser extensions like:
- **Unhook** - Removes YouTube's addictive features
- **DF YouTube** - Distraction-free YouTube

### On Mobile

1. Open the YouTube app
2. Tap your profile picture > Settings
3. Go to "History & privacy"
4. Toggle off "Watch history" and "Search history"
5. Optionally, clear your existing history

### Result

With watch history disabled:
- The YouTube home page will become mostly empty or show a message
- Your main feed becomes the "Subscriptions" tab
- Recommendations are significantly reduced
- You regain control over your content consumption

## 🛡️ Privacy & Security

- **Never commit `client_secret.json`** to version control
- The OAuth tokens are stored locally and only you have access to them
- These scripts only request the minimum required permissions
- No data is collected or sent anywhere except to YouTube's official API

## ⚠️ Quota Limits

The YouTube Data API has daily quota limits:
- Each subscription/unsubscription costs 50 quota units
- Default daily limit is 10,000 units (200 operations per day)
- If you hit the limit, wait 24 hours and try again

## 🤔 Troubleshooting

**"The authentication flow failed"**
- Make sure you've added yourself as a test user in the OAuth consent screen
- Check that the YouTube Data API v3 is enabled

**"Channel not found"**
- The channel name might not match exactly
- Try searching YouTube manually for the correct channel name
- Some channels have different display names

**"Daily quota exceeded"**
- You've hit YouTube's API limits
- Wait 24 hours before trying again
- Consider processing your channels in smaller batches

## 🤝 Contributing

Feel free to open issues or submit pull requests if you have suggestions for improvements!

