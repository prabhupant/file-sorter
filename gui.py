from gi.repository import Gtk
from file_sorter import application

class MainWindow(Gtk.Window, application):
	
	
	
	def __init__(self):
		Gtk.Window.__init__(self, title = '')
		self.set_border_width(30)
		layout = Gtk.Box(spacing = 6)
		self.add(layout)
				
		button = Gtk.Button('Choose Directory')
		button.connect('clicked', self.on_file_clicked)
		layout.add(button)
		
	#user clicked the choose directory button
	def on_file_clicked(self, widget):
		
		dialog = Gtk.FileChooserDialog('Select a directory', self, Gtk.FileChooserAction.SELECT_FOLDER,('Cancel', Gtk.ResponseType.CANCEL, 'Ok', Gtk.ResponseType.OK))
		response = dialog.run()
		
		obj_application = application()
		
		if response == Gtk.ResponseType.OK:
			
			path = dialog.get_filename()
			obj_application.search_folders(path+'/')
			
		elif response == Gtk.ResponseType.CANCEL:
			print('User didnt choose any file')
		
		dialog.destroy()
	

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
