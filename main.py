#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import urllib2
from xml.dom import minidom

import webapp2

def get_traffic():
    url = "http://services.my511.org/traffic/getpathlist.aspx?token=29a0def9-03d8-45b7-a4af-4eeafd6dcbc7&o=332&d=276"
    content = None
    try:
        content = urllib2.urlopen(url).read()
    except urllib2.URLError:
        return
    if content:
        content = urllib2.urlopen(url).read()
        b = minidom.parseString(content)
        return b.getElementsByTagName("path")[0].childNodes[0].childNodes[0].nodeValue

class MainHandler(webapp2.RequestHandler):
    def get(self):
        c = get_traffic()
        print c
        self.response.write("%s" % c)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
