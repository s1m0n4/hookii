#!/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import re
import numpy

'''
Created on Aug 18, 2015

   @author: s1m0n4
   @copyright: 2015 s1m0n4 for hookii.it
'''

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Indicare il file delle coordinate'
        exit(1)
    if not os.path.exists(sys.argv[1]):
        print 'Il file delle coordinate deve essere accessibile'
        exit(2)
    if not os.path.isfile(sys.argv[1]):
        print 'Un file, non una cartella'
        exit(3)
    with open(sys.argv[1], 'r+') as fo:
        lines = fo.readlines()
    if (lines is None) or (len(lines) <= 2):
        print 'Il file deve contenere coordinate di almeno 2 mhookii su più linee.'
        exit(4)
    
    longitudes = []
    latitudes = []
    tmp=0.0
    errors=0
    del lines[0] # la prima riga contiene i nomi delle colonne
    for line in lines:
        match = re.match(r"(.+?)\t([-+]?\d*\.\d+|\d+)\t([-+]?\d*\.\d+|\d+)", line)
        if match is None:
            print "errore nel processare la linea [%s]" % line
            errors += 1
            continue
        try:
            tmp = float(match.group(2))
        except ValueError:
            print "%s non é una longitudine valida" % match.group(2)
            errors += 1
            continue
        longitudes.append(tmp)
        try:
            tmp = float(match.group(3))
        except ValueError:
            print "%s non é una latitudine valida" % match.group(3)
            errors += 1
            continue
        latitudes.append(tmp)
    print "Processate %d linee, errori: %d" % (len(lines), errors)
    if (len(longitudes)>0) and (len(latitudes)>0):
        longitude = numpy.median(numpy.array(longitudes))
        latitude = numpy.median(numpy.array(latitudes))
        print "Longitudine: %.8f; Latitudine: %.8f" % (longitude, latitude)
    exit(0)
    