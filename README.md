PyXLS2PO
========

This Python script takes an XLS file and converts it to a PO file (for multilingual sites)

I was given an XLS file and told to make a PO file out of this for a Multilingual Drupal website.  The other soltuions i found were hard to use and/or didn't work right.  I came up with my own script for this method and have posted it here in hopes that someone who may need it, will find it.

The XLS file I used had 3 columns: Comments | English Translation | French Translation

Obviously this can be used for any number of languages beyond just French.

###Requirements:
 * XLRD - sudo pip install xlrd

###References:
 * <http://www.python-excel.org/>