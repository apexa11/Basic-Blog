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
import os
import jinja2
import webapp2

from google.appengine.ext import db

#set templet directory
template_dir = os.path.join(os.path.dirname(__file__),'templates')
#add jinja environment
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir),
    autoescape = True)


class BlogHandler(webapp2.RequestHandler):
    def write(self,*a,**kw):
        self.response.out.write(*a,**kw)

    def render_str(self, template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template , **kw))

class MainHandler(BlogHandler):
    def get(self):
        self.write("hello Udacity")

# blog stuff

def blog_key(name = 'default'):
    return db.Key.from_path('blogs',name)

class post(db.Model):
    subject=db.StringProperty(required = True)
    content=db.TextProperty(required = True)
    created=db.DateTimeProperty(auto_now_add = True)
    last_modified = db.DateTimeProperty(auto_now = True)

    def render(self):
        self.render_text = self.conetent.replace('\n','<br>')
        return render_str('post.html', p = self)











app = webapp2.WSGIApplication([
    ('/', MainHandler),
], debug=True)
