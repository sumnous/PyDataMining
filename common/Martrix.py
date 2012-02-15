#!/usr/bin python
#encoding: utf-8

class Matrix(object):
    def __init__(self, cols, rows):
        self.cols = cols
        self.rows = rows
        self.matrix = []
        for i in range(rows):
            ea_row = []
            for j in range(cols):
                ea_row.append(0)
            self.matrix.append(ea_row)

    def set_item(self, col, row, v):
        self.matrix[col - 1][row - 1] = v

    def get_item(self, col, row):
        return self.matrix[col - 1][row - 1]

    def __repr__(self):
        out_str = ""
        for x in range(self.rows):
            out_str += '%s\n' % (self.matrix[x])
        return out_str


#a = Matrix(4,4)
#print a
#a.set_item(3,4,'55.75')
#print a
#a.set_item(2,3,19.1)
#print a
#print a.get_item(3,4)
