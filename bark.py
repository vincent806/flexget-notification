from http import HTTPStatus
import xml.etree.ElementTree as ET

import requests
from loguru import logger
from requests.exceptions import RequestException

from flexget import plugin
from flexget.config_schema import one_or_more
from flexget.event import event
from flexget.plugin import PluginWarning
from urllib import parse

plugin_name = 'bark'
logger = logger.bind(name=plugin_name)


class BarkNotifier:
    """
    Author: vincent806
    Date: 05Dec2021
    Description: support bark notification for flexget
    Usage: put this file to plugin folder of flexget

    Example config:

    notify:
      entries:
        title: "{{ task }}"
        message: "{{ title }}"
        via:
          - bark:
              barkurl: https://yoururl/yourtoken/
              # optional parameters below:
              group: yourgroup
              automaticallyCopy: 1
              isArchive: 1
              url: https://www.google.com
              icon: https://www.google.com/images/branding/googlelogo/2x/googlelogo_color_272x92dp.png
              level: timeSensitive
              sound: bell
    """

    schema = {
        'type': 'object',
        'properties': {
            'barkurl': {'type': 'string'},
            'group': {'type': 'string'},
            'automaticallyCopy': {'type': 'string'},
            'isArchive': {'type': 'string'},
            'url': {'type': 'string'},
            'icon': {'type': 'string'},
            'level': {'type': 'string'},
            'sound': {'type': 'string'},
        },
        'required': ['barkurl'],
        'additionalProperties': False,
    }

    def notify(self, title, message, config):
        """
        Send a bark notification
        """

        # initialize data
        data = {}

        baseurl = config.get('barkurl')
        if not baseurl.endswith("/"):
            baseurl = baseurl + "/"

        #handle optional parameters
        group = config.get('group')
        automaticallyCopy = config.get('automaticallyCopy')
        isArchive = config.get('isArchive')
        url = config.get('url')
        icon = config.get('icon')
        level = config.get('level')
        sound = config.get('sound')

        if group is None:
            group = "default"

        data['group'] = group

        if automaticallyCopy is not None:
            data['automaticallyCopy'] = automaticallyCopy
        if isArchive is not None:
            data['isArchive'] = isArchive
        if url is not None:
            data['url'] = url
        if icon is not None:
            data['icon'] = icon
        if level is not None:
            data['level'] = level
        if sound is not None:
            data['sound'] = sound

        # if title is
        if(len(title)>0):
            data['title'] = title

        # trim down the length to 5000 in order to avoid server error - the server limit is 5000
        if (len(message)>5000):
            message_tuned = message[0:5000]
        else:
            message_tuned = message
        data['body'] = message_tuned

        try:
            response = requests.post(baseurl,data)
        except RequestException as e:
            if e.response is not None:
                if e.response.status_code in (HTTPStatus.UNAUTHORIZED, HTTPStatus.FORBIDDEN):
                    message = 'Invalid Bark access token'
                else:
                    message = e.response.json()['error']['message']
            else:
                message = str(e)
            raise PluginWarning(message)


@event('plugin.register')
def register_plugin():
    plugin.register(BarkNotifier, plugin_name, api_ver=2, interfaces=['notifiers'])
