import sublime, sublime_plugin

class DollarCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		wordpos = self.view.word(self.view.sel()[0].end()-1)
		word = self.view.substr(wordpos)
		if self.view.substr(wordpos.begin()-1) is "$":
			if word not in DollarCommand.varlist:
				DollarCommand.varlist.append(word)
				
		elif word in DollarCommand.varlist:
			for pos in self.view.sel():
				self.view.insert(edit, wordpos.begin(), '$')
