tdk-crawler
========
TDK is the official governmental institution responsible for Turkish Language.

Underlying database is not available for public use. TDK kindly let me know that is not available due to licensing restrictions.

This tool fetches all the words from TDK for educational reasons. You can do various linguistic analysis as this should be the most comprehensive and authoritive Turkish vocabulary.

Usage:
----------

    scrapy crawl tdk
    
This will fetch create files under folder *d* with pattern letter_page.txt which you can later concatenate with

    cat *txt > dict.txt
    
Then you can also strip tralining commas in the line with

    ./stripcommas.py < dict.txt > dict-stripped.txt
    
Requirement
-----------------
This tool uses [Scrapy](http://scrapy.org). You can (hopefully) install it via:

    pip install scrapy