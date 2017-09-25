#!/usr/bin/python
import csv
import itertools

with open('test.txt', 'r') as in_file:
    lines = in_file.read().splitlines()
    stripped = [line.replace("--"," ").split() for line in lines]
    grouped = itertools.izip(*[stripped]*1)
    with open('test_out.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('Admission', 'Date'))
        for group in grouped:
            writer.writerows(group)
