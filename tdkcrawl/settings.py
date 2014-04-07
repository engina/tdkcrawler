# Scrapy settings for tdkcrawl project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'tdkcrawl'

SPIDER_MODULES = ['tdkcrawl.spiders']
NEWSPIDER_MODULE = 'tdkcrawl.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'tdkcrawl (+http://www.yourdomain.com)'
