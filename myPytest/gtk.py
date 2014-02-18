#!/usr/bin/env python

import sys
import os
import re
import thread
import base64
import platform

import pygtk
pygtk.require('2.0')
import gtk
gtk.gdk.threads_init()


# -----------------------------------------------------------------------------
# HelloWorld
# -----------------------------------------------------------------------------
class HelloWorld:
    def hello(self, widget, data=None):
        print "Hello World"
    
    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        self.window = gtk.W

def myMenu():
    menu = gtk.Menu()
    item = gtk.MenuItem("feilunzhou")
    item.show()
    menu.append(item)
    menu.show()

if __name__ == '__main__':
    myMenu()
