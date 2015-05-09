QR-IO
============
A utility for using android as stdin device for barcodes


## Usage
### Main
```
usage: main.py [-h] {upload,io,qr} ...

QR-IO Service

positional arguments:
  {upload,io,qr}

optional arguments:
  -h, --help      show this help message and exit
```

#### Upload
```
usage: main.py upload [-h] [-u USERNAME] [-p PASSWORD] [-s SERVER] [-o PORT]
                  [-w]

optional arguments:
-h, --help            show this help message and exit
-u USERNAME, --username USERNAME
                    ftp username
-p PASSWORD, --password PASSWORD
                    ftp password
-s SERVER, --server SERVER
                    ftp server
-o PORT, --port PORT  ftp port
-w, --watch           watch
```

#### IO
```
usage: main.py io [-h] [-d] [-e EXTERNAL_URI] [-p PORT]

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           debug
  -e EXTERNAL_URI, --external-uri EXTERNAL_URI
                        External hostname
  -p PORT, --port PORT  Port to listen to
```

#### QR
```
usage: main.py qr [-h] [-d DATA]

optional arguments:
  -h, --help            show this help message and exit
  -d DATA, --data DATA  data
```