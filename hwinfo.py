import os
import re
import numpy as np
from math import sin, pi
import sys
from gpu_amd import ListAMDGPUDevices
from gpu_nvidia import ListNVIDIAGPUDevices
from cpu import GetCPUDevice
from sparklines import sparklines


gpuDevices = []
cpuDevice = None

def DetectHardware():
    print('Detecting Hardware...')
    global gpuDevices
    global cpuDevice
    #GPU devices
    gpuDevices = ListAMDGPUDevices(False)
    gpuDevices.extend(ListNVIDIAGPUDevices())
    cpuDevice = GetCPUDevice()



# TODO
def PrintHardwareInfo():
    print('Hardware Info...')

    num_gpus = len(gpuDevices)
    print('NUM_GPUS:' + str(num_gpus))
    for i in range(0,num_gpus):
        print(gpuDevices[i].name)
        print(gpuDevices[i].id)
        print(gpuDevices[i].gpu_usage)
        


def DisplayStats(win):

    #COLOR_CYAN

    # Draw GPU Info
    for i in range(0, len(gpuDevices)):
        index = gpuDevices[i].MAX_SAMPLES-1

        win.addstr(gpuDevices[i].name)
      
        gpuDevices[i].Sample()
        
        
        #gpu usage
        win.addch('\n')
        win.addstr('USAGE  ')
        y=gpuDevices[i].gpu_usage
        line = sparklines(y,num_lines=2, minimum=0, maximum=100)
        win.addstr(line[0])
        win.addch('\n')
        win.addstr('%3d %%  ' % gpuDevices[i].gpu_usage[index])
        win.addstr(line[1])

        #vram usage
        #vram_size = 8 * 1024 * 1024 * 1024
        win.addch('\n')
        win.addch('\n')
        win.addstr('VRAM   ')
        y=gpuDevices[i].vram_usage
        line = sparklines(y,num_lines=2, minimum=0, maximum=100)
        win.addstr(line[0])
        win.addch('\n')
        win.addstr('%3d %%  ' % gpuDevices[i].vram_usage[index])
        win.addstr(line[1])
 
        
        #pcie bandwidth
        win.addch('\n')
        win.addch('\n')
        win.addstr('PCIE    ')
        y=gpuDevices[i].pcie_bw
        line = sparklines(y,num_lines=2, minimum=0, maximum=100)
        win.addstr(line[0])
        win.addch('\n')
        win.addstr('%3d MB/s' % gpuDevices[i].pcie_bw[index])
        win.addstr(line[1])
        
    #Draw CPU stats
    win.addch('\n')
    win.addch('\n')
    win.addstr('%s' % cpuDevice.name)
    win.addch('\n')
    cpuDevice.Sample()

    index = cpuDevice.MAX_SAMPLES-1
        
    #cpu usage
    win.addstr('USAGE  ')
    y=cpuDevice.cpu_usage
    line = sparklines(y,num_lines=2, minimum=0, maximum=100)
    win.addstr(line[0])
    win.addch('\n')
    win.addstr('%3d %%  ' % cpuDevice.cpu_usage[index])
    win.addstr(line[1])
    

    
