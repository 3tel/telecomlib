from time import ctime

from telecomlib import __version__


def run():
    cur_time = ctime()
    text = f"""
    # wetel

    version {__version__} ({cur_time} +0800)
    """
    print(text)
