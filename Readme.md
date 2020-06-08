###################################URL Shortener#######################################

It gives different shortened url for a given long url :
Note:- if you want to have same url for a single same url submittted multiple time than remove uuid field from shorten function 

It takes a long URL or a "txt" files with Urls separated by "\n" and provides shortened url in a file

example: - 
input :- "https://medium.com/front-end-weekly/reactjs-hoc-how-to-inject-dependencies-to-react-component-in-angularjs-way-a2fc63d795c8"
output :- "https://teikametrics/X6Yste"

if you don't want the "https://teikametrics" change it to blank or replace it with something that suits you


Argumnets supported:-
-f : file with urls that should be shortened
-u : url that needs to be shortened
-p : path of file u want to shorten a single url

-f and -u can't be used  at the same time . 
-p if not provided will print all the values on console and not on file.

######how to execute the file ####################

python3 teikametrics.py -h [give helps how to execute]

python3 teikametrics.py -u url [when you want to shorten a singleurl]

python3 teikametrics.py -f filepath -p path_where_you_want_output_file [if -p is blank then will print everything on console]

#############################Requirements##############################################
Python 3.6 and above
modules required :- argparse,os,threading,sys,hashlib,base64,uuid,string,random,unittest,validators

pip install -r requirements.txt



#########################Function implemented#######################################

shorten(url):-
expects an url to be shortened and return a shortened url .
ex:- "https://teikametrics/X6Yste" remove the first teikametrics part if you just want the six value unique key


shortenedurl(url=None,filepath=None,endfilepath=None):
expects one among url or filepath 
endfilepath is location where you want a file with output for input file(not mandatory will print on console otherwise)
uses multithreading to split a file with many urls into batches of 50 to improve execution time



convert_file_shorten(list1,start,next_step,file)

takes the original data list got from file and convert the urls to a shortened url and will print onto file if provided



########################To use the module as a normal module############################
Either add the teikametrics file to "/usr/lib/python3.6" and u can use it as normal python module file

or 

When u want to use it code:
import sys
sys.path.append("teikametrics.py file directory")
import teikamtrics
shortenedurl = teikametrics.shorten(url)




#############################Test File Description(test.py)#######################################

def test_url_shortner
		"""
		Test that the shortend url has just 6 letters
		can change url to any other url and it will pass 
		"""

def test_convert_file_shortner
		"""
		Test that the cnvert file shorten converts exactly the same number of urls to shorten urls
		as given and not more 
		"""

def test_getshortendurl_for_file
		"""
		Test that the shortend url takes a filepath and filepathbasic and return a filepath for the same
		the no of urls converted is same as the no of urls inputted 
		the no of duplicate in converted urls is equal to zero
		"""

##########################how to execute test file#################################

python3 test.py




