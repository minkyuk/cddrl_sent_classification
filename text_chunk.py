class text_chunk:
	def __init__(self):
		self.raw_text_list = []
		self.rare_text_list = []
		self.filtered_text_list = []
		self.temp_wrapped_data = {}
		self.temp_allow_duplicate = False

	def unpopulate_(self):
		self.raw_text_list = []
		self.rare_text_list = []
		self.filtered_text_list = []

	def check_duplicate(self, s, l):
		if(s in l): return True
		return False

	def add_raw_text(self, text, doc_index, file_index):
		self.raw_text_list.append([doc_index, file_index, text])

	def add_rare_text(self, text, doc_index, file_index):
		self.rare_text_list.append([doc_index, file_index, text])

	def add_filtered_text(self, text, doc_index, file_index):
		self.filtered_text_list.append([doc_index, file_index, text])

	def add_all_text(self, raw_text, rare_text, filtered_text):
		self.filtered_text_list.append(text)
		self.rare_text_list.append(text)
		self.raw_text_list.append(text)

	#importing dictionary
	#We can be as strict as to check raw_text, or as loose as filtered_text. 
	#returns: whether if the text passed the duplicate test.

	def add_all_dict(self):
		wrapped_data = self.temp_wrapped_data
		allow_duplicate = self.temp_allow_duplicate	
		if not allow_duplicate:
			test_sent = wrapped_data['raw_text_data']
			if(self.check_duplicate(test_sent, self.raw_text_list)):
				print('duplicate detected.')
				return False;

		self.add_raw_text(
			[wrapped_data['doc_index'], wrapped_data['file_index'], wrapped_data['filtered_text_data']])
		self.add_rare_text(
			[wrapped_data['doc_index'], wrapped_data['file_index'], wrapped_data['rare_text_data']])
		self.add_filtered_text(
			[wrapped_data['doc_index'], wrapped_data['file_index'], wrapped_data['raw_text_data']])
		return True;


	def __str__(self):
		t = 'raw_text_list', len(self.raw_text_list), 
		'rare_text_list', len(self.rare_text_list), 
		'filtered_text_list', len(self.filtered_text_list)
		t = map(str, t)
		return t