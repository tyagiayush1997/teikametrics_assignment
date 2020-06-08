#URL Shortener:-

A urlshortener that shortens the long url to a short url.(teikametrics.py)

Ex:- 
input :- "https://medium.com/front-end-weekly/reactjs-hoc-how-to-inject-dependencies-to-react-component-in-angularjs-way-a2fc63d795c8"
output :- "https://teikametrics/X6Yste"
If you don't want the "https://teikametrics" change it to blank or replace it with something that suits you



##Installation Instructions :-
1. Clone the repository
2. Insatll virtual env to create a virtualenv for this.
	virtualenv -p python3 env
3. activate the virtual env .
	source env/bin/activate
4. install the dependencies.
	pip install -r requirements.txt
	
###How it works -
It takes a long URL or a txt File with URLs and return a shortened URL or a file with shortened URLs.
it generates unique shortened URL for same URL submitted again . To generate the same URL for same URL submitted again omit uuid field in shorten function.


###Parameters:-
1. -f filepath for which short urls to be generated
2. -p endfilepath where to put the file generated after converting the URLs from input file
3. -u single URL to be shortened

-f and -u can't be used  at the same time . ,  
-p if not provided will print all the values on console and not on file.


###How to EXECUTE the file:-
python3 teikametrics.py -h [give helps how to execute]

python3 teikametrics.py -u url [when you want to shorten a singleurl]

python3 teikametrics.py -f filepath -p path_where_you_want_output_file [if -p is blank then will print everything on console]

###How to use file as Library:-
Either add the teikametrics file to "/usr/lib/python3.6" and you can use it as normal python module file or place it in
~/.local/lib/pythonX.X/site-packages

or 

When u want to use it code:
import sys
sys.path.append("teikametrics.py file directory")
import teikamtrics
shortenedurl = teikametrics.shorten(url)
