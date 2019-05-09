
class fraction():
	frac_count = 1

	def __init__(self,numerator,denominator):
		assert (type(numerator)==int), "Numerator has to be int"
		assert (type(denominator)==int), "Denominator has to be int"
		assert (denominator != 0), "Denominator can't be zero"

		self.numerator = numerator
		self.denominator = denominator
		self.frac_count = fraction.frac_count

		fraction.frac_count += 1

	def __str__(self):
		return (str(self.numerator)+'/'+str(self.denominator))

	def invert(self):
		assert (self.numerator!=0), "Numerator can't be zero"

		self.numerator,self.denominator = self.denominator,self.numerator

	def __gcd(a,b):
		return (b if a%b==0 else fraction.__gcd(b,a%b))

	def reduce(self):
		gcd_ = fraction.__gcd(self.numerator,self.denominator)
		self.numerator = self.numerator//gcd_
		self.denominator = self.denominator//gcd_

	def get_numerator(self):
		return self.numerator

	def get_denominator(self):
		return self.denominator

	def get_real_value(self):
		return self.numerator/self.denominator

	def set_numerator(self,new_numerator):
		assert (type(new_numerator)==int), "Numerator has to be int"
		self.numerator = new_numerator

	def set_denominator(self,new_denominator):
		assert (type(new_denominator)==int), "Denominator has to be int"
		assert (new_denominator!=0), "Denominator can't be zero"

		self.denominator = new_denominator

	def get_frac_count(self):
		return self.frac_count


class integer(fraction):
	int_count = 1

	def __init__(self,value):
		assert (type(value)==int), "Value should be integer"

		fraction.__init__(self,value,1)
		self.value = value
		self.int_count = integer.int_count
		integer.int_count += 1

	def __str__(self):
		return str(self.value)

	def __add__(self,other):
		new_int = integer(self.value + other.value)
		return new_int 

	def __sub__(self,other):
		new_int = integer(self.value - other.value)
		return new_int

	def __mul__(self,other):
		new_int = integer(self.value*other.value)
		return new_int

	def __truediv__(self,other):
		assert (other.value!=0), "Can't divide by zero"

		new_frac = fraction(self.value,other.value)
		new_frac.reduce()
		if(new_frac.get_denominator()==1):
			new_int = integer(new_frac.get_numerator())
			return new_int
		else:
			return new_frac

	def set_value(self,value):
		assert (type(value)==int), "Value should be integer"

		self.value = value

	def get_value(self):
		return self.value

	def get_int_count(self):
		return self.int_count

if __name__ == "__main__":
	q = fraction(4,2)
	q.invert()
	q.reduce()
	
	print(q)

	p = integer(4)
	w = integer(2)
	z = (p/w)
	print((z))
