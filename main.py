
# Задача 1
class FlatIterator:

	def __init__(self, some_list):
		self.main_list = some_list

	def __iter__(self):
		self.main_list_cursor = 0
		self.nested_list_cursor = -1
		self.full_list = []
		return self

	def __next__(self):
		self.nested_list_cursor += 1

		if len(self.main_list[self.main_list_cursor]) == self.nested_list_cursor:
			self.main_list_cursor += 1
			self.nested_list_cursor = 0

		if self.main_list_cursor == len(self.main_list):
			raise StopIteration

		self.full_list = self.main_list[self.main_list_cursor][self.nested_list_cursor]
		return self.full_list
		
# Задача 2
def gen_list(list_):
	for item_1 in list_:
		for item_2 in item_1:
			yield item_2

if __name__ == '__main__':
	nested_list = [
				['a', 'b', 'c'],
				['d', 'e', 'f', 'h', False],
				[1, 2, None],
			]

	for item in FlatIterator(nested_list):
		print(item)  

	list_ = [item for item in FlatIterator(nested_list)]
	print(list_)

	for elem in gen_list(nested_list):
		print(elem)
