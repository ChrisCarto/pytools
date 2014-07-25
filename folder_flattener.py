import os, shutil

def deFolder(delete_original):
	"""
	delete_original: true or false. true removes folders after it pulls the contents, false leaves it

	for this to currently work, drop this script into a directory with a bunch of files in folders. it currently only goes one level deep
	todo: add parameter to go entire depth of input dir
	"""
	if((delete_original == 'True') or (delete_original == 'true')):
		delete_original == True
	else:
		delete_original == False

	for f in os.listdir('.'):
		if os.path.isdir(f):
			for e in os.listdir(f):

				shutil.copyfile(f+'/'+e, e)
			if(delete_original == True):
				shutil.rmtree(f)
			else:
				pass

deFolder(True)