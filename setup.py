from setuptools import setup

APP = ['batterychecker.py']
DATA_FILES = ["icon"]
OPTIONS = {
    'iconfile':'icon.icns',
    'argv_emulation': True,
    'plist': {
        'LSUIElement': True,
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    name='ばってりーちぇっかー。',
    setup_requires=['py2app'],
)