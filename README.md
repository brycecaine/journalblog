journalblog
===========

Blogified journals via pelican

## Local setup
#### Install & configure pelican
```
pip install pelican markdown
```
On the next command, choose ssh as the option to update the site.
* SSH_HOST=localhost
* SSH_PORT=<<<ssh port>>>
* SSH_USER=root
* SSH_TARGET_DIR=/usr/share/nginx/www
```
pelican-quickstart
```
```
put server-user's public key in root's authorized_keys file
```

#### Cron entry
```
PATH=<<<your PATH environment variable>>>
* * * * * cd <<<project path>>>/journalblog && make rsync_upload >> <<<log path>>>/jb_log.txt 2>&1
```

#### Link to external content
```
ln -s <<<path to mounted external-files directory>>> <<<project path>>>/journalblog/content
```

#### Install nginx
sudo apt-get install nginx

## Create journal entry
* Create markdown file in location that's synced up to your external file directory
* Add any referenced pics to the same folder
