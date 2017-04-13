import json
import re

class Review:

    RATING_TAG = './/meta[@itemprop="ratingValue"]'
    USER_REGEX = '/cook/([A-Za-z_0-9]+)'

    def __init__(self):
        self.properties = {}

    def parseReview(self, review, id):
        self.properties['recipe'] = id
        self.parseAttributes(review)

    def parseAttributes(self, review):
        self.properties['rating'] = int(review.xpath(self.RATING_TAG)[0].get("content").strip())
        user_field = review.xpath('.//a')[0].get("href").strip()
        self.properties['user'] = re.match(self.USER_REGEX, user_field).group(1)
    def toJSON(self):
        return json.dumps(self.properties)
