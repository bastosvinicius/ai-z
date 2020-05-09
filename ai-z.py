#!/usr/bin/env python

import argparse
import sys
from hwinfo import DetectHardware, PrintHardwareInfo, gpuDevices, DisplayStats
from time import sleep
import curses

__version__ = '0.1'


def DisplayHelp():
    print("AI-Z usage")
    print("--help: display this page")
    print("--version: display version")
    print("--hwinfo: list hardware info")

def ParseCmdLine(argv):
    parser = argparse.ArgumentParser()
    parser.add_argument('--h', default=False, action='store_true')
    parser.add_argument('--version', default=False, action='store_true')
    parser.add_argument('--showhwinfo', default=False, action='store_true')

    #print(argv)
    args = parser.parse_args(argv)

    return args


def InitDisplay():
    return curses.initscr()

def DisplayMenu(win):
    win.addch('\n')
    win.addch('\n')
    win.addstr("q:Quit")

def Shutdown(win):
    curses.endwin()
    sys.exit(0)

def MainLoop(win):
    curses.start_color()
    curses.noecho()
    win.nodelay(True)

    while(True):
        #sleep(0.10)
        win.clear()
     
        DisplayStats(win)

        DisplayMenu(win)

        curses.cbreak()
        key = win.getch()
        curses.nocbreak()
        if key == 113:
            Shutdown(win)

        win.refresh()


def main(argv):
    args = ParseCmdLine(argv[1:])

    if args.h is True:
        DisplayHelp()

    if args.version is True:
        print("AI-Z version %d" % __version__)


    DetectHardware()
    
    if args.showhwinfo is True:
        PrintHardwareInfo()
        return

    win = None

    try:
        win = InitDisplay()
        MainLoop(win)
    except:
        Shutdown(win)


if __name__ == '__main__':
    main(sys.argv)