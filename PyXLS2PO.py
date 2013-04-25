#!/usr/bin/env python
# -*- coding: utf-8 -*-

# File to create:
fileA = '/path/to/french.po'

# XLS file to access - expecting columns: comment | english | other translation
fileB = '/path/to/french_trans.xls'

import xlrd
import codecs
import os
import sys

reload(sys).setdefaultencoding("utf8")

print sys.getfilesystemencoding()
print ""
print sys.getdefaultencoding()
print ""

# Remove file, as to not append to.
os.remove(fileA)

f = codecs.open(fileA, mode='w', encoding='utf-8')

book = xlrd.open_workbook(fileB, encoding_override="utf-8")
worksheet = book.sheet_by_index(0)
num_rows = worksheet.nrows - 1
num_cells = worksheet.ncols - 1
curr_row = -1
while curr_row < num_rows:
  curr_row += 1
  row = worksheet.row(curr_row)
  line1 = unicode(row[0].value).replace('\n', '')
  line2 = unicode(row[1].value).replace('\n', '')
  line3 = unicode(row[2].value).replace('\n', '')

  # See output of the translated language, just for fun.
  print line3

  f.write(u"#: ")
  f.write(line1.encode('utf8'))
  f.write(u"\n")
  f.write(u"msgid \")
  f.write(line2.encode('utf8'))
  f.write(u"\"\n")
  f.write(u"msgstr \"")
  f.write(line3.decode('utf8'))
  f.write(u"\"\n\n")

f.close()