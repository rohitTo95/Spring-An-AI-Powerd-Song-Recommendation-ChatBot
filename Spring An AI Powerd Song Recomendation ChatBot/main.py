import eel
import sys


def close_callback(page, sockets):
    print("Closing the server...")
    sys.exit()

@eel.expose
def returnStr():
    str = "Hello I am a Button"
    return str
    
eel.init('web')
print("Starting Eel To Html File")
    
eel.start('welcome_page/index.html', size=(1200,600), port=8000, close_callback=close_callback)
# eel._websocket_close('welcome_page/index.html',close_callback=close_callback)

