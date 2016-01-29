'''import modules'''
from selenium import webdriver
from selenium.webdriver.common.keys import Keys 

#specify the browser
driver = webdriver.Firefox()

'''generate URL to UCSC browser ROI'''

#this is the email address to access the UCSC web browser GRCh37/hg19 - you dont need the hgsid to run the query.

#https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr21%3A33031567-33041570&hgsid=471541513_A7QcraU1HbeDyyHmy9zAjF7BJR4B

#URL break down in order. you don't need the hgsid to access the web page:
#&lastVirtModeType=default
#&lastVirtModeExtraState=
#&virtModeType=default
#&virtMode=0
#&nonVirtPosition=
#&position=chr21%3A33031567-33041570

'''variables for URL construction in the order to be constructed''' 
#you can run the base and still get to the home page
base = "https://genome.ucsc.edu/cgi-bin/hgTracks?db=hg19" 
#this is the additional URL tags in the homepage - these are all defaults
base_extension = '&lastVirtModeType=default&lastVirtModeExtraState=&virtModeType=default&virtMode=0&nonVirtPosition=&position=chr'
#this will have to be variable once tested
Chr = '12'
#a constant variable between the non-constant chromosome and genomic coordinate
chr_coord_separator = '%3A'
#the genomic coordinate needs to go through the expander to make sure the ROI conservation displayaed is more than just a single amino acid. 
#HNF1A Chr12 build 37:121426743
genomic_coordinate = '121426743'

'''function to expand the region of interest to 15 amino acids either side of the SNV genomic coordinate'''
def coord_expander(genomic_coordinate):
	up = int(genomic_coordinate) + 45
	down = int(genomic_coordinate) - 45
	ROI = str(down) + '-' + str(up)
	URL = base + base_extension + Chr + chr_coord_separator + ROI
	driver.get(URL)
	return

''''generate the URL to UCSC browser based on the ROI surrounding the specified genomic coordinate''' 
if __name__ == "__main__":
	coord_expander(genomic_coordinate)	

#to get the conservaton to display:
	#access the browser using the default URL and the specified location to generate a hgsid
	#extract the hgsid and feed it to 

#screenshot the results
#https://github.com/ponty/pyscreenshot/blob/master/README.rst

#save to file
#place saved file in a powerpoint

'''#navigate to the elements needed by name - use a for loop to iterate through a list containing the name of the check boxes that require clicking
for item in list_of_names:
	element = driver.find_element_by_name(item)
	if element = True:
		try:
			options = element.find_elements_by_tag_name("checked")
		except:
			element.click()
	assert element.find_elements_by_tag_name("checked"), item + " did not get clicked and may not be presented in the''' 
			
