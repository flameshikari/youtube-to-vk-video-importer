## Description

That script imports all videos from YouTube channel to the video section of your VK group. Perhaps, someone will needs it. 

## Requirements

**Python 3** with **requests** and **vk**. Install them:

```bash
sudo pip3 install vk requests
```

## Features

* Pretty output;
* Works with channel IDs and usernames;
* Saving links to file;
* Pausing;
* Setting custom positions.

By my calculation, speed of importing videos is ≈1 video per second. *Such speed!*

## Getting Credentials

Settings are located in the head of <b>importer.py</b> file. They look next:

```python
settings = {'youtube_api_key':  '',
            'youtube_channel':  '',
            'vk_login':         '',
            'vk_password':      '',
            'vk_app_id':        '',
            'vk_group_id':      ''}
```

The harder part of filling settings is getting YouTube API key and creating an application in VK… heh, just kidding. It'll take 5 minutes of your time or less. Let's go!

#### youtube_api_key

It's hard to explain, read **[this](http://help.dimsemenov.com/kb/wordpress-royalslider-tutorials/wp-how-to-get-youtube-api-key)**!

#### youtube_channel

Just copy username or channel ID from YouTube URL. That's it.

#### vk_api_login

Your VK profile login. Don't worry, this script isn't sending your credentials to another server.

#### vk_api_password

Your VK profile password. Keep calm! 

#### vk_api_id

**[Click here](https://vk.com/editapp?act=create)** to create an app. After creating an app go to **Settings**, copy **Application ID** and paste it to config file between quote marks. Done!

#### vk_group_id

Well, it's easy too to get.

## Using

After filling settings, you can execute the script by:
```bash
python3 importer.py
```
or:
```bash
chmod +x importer.py
./importer.py
```

## License

This project is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
