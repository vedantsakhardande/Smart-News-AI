import scrapy
import hashlib
from urllib.parse import quote


class ScreenshotPipeline(object):
    """Pipeline that uses Splash to render screenshot of
    every Scrapy item."""

    SPLASH_URL = "https://www.ndtv.com/top-stories/page-1"

    def process_item(self, item, spider):
        encoded_item_url = quote(item["https://www.ndtv.com/top-stories/page-1"])
        screenshot_url = self.SPLASH_URL.format(encoded_item_url)
        request = scrapy.Request(screenshot_url)
        dfd = spider.crawler.engine.download(request, spider)
        dfd.addBoth(self.return_item, item)
        return dfd

    def return_item(self, response, item):
        if response.status != 200:
            # Error happened, return item.
            return item

        # Save screenshot to file, filename will be hash of url.
        url = item["https://www.ndtv.com/top-stories/page-1"]
        url_hash = hashlib.md5(url.encode("utf8")).hexdigest()
        photo = "{}.png".format(url_hash)
        with open(photo, "wb") as f:
            f.write(response.body)
        # Store filename in item.
        item["screenshot_filename"] = photo
        return item