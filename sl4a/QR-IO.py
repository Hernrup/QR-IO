#qpy:console
#qpy:3
try:
    import androidhelper as android
except ImportError:
    import android

import json
import requests

droid = android.Android()


def scan_code():
    scan = droid.scanBarcode().result
    result = [(scan['extras']['SCAN_RESULT'])]
    return 'u'.join(result)


def make_request(endpoint, data):
    try:
        r = requests.post(
            endpoint,
            data=json.dumps(data),
            headers={'content-type': 'application/json'}
        )
        droid.makeToast('{}: {}'.format(r.status, data))
    except Exception as e:
        droid.makeToast('ERROR: {}'.format(str(e)))

def main():
    endpoint = scan_code()

    while True:
        data = scan_code()
        droid.makeToast(data)
        make_request(endpoint, data)


main()