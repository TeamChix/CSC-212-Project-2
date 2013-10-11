# 
# CSC 412 Fall 2013 - Project 2
# implement a prototype for a solution to project 1
# Selected Scenario - Housing Lottwery
# Selected Solution - Provide room availablity preview prior to room selection time
#                     
import web

__author__="US978847"
__date__ ="$Oct 3, 2013 12:47:14 PM$"

# Redirect to index.html file
class Index(object):
  def GET(self):
    raise web.seeother('../static/index.html');


urls = (
  '/', Index
);

if __name__ == "__main__":
  app = web.application(urls, globals(), True)
  app.run()
