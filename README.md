## Description
This repository aims to provide notification plugin for flexget.  The following message channels are supported.

- [Bark](https://github.com/Finb/Bark)
- [ServerChan](https://sct.ftqq.com/)
- [PushPlus](https://www.pushplus.plus/)
- [Iyuu](https://iyuu.cn/)
- [DingTalk](https://open.dingtalk.com/document/robots/custom-robot-access)
- [FeiShu](https://www.feishu.cn/hc/zh-CN/articles/360024984973)
- [WxBot](https://developer.work.weixin.qq.com/document/path/91770)

## Usage
1. Copy the python files to plugins folder in flexget, ideally plugins folder is a subfolder in config folder.
2. Restart flexget
3. Refer to the following example to configure the notification plugin

- [Bark](https://github.com/Finb/Bark)
```
    notify:
      task:
        title: "Torrent download started"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          {{ group.list|length }} torrents from task {{ group.grouper }}:
          {% for entry in group.list %}
          {{ loop.index }}: {{ entry.title }} 
          {%- endfor -%}
          {%- endfor -%}
          {%- endif -%}
        via:
          - bark:
              barkurl: http://<your-url>/<your-key/
              group: flexget-message  #optional
              automaticallyCopy: "0"  #optional
              isArchive: "1"          #optional
              icon: "http://<iconurl>/<filename>.png"    #optional
              level: "active"           #optional
              sound: "birdsong"         #optional
```
- [ServerChan](https://sct.ftqq.com/)
```
    notify:
      task:
        title: "Torrent download started"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          {{ group.list|length }} torrents from task {{ group.grouper }}:
          {% for entry in group.list %}
          {{ loop.index }}: {{ entry.title }} 
          {%- endfor -%}
          {%- endfor -%}
          {%- endif -%}
        via:
          - serverchan:
              sckey: <your-sckey>
```
- [PushPlus](https://www.pushplus.plus/)
```
    notify:
      task:
        title: "Torrent download started"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          {{ group.list|length }} torrents from task {{ group.grouper }}:
          {% for entry in group.list %}
          {{ loop.index }}: {{ entry.title }} 
          {%- endfor -%}
          {%- endfor -%}
          {%- endif -%}
        via:
          - pushplus:
              token: <your-token>
```
- [Iyuu](https://iyuu.cn/)
```
    notify:
      task:
        title: "Torrent download started"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          {{ group.list|length }} torrents from task {{ group.grouper }}:
          {% for entry in group.list %}
          {{ loop.index }}: {{ entry.title }} 
          {%- endfor -%}
          {%- endfor -%}
          {%- endif -%}
        via:
          - iyuu:
              token: <your-token>
```
- [DingTalk](https://open.dingtalk.com/document/robots/custom-robot-access)
```
    notify:
      task:
        title: "Torrent download started"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          {{ group.list|length }} torrents from task {{ group.grouper }}:
          {% for entry in group.list %}
          {{ loop.index }}: {{ entry.title }} 
          {%- endfor -%}
          {%- endfor -%}
          {%- endif -%}
        via:
          - dingtalk:
              secret: <your-secret>
              webhook: <your-webhook-url>
```
- [FeiShu](https://www.feishu.cn/hc/zh-CN/articles/360024984973)
```
    notify:
      task:
        title: "Torrent download started"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          {{ group.list|length }} torrents from task {{ group.grouper }}:
          {% for entry in group.list %}
          {{ loop.index }}: {{ entry.title }} 
          {%- endfor -%}
          {%- endfor -%}
          {%- endif -%}
        via:
          - feishu:
              secret: <your-secret>
              webhook: <your-webhook-url>
```
- [WxBot](https://developer.work.weixin.qq.com/document/path/91770)
```
    notify:
      task:
        title: "Torrent download started"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          {{ group.list|length }} torrents from task {{ group.grouper }}:
          {% for entry in group.list %}
          {{ loop.index }}: {{ entry.title }} 
          {%- endfor -%}
          {%- endfor -%}
          {%- endif -%}
        via:
          - wxbot:
              webhook: <your-webhook-url>
```
