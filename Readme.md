URL Shortener:-

A urlshortener that shortens the long url to a short url.(teikametrics.py)



Installation Instructions :-
1. Clone the repository
2. Insatll virtual env to create a virtualenv for this.
	virtualenv -p python3 env
3. activate the virtual env .
	source env/bin/activate
4. install the dependencies.
	pip install -r requirements.txt
	
How it works -
It takes a long URL or a txt File with URLs and return a shortened URL or a file with shortened URLs.
it generates unique shortened URL for same URL submitted again . To generate the same URL for same URL submitted again omit uuid field in shorten function.


Parameters:-
-f filepath for which short urls to be generated
-p endfilepath where to put the file generated after converting the URLs from input file
-u single URL to be shortened


