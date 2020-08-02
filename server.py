import cherrypy

from root import Root

if __name__ == '__main__':
    cherrypy.config.update({'server.socket_port': 443}) #port 443 for https or port 80 for http
#    cherrypy.config.update({'server.socket_port': 80})
    cherrypy.config.update({'server.socket_host': 'ec2-35-162-124-51.us-west-2.compute.amazonaws.com'})

    #cherrypy.tree.mount(Root())
    cherrypy.tree.mount(Root(),'/',

{ 

    '/robots.txt': { 'tools.staticfile.on': True, 'tools.staticfile.filename': '/home/ec2-user/server/robots.txt'  },
    '/video1.mp4': { 'tools.staticfile.on': True, 'tools.staticfile.filename': '/home/ec2-user/Joyeux Noel.mp4'  },
    
}

 )

    cherrypy.server.ssl_module = 'builtin'
    cherrypy.server.ssl_certificate = "/etc/letsencrypt/live/video.n-plat.com/fullchain.pem"
    cherrypy.server.ssl_private_key = "/etc/letsencrypt/live/video.n-plat.com/privkey.pem"
    cherrypy.server.ssl_certificate_chain = "/etc/letsencrypt/live/video.n-plat.com/fullchain.pem"
    cherrypy.server.thread_pool = 50


    cherrypy.engine.start()
    cherrypy.engine.block()

