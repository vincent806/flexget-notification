## 语言
[English](README.md) 中文

## 简介
本代码库主要是为了提供flexget的通知插件，目前支持以下的消息通道：

- [Bark](https://github.com/Finb/Bark)
- [ServerChan](https://sct.ftqq.com/)
- [PushPlus](https://www.pushplus.plus/)
- [Iyuu](https://iyuu.cn/)
- [DingTalk](https://open.dingtalk.com/document/robots/custom-robot-access)
- [FeiShu](https://www.feishu.cn/hc/zh-CN/articles/360024984973)
- [WxBot](https://developer.work.weixin.qq.com/document/path/91770)

## 使用方法
1. 复制python文件到flexget的plugins目录，通常情况下plugins文件夹是flexget config文件夹的子文件夹
2. 重启flexget
3. 根据以下的样例，配置你的flexget通知插件

- [Bark](https://github.com/Finb/Bark)
```
    notify:
      task:
        title: "种子下载开始"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          共 {{ group.list|length }} 个种子来自任务 {{ group.grouper }}:
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
        title: "种子下载开始"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          共 {{ group.list|length }} 个种子来自任务 {{ group.grouper }}:
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
        title: "种子下载开始"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          共 {{ group.list|length }} 个种子来自任务 {{ group.grouper }}:
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
        title: "种子下载开始"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          共 {{ group.list|length }} 个种子来自任务 {{ group.grouper }}:
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
        title: "种子下载开始"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          共 {{ group.list|length }} 个种子来自任务 {{ group.grouper }}:
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
        title: "种子下载开始"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          共 {{ group.list|length }} 个种子来自任务 {{ group.grouper }}:
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
        title: "种子下载开始"
        message: |+
          {%- if task.accepted -%}
          {%- for group in task.accepted|groupby('task') -%}
          共 {{ group.list|length }} 个种子来自任务 {{ group.grouper }}:
          {% for entry in group.list %}
          {{ loop.index }}: {{ entry.title }} 
          {%- endfor -%}
          {%- endfor -%}
          {%- endif -%}
        via:
          - wxbot:
              webhook: <your-webhook-url>
```
