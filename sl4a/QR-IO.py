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
    if not scan:
        return None
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


def show_message(header, text):
    droid.dialogCreateAlert(header, text)
    droid.dialogSetPositiveButtonText('Ok')
    droid.dialogShow()
    droid.dialogGetResponse().result
    droid.dialogDismiss()


def show_yes_no(header, text):
    droid.dialogCreateAlert(header, text)
    droid.dialogSetPositiveButtonText('Yes')
    droid.dialogSetNegativeButtonText('No')
    droid.dialogShow()
    response = droid.dialogGetResponse().result
    droid.dialogDismiss()
    return 'which' in response and response['which'] == 'positive'


def register_reader():
    show_message(
        'Connect you reader',
        'Scan your system QR code now to connect this reader to the system'
    )

    try:
        endpoint = scan_code()

        show_message(
            'Reader successfully connected',
            'endpoint: {}'.format(endpoint)
        )
    except Exception as e:
        show_message(
            'ERROR',
            str(e)
        )

    return endpoint



def main():
    endpoint = register_reader()

    while True:
        data = scan_code()
        if not data:
            responce = show_yes_no(
                'Quit?',
                'No code was scanned, do you want to exit the scanner?')
            if responce:
                break
        droid.makeToast(data)
        make_request(endpoint, data)

main()