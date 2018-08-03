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

```
youtube_api_key: JKFjskf71jxvnf9781hjkv-21jf7f
youtube_channel: Kurzgesagt
vk_login: mail@example.com
vk_password: totallynotapassword
vk_app_id: 13333337
vk_group_id: 13333337
vk_api_version: 5.0
```

Let's see what's defined in `config.yaml`.

#### youtube_api_key

YouTube API key. **[Here is a tutorial for getting the key](http://help.dimsemenov.com/kb/wordpress-royalslider-tutorials/wp-how-to-get-youtube-api-key)**.

#### youtube_channel

Username or channel ID. Examples:

![alt text](https://www.slickremix.com/wp-content/uploads/2013/08/Screen-Shot-2015-05-08-at-2.20.51-AM.png "Channel ID")
***
![alt text](https://www.slickremix.com/wp-content/uploads/2013/08/Screen-Shot-2014-10-25-at-7.45.00-PM.png "Username")

#### vk_api_login

Your VK profile login. It should be an email address.

#### vk_api_password

Your VK profile password. Don't worry, this script doesn't send your password to China servers or something. You can check source code anyway.

#### vk_api_id

Click **[here](https://vk.com/editapp?act=create)** to create an app. After creating an app go to **Settings**, copy **Application ID** and paste it to config file between quote marks. Done!

#### vk_group_id

Go to the group and just copy ID number from address bar.

#### vk_api_version

Since February 2018 [every request to VK API should contains the parameter with API's version](https://vk.com/dev/version_update). Version `5.0` works fine, you can set it.

## Using

After filling settings, you can execute the script by:
```bash
$ python importer.py
```
The script will ask you about collecting links, positions, etc. Also it will shows some tips for using, pausing/resuming, etc.
## License

This project is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
