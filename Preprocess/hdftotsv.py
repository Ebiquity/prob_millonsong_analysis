#!/usr/bin/env python

import h5py
from os import listdir
from os.path import *

def discover_files(path):

    h5Files = [ f for f in listdir(path) if isfile(join(path,f)) and  ".h5" in f ]

    return h5Files


def get_song_data_rows(filename):
    d = h5py.File(filename, "r")
    f = d['metadata/songs']
    row = [item for item in f]
    return row



def append_artist_data(data):


    with open("artist_data.tsv", "a") as h:
        for row in data:
            line = "\t".join(row)
            h.write(line)
            h.write("\n")



