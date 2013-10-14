# 
# start up a local server for project 2 demonstration
# need a python environment and web.py installed to run - http://webpy.org/
#
import web

__author__="CRyan"
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
