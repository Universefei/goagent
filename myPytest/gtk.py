#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk


# -----------------------------------------------------------------------------
# HelloWorld
# -----------------------------------------------------------------------------
Class HelloWorld:
    def hello(self, widget, data=None):
        print "Hello World"
    
    def delete_event(self, widget, event, data=None):
        print "delete event occurred"
        return False

    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init_(self):
        self.window = gtk.W

