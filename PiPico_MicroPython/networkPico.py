import network
import socket
from machine import Pin


def connect_wifi(ssid, password):
    station = network.WLAN(network.STA_IF)
    station.active(True)
    station.connect(ssid, password)

    while station.isconnected() == False:
        pass

    print('Connection successful')
    print(station.ifconfig())
    
led = Pin("LED", Pin.OUT)

def web_page():
    if led.value():
        gpio_state="ON"
    else:
        gpio_state="OFF"

    html = """<html><body><h1>ESP Web Server</h1>
    <p>GPIO state: <strong>""" + gpio_state + """</strong></p>
    <p><a href="/?led=on"><button>ON</button></a></p>
    <p><a href="/?led=off"><button>OFF</button></a></p>
    </body></html>"""
    return html

def start_web_server():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(('', 8080))
    s.listen(5)

    while True:
        conn, addr = s.accept()
        request = conn.recv(1024)
        request = str(request)
        led_on = request.find('/?led=on')
        led_off = request.find('/?led=off')

        if led_on == 6:
            print('LED ON')
            led.value(1)
        if led_off == 6:
            print('LED OFF')
            led.value(0)

        response = web_page()
        conn.send('HTTP/1.1 200 OK\n')
        conn.send('Content-Type: text/html\n')
        conn.send('Connection: close\n\n')
        conn.sendall(response)
        conn.close()

ssid = 'ssid'
password = 'pass'
    
def main():
    connect_wifi(ssid, password)
    start_web_server()

if __name__ == "__main__":
    main()