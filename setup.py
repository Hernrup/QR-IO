from setuptools import setup

setup(name='QR-IO',
      version='0.2',
      description='A utility for using android as stdin device for barcode',
      url='https://github.com/Hernrup/QR-IO',
      author='Mikael Hernrup',
      author_email='mikael@hernrup.se',
      license='MIT',
      packages=['qr_io', 'qr_io.utils', 'qr_io.web'],
      install_requires=[
          'CherryPy==3.7.0',
          'Flask==0.10.1',
          'pypng==0.0.17',
          'PyQRCode==1.1',
          'pyreadline==2.0',
          'qrcode==5.1',
          'watchdog==0.8.3',
          'Pillow==9.0.0',
          'PyAutoGUI==0.9.30'
          ],
      tests_require=['nose'],
      scripts=['bin/qr-io.py'],
      zip_safe=False)