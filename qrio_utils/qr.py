import pyqrcode
import io
from PIL import Image
import math


def generate_qr_image(data, file=None, error='Q', image_format='svg',
                      scale=4, custom_inlay=None, inlay_size=0.4):
    code = pyqrcode.create(data, error=error)
    stream = io.BytesIO()

    if image_format == 'svg':
        code.svg(file=stream, scale=scale)
        if custom_inlay:
            raise ValueError('inlay is not allowed for image_format="svg"')
    elif image_format == 'png':
        code.png(file=stream, scale=scale)
        if custom_inlay:
            _add_custom_inlay(stream, custom_inlay, inlay_size)
    else:
        raise ValueError(
            'invalid value for image_format: {}'.format(image_format))

    image = stream.getvalue()
    stream.close()

    if file:
        with open(file, 'wb') as f:
            f.write(image)

    return image


def generate_qr_string(data):
    code = pyqrcode.create(data)
    return code.terminal(module_color='black', background='white')


def _add_custom_inlay(stream, file, inlay_size):
    stream.seek(0)
    background = Image.open(stream, mode='r')
    foreground = Image.open(file, mode='r')
    foreground = foreground.resize(
        (math.floor(s*inlay_size) for s in background.size),
        resample=Image.NEAREST)
    img_w, img_h = foreground.size
    bg_w, bg_h = background.size
    offset = (math.floor((bg_w - img_w) / 2), math.floor((bg_h - img_h) / 2))

    background.paste(foreground, offset, foreground)
    stream.seek(0)
    background.save(stream, 'png')