Kiln API
==================

An API for controlling a kiln

Install
-------
sudo python setup.py install

Usage
-----

    kilnapi [-h] [-d] [-f] [-P [PIDFILE]]
    
    Kiln controller API daemon
    
    optional arguments:
      -h, --help            show this help message and exit
      -d, --daemon          run in the background
      -f, --foreground      run in the foreground
      -P [PIDFILE], --pidfile [PIDFILE]    pid file for use with service script

Start manually:

    sudo kilnapi -d
    
Start with the service script::

    sudo service kilnapi start
