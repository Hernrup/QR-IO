import pyqrcode
import io


def generate_qr_image(data, file, error='Q'):
    code = pyqrcode.create(data, error=error)
    code.svg(file, scale=3)


def generate_qr_string(data):
    code = pyqrcode.create(data)
    return code.terminal(module_color='black', background='white')


def generate_qr_image_to_memory(data, error):
    output = io.BytesIO()
    generate_qr_image(data, output, error)
    code = output.getvalue()
    output.close()
    return code