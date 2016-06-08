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
import webapp2
import jinja2
import os 

my_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('Hello world!')

class CountHandler(webapp2.RequestHandler):
    def get(self):
      my_variables = {"number" : [9,5,5,10]}
      count_template=my_env.get_template('templates/count.html')
      self.response.write(count_template.render(my_variables))

class PigHandler(webapp2.RequestHandler):
    def get(self):
      pig_template=my_env.get_template('templates/pig.html')
      self.response.write(pig_template.render())


    def post(self):
      def pigLatin(word):
        vowels = ["a", "e", "i", "o", "u"]
        if word[0].lower() in vowels:
          pig_latin_word = word + "ay"
        else:
          if word[1].lower() not in vowels:
            first_letters = word[:2]
            rest_of_word = word[2:]
            pig_latin_word = rest_of_word + first_letters + "ay"
          else:
            first_letter = word[0]
            rest_of_word = word[1:]
            pig_latin_word = rest_of_word + first_letter + "ay"
        return pig_latin_word

      pl_result = pigLatin(self.request.get ("user_word"))
      my_variables = {"translated_word": pl_result}
      pig_template=my_env.get_template('templates/pig.html')
      self.response.write(pig_template.render(my_variables))

# route, address book as to where you find things 
app = webapp2.WSGIApplication([
    ('/', MainHandler),
    ('/count', CountHandler),
    ('/piglatin', PigHandler)
], debug=True)
