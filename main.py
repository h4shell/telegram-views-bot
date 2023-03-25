from time import sleep as swait
from utilitys import auto_loader, input_loader
from threading import Thread, active_count, Event
from auto_proxy import Proxy
from telegram import Api
import random

THREADS = 500
logo = '''
   ~ Telegram Auto Views V2 ~
     ~ github.com/TeaByte ~
          ~ @TeaByte ~
'''

channel, post = input_loader("https://t.me/OfferteAmazon2025/193")

print(logo)


def start(num):

    event = Event()

    http, socks4, socks5 = auto_loader()

    auto = Proxy(http_sources=http, socks4_sources=socks4,
                 socks5_sources=socks5)
    api = Api(channel, post=num)
    views = Thread(target=api.views, args=(event,)).start()
    tui = Thread(target=api.tui, args=(event, logo, THREADS)).start()

    threads = []
    auto.init()
    for proxy_type, proxy in auto.proxies:
        while active_count() > THREADS:
            swait(0.05)
        thread = Thread(target=api.send_view, args=(proxy, proxy_type))
        threads.append(thread)
        thread.start()
        try:
            if int(api.real_views) > random.randint(800, 999):
                event.set()
                break
        except:
            event.set()
            break

    for t in threads:
        t.join()
        num = str(int(num) + 1)

        # views = Thread(target=api.views, args=(event,)).start()
        # tui = Thread(target=api.tui, args=(event, logo, THREADS)).start()
        start(num)


start(post)
