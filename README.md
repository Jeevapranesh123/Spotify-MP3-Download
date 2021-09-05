# Spotify MP3  Download

### Getting Started

Clone this repository

All the Configuration need to be Given in Config.json

### Getting Profile URL

1. Open Spotify Desktop or Spotify Web Player

2. Open Your Profile

3. Copy Link to Profile

4. Open Config.json

```
{
            "OAuth_Token":"",

            "profile_url":"",

            "Playlist":""
}

```
5. Paste your profile url in Config.json file in "profile_url"

```
Example: "profile_url":"https://open.spotify.com/user/4giirgtpao0enysbvdcdaxnri?si=682ab7cff3ac48ed"
```

### Getting OAuth Token

1. [Login](https://developer.spotify.com/dashboard/) at Spotify for Developers

2. [Head](https://developer.spotify.com/console/get-current-user/) to get OAuth Access Token

3. Click on Get Token 

4. Copy the Token and paste in Config.json

```
Example "OAuth_Token":"<copied_token>"
```

### Enter Playlist to Download

1. Open Config.json

2. Paste the Playlist form which you want to Download Songs

```
Example "Playlist":"<Playlist to Download>"
```

### All Set

#### Run Main.py

```
python .\main.py

```
