#!/usr/bin/env python

import h5py
import os


def discover_files(path):
    res = []
    for root, dirs, files in os.walk(path):
        for filename in files:
            if '.h5' in filename:
                res.append(os.path.join(root[len(path):], filename))
    return res


def get_song_data_rows(filename):
    d = h5py.File(filename, "r")
    f = d['metadata/songs']
    row = [item for item in f]
    d.close()
    return row


def append_artist_data(data):
    with open("artist_data.tsv", "a") as h:
        for row in data:
            row_data = [str(item) for item in row ]
            line = "\t".join(row_data)
            h.write(line)
            h.write("\n")


if __name__ == "__main__":

    datadir = "../data/subset/cvt_large_test/"
    files = discover_files(datadir)
    for filename in files:
        print filename
        data_rows = get_song_data_rows(os.path.join(datadir, filename))
        append_artist_data(data_rows)


