import unittest
from HW2_2018217 import minFunc



class testpoint(unittest.TestCase):
	def test_minFunc1(self):
		self.assertTrue(minFunc('4','(0) d()'),'a\'b\'c\'d\'')
	def test_minFunc2(self):
		self.assertTrue(minFunc('4','(0,1) d(2,3)'),'a\'b\'')
	def test_minFunc3(self):
		self.assertTrue(minFunc('4','(0,1,2,3,4,5,6) d(7,8,9,10,11,12,13,14,15)'),'1')
	def test_minFunc4(self):
		self.assertTrue(minFunc('4','(6,7,8,9) d(10,11,12,13,14,15)'),'bc + a' or 'a + bc')
	def test_minFunc5(self):	
		self.assertTrue(minFunc('4','(0,2,5,8,10,15) d()'),'b\'d\' + abcd + a\'bc\'d' or 'abcd + b\'d\' + a\'bc\'d' or 'abcd + a\'bc\'d + b\'d\'' or 'b\'d\' + a\'bc\'d + abcd' or 'a\'bc\'d + b\'d\' + abcd' or 'a\'bc\'d + abcd + b\'d\'')
	def test_minFunc6(self):
		self.assertTrue(minFunc('3','(0,2,4,5,6,7) d()'),'c\' + a' or 'a + c\'')
	def test_minFunc7(self):	
		self.assertTrue(minFunc('3','(4,6) d(0,1,2,3)'),'c\'')
	def test_minFunc8(self):	
		self.assertTrue(minFunc('3','(1,7) d(0,2)'),'a\'b\' + abc' or 'abc + a\'b\'')
	def test_minFunc9(self):	
		self.assertTrue(minFunc('3','(0,4,3,7) d(2,6)'),'b + c\'' or 'c\' + b')
	def test_minFunc10(self):	
		self.assertTrue(minFunc('3','(1,7) d(3,5)'),'c')
	def test_minFunc11(self):	
		self.assertTrue(minFunc('2','(0,1) d(2,3)'),'1')
	def test_minFunc12(self):	
		self.assertTrue(minFunc('2','(0,3) d()'),'ab + a\'b\'' or 'a\'b\' + ab')
	def test_minFunc13(self):	
		self.assertTrue(minFunc('2','(1,3) d()'),'b')
	def test_minFunc14(self):	
		self.assertTrue(minFunc('2','(2) d(0)'),'b\'')
	def test_minFunc15(self):	
		self.assertTrue(minFunc('2','(0) d()'),'a\'b\'')
		
                
if __name__=='__main__':
	unittest.main()
