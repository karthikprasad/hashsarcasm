#!/usr/bin/env python

###
#
#
#
#
#
##

import webapp2
import jinja2
import os
import urllib

import humanpatterns
import machinepatterns

jinjaEnv = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.dirname(__file__)))

class MainPage(webapp2.RequestHandler):
  def get(self):
    template = jinjaEnv.get_template("./templates/index.html")
    self.response.out.write(template.render())


class Check(webapp2.RequestHandler):
  def post(self):
    tweet = urllib.unquote(self.request.get("t"))
    #print tweet

    mpRating = machinepatterns.getRating(tweet)
    hpRating = humanpatterns.getRating(tweet)
        
    rating = 0.71*hpRating + 0.29*mpRating
            
    if rating < 1.5:
      score = 1
    elif rating < 2.2:
      score = 2
    else:
      score = 3

    templateValues = {"score" : score}

    template = jinjaEnv.get_template("./templates/outcome.html")
         
    self.response.out.write(template.render(templateValues))


class AboutPage(webapp2.RequestHandler):
  def get(self):
    template = jinjaEnv.get_template("./templates/about.html")
    self.response.out.write(template.render())


app = webapp2.WSGIApplication([("/", MainPage),
                               ("/about", AboutPage),
                               ("/check", Check)
                              ],
                              debug=True
                             )
