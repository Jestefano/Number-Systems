
class fraction():
	""" 
	This is the implementation of a fraction number
	Note: To work properly we assume that there is no other class
		called fraction neither in the project nor in the modules that
		the user has imported. Otherwise, all the operations will not
		work properly.
	"""
	frac_count = 1

	def __init__(self,numerator,denominator):
		"""In order to initialize we ask for two integer numbers
		The second one should be different from zero """
		assert (type(numerator)==int), "Numerator has to be int"
		assert (type(denominator)==int), "Denominator has to be int"
		assert (denominator != 0), "Denominator can't be zero"

		self.numerator = numerator
		self.denominator = denominator
		self.frac_count = fraction.frac_count

		fraction.frac_count += 1

	def __str__(self):
		"""We print the number as a/b"""
		return (str(self.numerator)+'/'+str(self.denominator))

	def __add__(self,other):
		"""
		Addition:
		We can add with a fraction or an integer
		"""
		if('fraction' in str(type(other))):
			new_numerator = self.numerator*other.denominator + other.numerator*self.denominator
			new_denominator = self.denominator * other.denominator
			new_frac = fraction(new_numerator, new_denominator)
			return new_frac
		elif('integer' in str(type(other))):
			new_numerator = self.numerator + other.value * self.denominator
			new_frac = fraction(new_numerator,self.denominator)
			return new_frac
		else:
			raise Exception("Use an integer or fraction in the operator")

	def __sub__(self,other):
		"""
		We can substract with another fraction or an integer
		"""
		if('fraction' in str(type(other))):
			new_frac = fraction((-1)*other.get_numerator(),other.get_denominator())
			return fraction.__add__(self,new_frac)
		elif('integer' in str(type(other))):
			new_int = integer((-1)*other.get_value())
			return fraction.__add__(self,new_int)
		else:
			raise Exception("Use an integer or fraction in the operator")

	def __mul__(self,other):
		"""
		We can multiply with another fraction or an integer
		"""
		if('fraction' in str(type(other))):
			new_numerator = self.numerator * other.get_numerator()
			new_denominator = self.denominator * other.get_denominator()
			new_frac = fraction(new_numerator,new_denominator)
			return new_frac
		elif('integer' in str(type(other))):
			new_numerator = self.numerator * other.get_value()
			new_frac = fraction(new_numerator, self.denominator)
			return new_frac
		else:
			raise Exception("Use an integer or fraction in the operator")

	def __truediv__(self,other):
		"""
		We can divide with another fraction or an integer as long as they
		are not zero
		"""
		if('fraction' in str(type(other))):
			assert (other.get_numerator()!=0), "Can't divide by zero"
			new_numerator = self.numerator * other.get_denominator()
			new_denominator = self.denominator * other.get_numerator()
			new_frac = fraction(new_numerator,new_denominator)
			return new_frac
		elif('integer' in str(type(other))):
			assert (other.get_value()), "Can't divide by zero"
			new_denominator = self.denominator * other.get_value()
			new_frac = fraction(self.numerator, new_denominator)
			return new_frac
		else:
			raise Exception("Use an integer or fraction in the operator")

	def invert(self):
		"""
		We can invert a non-zero fraction """
		assert (self.numerator!=0), "Numerator can't be zero"

		self.numerator,self.denominator = self.denominator,self.numerator
		return self

	def __gcd(a,b):
		"""
		This is an internal function that we use to reduce 
		the fraction """
		return (b if a%b==0 else fraction.__gcd(b,a%b))

	def reduce(self):
		"""
		This function returns the fraction reduced 
		"""
		gcd_ = fraction.__gcd(self.numerator,self.denominator)
		self.numerator = self.numerator//gcd_
		self.denominator = self.denominator//gcd_
		return self

	def get_numerator(self):
		return self.numerator

	def get_denominator(self):
		return self.denominator

	def get_real_value(self):
		return self.numerator/self.denominator

	def get_frac_count(self):
		return self.frac_count

	def set_numerator(self,new_numerator):
		assert (type(new_numerator)==int), "Numerator has to be int"
		self.numerator = new_numerator

	def set_denominator(self,new_denominator):
		assert (type(new_denominator)==int), "Denominator has to be int"
		assert (new_denominator!=0), "Denominator can't be zero"

		self.denominator = new_denominator



class integer(fraction):
	"""This is my implementation of an integer number
	It is based on the int class from Python, and it supports
	operations with integer and fraction """
	int_count = 1

	def __init__(self,value):
		"""
		In order to initialize this we need an int value"""
		assert (type(value)==int), "Value should be integer"

		fraction.__init__(self,value,1)
		self.value = value
		self.int_count = integer.int_count
		integer.int_count += 1

	def __str__(self):
		""" I print the value itself"""
		return str(self.value)
		

	def __add__(self,other):
		"""We can add an integer with a integer or
		with a fraction """
		if("fraction" in str(type(other))):
			new_frac = fraction.__add__(other,self)
			new_frac.reduce()
			if(new_frac.get_denominator()==1):
				new_int = integer(new_frac.get_numerator())
				return new_int
			else:
				return new_frac
		elif("integer" in str(type(other))):
			new_int = integer(self.value + other.value)
			return new_int 
		else:
			raise Exception("Integer or fraction expected")

	def __sub__(self,other):
		"""We can substract an integer with a integer or
		with a fraction """
		if("fraction" in str(type(other))):
			aux_frac = fraction(-other.get_numerator(),other.get_denominator())
			new_frac = fraction.__add__(aux_frac,self)
			new_frac.reduce()
			if(new_frac.get_denominator()==1):
				new_int = integer(new_frac.get_numerator())
				return new_int
			else:
				return new_frac
		elif("integer" in str(type(other))):
			new_int = integer(self.value - other.value)
			return new_int
		else:
			raise Exception("Integer or fraction expected")

	def __mul__(self,other):
		"""We can multiply an integer with a integer or
		with a fraction """
		if("fraction" in str(type(other))):
			new_frac = fraction.__mul__(other,self)
			return new_frac
		elif("integer" in str(type(other))):
			new_int = integer(self.value*other.value)
			return new_int
		else:
			raise Exception("Operator has to be integer or fraction")

	def __truediv__(self,other):
		"""We can divide an integer with a integer or
		with a fraction as long as it is non-zero"""
		if("integer" in str(type(other))):
			assert (other.get_value()!=0), "Can't divide by zero"
			new_frac = fraction(self.value,other.get_value())
			new_frac.reduce()
			if(new_frac.get_denominator()==1):
				new_int = integer(new_frac.get_numerator())
				return new_int
			else:
				return new_frac
		elif("fraction" in str(type(other))):
			assert (other.get_numerator()!=0), "Can't divide by zero"
			new_frac = integer.__mul__(self,other.invert())
			other.invert()
			return new_frac
		else:
			raise Exception("Operators have to be integer or fraction")

	def __floordiv__(self,other):
		"""This function returns the floor division. It only
		accepts an integer as parameter"""
		assert ("integer" in str(type(other))), "Operand has to be integer"
		assert (other.value!=0), "Can't divide by zero"

		new_int = integer(self.value//other.value)
		return new_int

	def set_value(self,value):
		assert (type(value)==int), "Value should be integer"
		self.value = value

	def get_value(self):
		return self.value

	def get_int_count(self):
		return self.int_count

if __name__ == "__main__":
	int1 = integer(3)
	int2 = fraction(6,3)

	print(int1*int2)
	print(int2*int1)
	print(int1/int2)
	print(int2/int1)
	print(int1*int2)
	print(int2*int1)
	print(int1/int2)
	print(int2/int1)
