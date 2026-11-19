# tcp-chat-python

Python ile yazılmış, thread kullanan küçük bir TCP chat sunucusu ve istemcisi.
SIMSOFT stajımın başında soket programlama ve thread konularını çalışırken hazırladığım örnek.

## Ne yapıyor

- `server.py`: 65432 portunu dinler. Bağlanan her istemci için ayrı bir thread açar ve gelen mesajı diğer bütün istemcilere iletir.
- `client.py`: Sunucuya bağlanır. Gelen mesajları arka plandaki bir thread dinler, ana thread klavyeden okuduğunu gönderir.

## Çalıştırma

Python 3 yeterli, ek paket gerekmez.

```
python server.py
python client.py     # ayrı terminallerde, iki ya da daha fazla
```

Çıkmak için istemcide `exit` yazılır.

## Kullanılan kavramlar

- TCP soket akışı: `socket`, `bind`, `listen`, `accept`, `connect`, `sendall`, `recv`
- `recv` boş dönerse karşı tarafın bağlantıyı kapattığı anlaşılır
- Her bağlantı için bir thread (`threading.Thread`, `daemon=True`)

## Bilinen eksikler

- `clients` listesine birden fazla thread aynı anda erişiyor ve kilit (`threading.Lock`) yok. İstemci sayısı arttığında yarış durumu (race condition) oluşabilir.
- Mesaj sınırı yok: TCP bir bayt akışı olduğu için uzun ya da art arda gelen mesajlar bölünebilir veya birleşebilir.
- Sunucu için düzgün kapanma (Ctrl+C) ve `SO_REUSEADDR` ayarı yok.
