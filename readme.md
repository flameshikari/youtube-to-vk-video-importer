## Description

This script can collect links of all videos from YouTube channel into the file and upload them to the video section of your VK group.



## Features

* Pretty output;
* Works with channel IDs and usernames;
* Collecting links to the file;
* Pausing and resuming the upload process;
* Setting custom start and end positions.

Average speed of importing videos is ≈1.1 video per second by my tests. *Such speed!*

## Requirements

**Python 3.*** with `requests` and `vk` modules. Installation examples:

#### Arch Linux
```bash
$ sudo pacman -S python3 python3-pip
$ pip3 install --user --upgrade requests vk
```

#### Ubuntu (or Debian)
```bash
$ sudo apt install python3 python3-pip
$ pip3 install --user --upgrade requests vk
```

## Configuration

The settings are located in `config.yaml`. An example of the settings:

```python
youtube_api_key: JKFjskf71jxvnf9781hjkv-21jf7f
youtube_channel: Kurzgesagt
vk_login: mail@example.com
vk_password: totallynotapassword
vk_app_id: 13333337
vk_group_id: 13333337
vk_api_version: 5.0
```

The filling of the settings will take 5 minutes of your time. Let's go!

#### youtube_api_key

It's hard to explain, read **[this](http://help.dimsemenov.com/kb/wordpress-royalslider-tutorials/wp-how-to-get-youtube-api-key)**!

#### youtube_channel

Just copy username or channel ID from YouTube URL. Examples:
: Channel ID: `https://www.youtube.com/channel/`**UCsXVk37blfLxx1rDPwtNM8Q**
: Username: `https://www.youtube.com/user/`**example**

#### vk_api_login

Your VK profile login. 

#### vk_api_password

Your VK profile password. Don't worry, this script doesn't send your password to China servers or something. You can check source code anyway.

#### vk_api_id

Click **[here](https://vk.com/editapp?act=create)** to create an app. After creating an app go to **Settings**, copy **Application ID** and paste it to config file between quote marks. Done!

#### vk_group_id

Go to the group and copy ID from address bar. Example:
: Group ID: `https://vk.com/group`**1337**

#### vk_api_version

Since February 2018 [every request to VK API should contains the parameter with API's version](https://vk.com/dev/version_update). Version `5.0` works fine, you can set it.

## Using

After filling settings, you can execute the script by:
```bash
$ python importer.py
```


## License

This project is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
