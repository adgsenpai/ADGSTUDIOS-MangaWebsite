#!/usr/bin/env python3


### Importing Common stuffs
from urllib import request as req
import json
from user_agent import generate_user_agent
### Common data
class CommonThings:
    def __init__(self):

        
        

        # choose a random user agent
        user_agent = generate_user_agent()
        self.headers = {
            "user-agent" : user_agent,
            "accept-language" : "en-US,en;q=0.9",
            "referer" : "https://mangaowl.to/",
            "origin" : "https://mangaowl.to",
            "authority" : "api.mangaowl.to",
            "sec-fetch-dest" : "empty"            
        }

    def requestToWeb(self, url, **kwargs):
        if kwargs:
            self.headers.update(kwargs)
        self.request = req.Request(
            url,
            headers = self.headers
        )
        res = req.urlopen(self.request)
        self.webcontent = res.read()
        return self.webcontent

