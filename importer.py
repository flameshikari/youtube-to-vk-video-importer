#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import json
import os
import sys
import time


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                                CREDENTIALS                                  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


settings = {'youtube_api_key':  '',
            'youtube_channel':  '',
            'vk_login':         '',
            'vk_password':      '',
            'vk_app_id':        '',
            'vk_group_id':      ''}


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                                   MESSAGES                                  #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #

error_interrupt = 'Forced exit!'

import_paused = 'Importing is paused on {} video! Enter to continue or ' \
                'interrupt to exit: '

video_imported = 'Video {} is imported! Link: {}'

retrying_upload = 'Something goes wrong while importing {} video. Retrying!'
value_empty = 'Value cannot be empty!'
value_less = 'Value cannot be less than {}!'
value_more = 'Value cannot be more than {}!'
value_int = 'Value must be integer!'


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                        COOLING OUTPUT WITH LOGGING                          #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


class Color:
    b = '\033[94m'  # BLUE
    g = '\033[92m'  # GREEN
    r = '\033[91m'  # RED
    y = '\033[93m'  # YELLOW
    x = '\033[0m'   # RESET


def log(message, n=0, use_print=True):
    timestamp = time.strftime('%H:%M:%S')
    types = {0: Color.b + 'INFO',
             1: Color.g + 'DONE',
             2: Color.y + 'WARN',
             3: Color.r + 'FAIL'}
    prompt = '[{}] [{}{}] {}'.format(timestamp, types[n], Color.x, message)

    if n == 3:
        print(prompt)
        exit(1)

    elif use_print:
        print(prompt)
    else:
        return prompt


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                   CHECKING SETTINGS AND LOADING MODULES                     #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


try:
    log('yt2vk-video-importer is started!', 0)
    log('Checking for settings…', 1)
    for n in settings:
        if not settings[n]:
            raise ValueError
    log('Settings are loaded!', 1)
    log('Checking for modules…')
    import vk
    import requests as r
    log('Modules are loaded!', 1)
except ValueError:
    log('Something wrong with settings!', 3)
except KeyboardInterrupt:
    log(error_interrupt, 3)
except ModuleNotFoundError:
    log('Missing modules! Execute: sudo pip3 install vk requests', 3)
except:
    log('Unknown error!', 3)


youtube_api_key = settings['youtube_api_key']
youtube_channel = settings['youtube_channel']
vk_login = settings['vk_login']
vk_password = settings['vk_password']
vk_app_id = settings['vk_app_id']
vk_group_id = settings['vk_group_id']


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                                AUTHORIZING VK                               #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


try:
    log('Authenticating to VK…')
    session = vk.AuthSession(vk_app_id,
                             vk_login,
                             vk_password,
                             scope='video')
    api = vk.API(session)
    log('Authenticated!', 1)
except KeyboardInterrupt:
    log(error_interrupt, 3)
except:
    log('Wrong VK credentials or overusing VK API!', 3)


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#             RESOLVING CHANNEL NAME AND MAKING A LIST WITH VIDEOS            #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


api_url = 'https://www.googleapis.com/youtube/v3/'
video_url = 'https://www.youtube.com/watch?v='
pl_url = '{}playlistItems?part=snippet&maxResults=50&pageToken=' \
         '{}&playlistId={}&key={}'


if youtube_channel.startswith('UC') and len(youtube_channel) == 24:
    log('Detected YouTube channel ID!')
    channel_video = '{}channels?&part=contentDetails&id={}&key={}'
    channel_data = '{}channels?&part=snippet,id&id={}&title&key={}'
else:
    log('Detected YouTube username!')
    channel_video = '{}channels?part=contentDetails&forUsername={}&key={}'
    channel_data = '{}channels?&part=snippet,id&forUsername={}&title&key={}'


def get_video_list():
    try:
        log('Collecting videos…')
        videos = []
        fetched = False
        load = r.get(channel_video.format(api_url, youtube_channel,
                                          youtube_api_key))
        read = load.json()
        pl_data = (read['items'][0]['contentDetails']['relatedPlaylists']
                       ['uploads'])
        load.close()
        next_page_token = ''
        while not fetched:
            try:
                load = r.get(pl_url.format(api_url, next_page_token, pl_data,
                                           youtube_api_key))
                read = load.json()
                if read['nextPageToken']:
                    next_page_token = read['nextPageToken']
                    returned_videos = read['items']
                    for video in returned_videos:
                        videos.append(video_url +
                                      video['snippet']['resourceId']
                                           ['videoId'])
            except:
                returned_videos = read['items']
                for video in returned_videos:
                    videos.append(video_url +
                                  video['snippet']['resourceId']['videoId'])
                fetched = True

        load = r.get(channel_data.format(api_url, youtube_channel,
                                         youtube_api_key))
        channel_title = load.json()['items'][0]['snippet']['title']
        load.close()
        log('Collected {} videos from {}!'
            .format(len(videos), channel_title), 1)
        return videos[::-1]

    except KeyboardInterrupt:
        log(error_interrupt, 3)
    except:
        log('Unknown error!', 3)


video_list = get_video_list()
video_total = len(video_list)


def upload(n):
    uploaded = False
    video = api.video.save(link=video_list[n],
                           group_id=vk_group_id,
                           description=video_list[n])
    r.get(video['upload_url'])
    uploaded = True


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                   SETTING THE POSITIONS AND UPLOADING VIDEOS                #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


while True:
    try:
        start_at = input(log('Start from [1-{}]: '
                         .format(video_total), 2, False))
        if start_at == '':
            log(value_empty, 2)
        elif int(start_at) <= 0:
            log(value_less.format('1'), 2)
        elif int(start_at) > video_total:
            log(value_more.format(video_total), 2)
        else:
            start_at = int(start_at)
            break
    except KeyboardInterrupt:
        log(error_interrupt, 3)
    except ValueError:
        log(value_int, 2)
    except:
        log('Unknown error!', 3)


while True:
    try:
        finish_at = input(log('Finish at [{}-{}]: '
                          .format(start_at, video_total), 2, False))
        if finish_at == '':
            log(value_empty, 2)
        elif int(finish_at) < start_at:
            log(value_less.format(start_at), 2)
        elif int(finish_at) > video_total:
            log(value_more.format(video_total), 2)
        else:
            finish_at = int(finish_at)
            break
    except KeyboardInterrupt:
        log(error_interrupt, 3)
    except ValueError:
        log(value_int, 2)


count = finish_at - start_at + 1

log('Click CTRL+C! for pause!', 2)
log('Importing {} videos [{}-{}]…'.format(count, start_at, finish_at))
time_started = time.time()
uploaded = False
for n in range(start_at - 1, finish_at):
    try:
        upload(n)
        log(video_imported.format(n + 1, video_list[n]))
    except KeyboardInterrupt:
        print()
        while True:
            try:
                stop = input(log(import_paused.format(n + 1), 2, False))
                if stop == '':
                    if not uploaded:
                        upload(n)
                        log(video_imported.format(n + 1, video_list[n]))
                        break
                    else:
                        break
            except KeyboardInterrupt:
                log(error_interrupt, 3)
    except:
        while True:
            log(retrying_upload.format(n + 1), 2)
            if not uploaded:
                upload(n)
                log(video_imported.format(n + 1, video_list[n]))
                break


# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #
#                                    END                                      #
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - #


time_passed = round(time.time() - time_started)
log('{} videos are imported in {} seconds!'.format(count, time_passed), 1)
exit()
