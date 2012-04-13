# -*- coding: utf-8 -*-
'''
============================================================================================
	Name        : Auto-Py-YUI-Compressor.py
	Author      : Artur Trzop
	Version     : 1.1.0
	Copyright   : MIT
	Description : Python script for auto compressing css and js files by YUI Compressor.
============================================================================================
'''

# ==========================================================================================
# START Config

### CSS settings
# relative path to directory where you keep css files
# remember to add slash at the end of path
relative_path_css = '../public_html/css/' 

# list of css files 
# Order of file names is significant. It's should be like in <meta> tag in the HEAD section of an HTML page.
list_css_files = ['reset.css', 'style.css'] 

# name of the minified css file
# this file will be placed in relative_path_css
output_css_min = 'allstyles.min.css' 
	

### JS settings	
# relative path to directory where you keep js files	
# remember to add slash at the end of path	
relative_path_js = '../public_html/js/' 

# list of js files
# Order of file names is significant. This is the order of running scripts.
list_js_files = ['jquery-1.7.2.js', 'jquery.cookie.js', 'jquery.easing.js', 'jquery.highlight.js', 'jquery.waypoints.js', 'myscripts.js'] 

# name of the minified js file
# this file will be placed in relative_path_js
output_js_min = 'allscripts.min.js' 

# END Config
# ==========================================================================================


import os
import subprocess
import shutil

counter = 1

def auto_py(relative_path, list_files, output_file):
	global counter
	
	print "# "+str(counter)
	counter += 1
	li = [] # empty list
	for file in list_files:
		li.append(open(relative_path+file).read())

	txt = "" # empty string
	for s in li:
		txt += "\n/* @next_file */\n"+s
		
	logfile = open('tmp/tmp_'+output_file, 'w')
	logfile.write(txt)
	logfile.close()

	print "Compressing files"
	subprocess.call("java -jar yuicompressor-2.4.7.jar --line-break 8000 -o tmp/"+output_file+" tmp/tmp_"+output_file);
	print "Copying output file to destination directory"
	shutil.copyfile('tmp/'+output_file, relative_path+output_file);
	
	os.remove('tmp/tmp_'+output_file)
	os.remove('tmp/'+output_file)
	
	return 

# ==========================================================================================


''' Compressing CSS files '''
auto_py(relative_path_css, list_css_files, output_css_min)

''' Compressing JS files '''
auto_py(relative_path_js, list_js_files, output_js_min)


print "\nDone!"
os.system("pause")
