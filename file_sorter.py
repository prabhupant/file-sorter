import os

path = input('Enter the file path : ')

def search_folders(path):
	if os.path.exists(path):
		file_name = os.listdir(path)
		for filename in file_name:
			#for moving images
			if '.jpg' in filename or '.png' in filename:
				if not os.path.exists(path + 'Photos'):
					os.makedirs(path + 'Photos')
				os.rename(path + filename, path +'Photos/'+ filename)
			#for moving audios	
			elif '.mp3' in filename:
				if not os.path.exists(path + 'Music'):
					os.makedirs(path + 'Music')
				os.rename(path + filename, path +'Music/'+ filename)
			#for moving zip files	
			elif '.zip' in filename:
				if not os.path.exists(path + 'Zip'):
					os.makedirs(path + 'Zip')
				os.rename(path + filename, path +'Zip/'+ filename)
			#for moving pdfs	
			elif '.pdf' in filename:
				if not os.path.exists(path + 'PDF'):
					os.makedirs(path + 'PDF')
				os.rename(path + filename, path +'PDF/'+ filename)
			#for moving videos
			elif '.mp4' in filename or '.mp4' in filename or '.flv' in filename or '.wmv' in filename:
				if not os.path.exists(path + 'Videos'):
					os.makedirs(path + 'Videos')
				os.rename(path + filename, path +'Videos/'+ filename)
			#for moving documents	
			elif '.doc' in filename or '.docx' in filename:
				if not os.path.exists(path + 'Docs'):
					os.makedirs(path + 'Docs')
				os.rename(path + filename, path +'Docs/'+ filename)
			#for moving powerpoint files
			elif '.ppt' in filename or '.pptx' in filename:
				if not os.path.exists(path + 'Docs'):
					os.makedirs(path + 'Docs')
				os.rename(path + filename, path +'Docs/'+ filename)	
			
			else:
				if not os.path.exists(path + 'Misc'):
					os.makedirs(path + 'Misc')
				os.rename(path + filename, path +'Misc/'+ filename)				
		
		
search_folders(path)
