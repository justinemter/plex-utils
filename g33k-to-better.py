'''
WARNING: THIS WILL ALTER PLEX MEDIA TITLES WHEN RUN. KNOW WHAT YOU ARE DOING.

This script scans specified plex TV libraries searching for "bad_titles" like "g33k" and automatically replaces it with "Series Name Season # Episode - #". 

I recommend commenting out where it says "episode.edit(**new_title)"  on line 31 and do a dry run to see what is printed in your console first. 

Update the two list variables below under "Begin Editable". 

'''
from plexapi.server import PlexServer

#--- Begin Editable
baseurl = 'http://192.168.1.103:32400'
token = '<token>'
libs = ['TV Shows', 'TV']
bad_titles = ['g33k']
#--- End Editable

PLEX = PlexServer(baseurl, token)

sections = PLEX.library.sections()
for section in sections:
	if section.title.lower() in (item.lower() for item in libs):
		sectionMedia = PLEX.library.section(section.title).all()
		for i, media in enumerate(sectionMedia):
		    episodes = PLEX.library.section(section.title).get(media.title).episodes()
		    for episode in episodes:
		    	if episode.title.lower() in (item.lower() for item in bad_titles):
		    		new_title = {'title.value': episode.grandparentTitle + " " + episode.parentTitle + " Episode - " + str(episode.index)}
		    		episode.edit(**new_title)
		    		episode.reload()
    				print(episode.title)