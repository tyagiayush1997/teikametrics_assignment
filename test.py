import unittest
import random
import string
import os
from teikametrics import shorten,convert_file_shorten,shortenedurl

filepathbasic = os.getcwd() + "/"

class TestShortner(unittest.TestCase):
	def test_url_shortner(self):
		"""
		Test that the shortend url has just 6 letters
		can change url to any other url and it will pass 
		"""
		url = "https://medium.com/front-end-weekly/reactjs-hoc-how-to-inject-dependencies-to-react-component-in-angularjs-way-a2fc63d795c8"

		result = shorten(url=url)
		urlbasic = "https://teikametrics/"
		self.assertEqual(len(result), len(urlbasic)+6)

	def test_convert_file_shortner(self):
		"""
		Test that the cnvert file shorten converts exactly the same number of urls to shorten urls
		as given and not more 
		"""
		list1 = ["https://websitebuilders.com","https://www.facebook.com/Learn-the-Net-330002341216/\n",
		"https://en.wikipedia.org/wiki/Internet#Terminology\n","https://www.google.com/dahvavacahcvaddvcagcvac/cahsvcgcagchvagcvadghcd/cadjhcjdavcjgadvgdc\n"]
		file = filepathbasic + ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(10))
		convert_file_shorten(list1=list1,start=0,next_step=50,file=file)
		with open(file,'r') as fp:
			data = fp.readlines()
		os.remove(file)
		self.assertEqual(len(data),len(list1))

	def test_getshortendurl_for_file(self):
		"""
		Test that the shortend url takes a filepath and filepathbasic and return a filepath for the same
		the no of urls converted is same as the no of urls inputted 
		the no of duplicate in converted urls is equal to zero
		"""
		filecheckpath = filepathbasic + "testurl.txt"
		fileabspath = shortenedurl(filepath=filecheckpath,endfilepath=filepathbasic)
		with open(filecheckpath,'r') as fp:
			data1 = fp.readlines()
		with open(fileabspath,'r') as fp:
			data2 = fp.readlines()
		os.remove(fileabspath)
		set1 = set()
		count = 0
		for data in data2:
			val = data.strip().split(":")[1]
			if val in set1:
				count +=1
			else:
				set1.add(val)

		self.assertEqual(count,0)
		self.assertEqual(len(data2),10000)
		self.assertEqual(len(data1),len(data2))

if __name__ == '__main__':
	unittest.main()