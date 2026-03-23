import numpy as np
import multiprocessing
import time
import os


if __name__ == '__main__':


    pce = 'F:\Project\jnd\jnd\pc_error.exe'
    path = ''
    Peak_value = 2047   # 11bit=2047   10bit=1023
    enc = ''        #
    dec = ''
    pcelog 'psnr.txt'
    
    os.system(pce + ' -a ' + enc + ' -b ' + dec + ' -l 1 -d 1 -d 1 -r ' + str(Peak_value) + ' --dropdups=2 --neighborsProc=1 >' + pcelog)
    
    
   
    
   

    