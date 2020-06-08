import argparse
import os
import threading
import sys
import validators
import hashlib
import base64
import uuid
import string
import random
import traceback
if os.getcwd() not in sys.path:
	sys.path.append(os.getcwd())



def shortenedurl(url=None,filepath=None,endfilepath=None):
	'''
	Shorten Function :
	received:-
		1.url(optional) : to convert a single url to a shortened url and return
		2.filepath(optional) : to convert all urls from txt file to shortened url
		3.endfile(optional) : to redirect shortened urls for a particular file to a new file and return the full path
	if the file is used all the files are divide in batches of 50 and used in threads so as to increase delay time in case
	of sequential implementation.
	we can use multiprocessing also so as to use the multiprocessors of the system as per system 
	configurations
	'''
	try:
		if url is None and filepath is None:
			raise Exception("Url and Filepath can't be both None")
		if url is not None and filepath is not None:
			raise Exception("You can either provide url or filepath but not both")
		if url is not None:
			mainurl = shorten(url)
			return mainurl
		else:
			if endfilepath is not None:
				file_name = endfilepath + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(10))
			else:
				file_name=None
			temp_data={}
			temp_data["active_threads"] = []
			with open(filepath,"r") as fp:
				data = fp.readlines()
			for i in range(0,len(data),50):
				thread = threading.Thread(target=convert_file_shorten, args=(data,i,i+50,file_name))
				thread.start()
				if thread not in temp_data['active_threads']:
					temp_data['active_threads'].append(thread)
			for active_thread in temp_data['active_threads']:
				active_thread.join()
			if endfilepath is not None:
				return file_name
	except Exception as e:
		traceback.print_exc()



def shorten(url):
	'''
	this function does the main part of converting the url into shorthand url
	module used:-
		1 - uuid :- to generate a unique id everytime a user enters a url to be shortened 
			#### if you want to get same shortend url for same url than u can just remove uuid 
			part from url
		2. hashlib :- to genrate sha256sum of the url that is unique in itself
		3. base64 : - to encode a url into base64 url safe and use 6 values as shorthand url as it will 
				generate 64*64*64*64*64*64 keys so the possiblity of same keys present is minimum
	'''
	try:
		if not isinstance(url,str):
			raise Exception("url passed should be a string")
		if validators.url(url) is not True:
			raise Exception("url passed is not a valid url")		
		url = url  + str(uuid.uuid4()) ### remove uuid if u want to get same url for a same url submitted multiple times
		urldigest = hashlib.sha256(url.encode("utf-8")).hexdigest()
		baseencode = base64.urlsafe_b64encode(urldigest.encode("utf-8"))
		mainurl = "https://teikametrics/" + str(baseencode[:6],"utf-8")
		return mainurl
	except Exception as e:
		traceback.print_exc()


def convert_file_shorten(list1,start,next_step,file):
	'''
	this is used to convert the long url to short urls while reading from a  file.
	if file is given and not none this function will append the shortend urls to that file
	in "url - shorthandurl" format or print on console if file not present
	'''
	try:
		if file is not None:
			with open(file,'a') as fp:
				while(start<next_step and start<len(list1)):
					#print(start)
					url_short = shorten(list1[start].strip())
					fp.write(list1[start].strip() + " :" + url_short + " \n")
					start += 1
		else:
			while(start<next_step and start<len(list1)):
				url_short = shorten(list1[start].strip())
				print(list1[start].strip() + " :" + url_short + " \n")
				start +=1
	except Exception as e:
		traceback.print_exc()

if __name__ == "__main__":
	''' 
	Argparse to parse arguments from command line and provide help to user while
	using the given module
	'''
	parser = argparse.ArgumentParser(description="Url Shortner created , use only one of url or file path option",)
	parser.add_argument("-f", "--file", help="Url shortening file", required=False)
	parser.add_argument("-u", "--url", help="Url to be shortened", required=False)
	parser.add_argument("-p", "--path", help="Provide Path if want to enter the shortened urls of given file to a new file , if left blank will print on console", required=False)
	args = parser.parse_args()
	print(shortenedurl(args.url,args.file,args.path))

