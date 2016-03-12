import sublime, sublime_plugin

class DollarCommand(sublime_plugin.TextCommand):
	# read every word
    # if word is a variable and if it does not already exist in the list, add to list
    # else check if word exists in list
        # if yes, prefix $ in front of it 
        
    varlist=[]
    traillist=[" ","="]
    stringlist=["'",'"']
    count=0
    
	def run(self, edit):
		wordpos = self.view.word(self.view.sel()[0].end()-1)
		word = self.view.substr(wordpos)
		if self.view.substr(wordpos.begin()-1) is "$":
			if word not in DollarCommand.varlist:
				DollarCommand.varlist.append(word)
				
		elif word in DollarCommand.varlist:
			for pos in self.view.sel():
				self.view.insert(edit, wordpos.begin(), '$')
