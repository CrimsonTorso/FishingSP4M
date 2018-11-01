import os, random, requests, json, string #Importing external packages.

chars = string.ascii_letters + string.digits + '!@#$%^&*()' #Sets the random ascii chars to have '!@#$%^&*()'.
random.seed = (os.urandom(1024)) #setting random seed to 1024.

url = 'DIRECT URL OF PHISHING LINK GOES HERE' #Defines the login URL.

names = json.loads(open('names.json').read()) #Defines 'names' equal to json command for opening and reading names.json

for name in names: #loop start for names
	name_extra = ''.join(random.choice(string.digits)) #allow for an extra join of random numbers & letters.

	username = name.lower() + name_extra + '@gmail.com' #Include @gmail.com at the end of username.
	password = ''.join(random.choice(chars) for i in range(8)) #Include random password.

	requests.post(url, allow_redirects=False, data={ #requests a post on the URL defined above * disallow forced redirects.
		'asdasdasd' : username, #Example username
		'adadadsasdads': password #Example password
		})
	print 'username %s and password %s has been sent: ' % (username, password) #prints something in CLI to show what is being sent.
	
	# Coded By CrimsonTorso
