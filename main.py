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
import random

def getRandomFortune():
# list of possilbe fortune
    fortunes = [
        "Smile Like You Mean It.",
        "Anger leads to fear. Fear leads to the darkside.",
        "There is no try. You either do or do not.",
        "Never dance with the devil in the pail moonlight.",
        "Today will be better than yesterday, but no better than tomorrow...",
        "Never tug on Superman's cape.",
        "Never spit into the wind.",
        "Don't take the mask off the Lone Ranger.",
        "You don't mess around with Jim.",
        "Take it easy.",
        ]
# randomly select one of the fortunes
    length=int(len(fortunes))
    index = random.randint(0, length-1)

    return fortunes[index]

class MainHandler(webapp2.RequestHandler):
    def get(self):
        header = "<h1>Fortune Cookie</h1>"

        fortune = "<strong>" + getRandomFortune() + "</strong>"
        fortune_sentence = "Your fortune: " + fortune
        fortune_paragraph = "<p>" + fortune_sentence + "</p>"

        lucky_Number = "<strong>" + str(random.randint(1,100)) + "</strong>"
        number_sentence = 'Your lucky number: ' + str(lucky_Number)
        number_paragraph  = "<p>" + number_sentence + "</p>"

        cookie_again_button = "<a href='.'><button>Another cookie please :)</button></a>"

        content = header + fortune_paragraph + number_paragraph + cookie_again_button
        self.response.write(content)




app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
