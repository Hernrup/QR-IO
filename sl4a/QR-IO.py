try:
    import androidhelper as android
except ImportError:
    import android
import time

droid = android.Android()


def scan_code():
    scan = droid.scanBarcode().result
    result = [(scan['extras']['SCAN_RESULT'])]
    return 'u'.join(result)


def main():
    endpoint = scan_code()

    while True:
        data = scan_code()
        droid.makeToast(data)
        print('{}/{}'.format(endpoint, data))

main()