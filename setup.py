from distutils.core import setup
setup(
  name = 'AudioRec',
  packages = ['AudioRec'],
  version = '0.1',
  license='MIT',
  description = 'Audio Recorder for python that lets you record WAV and MP3 Files from any input source',
  author = 'Joel Barmettler',
  author_email = 'joel.barmettler@uzh.ch',
  url = 'https://github.com/joelbarmettlerUZH/AudioRec',
  download_url = 'https://github.com/joelbarmettlerUZH/AudioRec/archive/v_01.tar.gz',
  keywords = ['Audio', 'Recording', 'Sound', 'music'],
  install_requires=[
          'pyaudio',
          'wave',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',

    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',

    'License :: OSI Approved :: MIT License',

    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
  ],
)