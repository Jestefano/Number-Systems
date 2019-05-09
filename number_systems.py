
class fraction():
	num_frac = 0

	def __init__(self,numerator,denominator):
		assert (type(numerator)==int), "Numerator has to be int"
		assert (type(denominator)==int), "Denominator has to be int"
		assert (denominator != 0), "Denominator can't be zero"

		self.numerator = numerator
		self.denominator = denominator
		self.num_frac = fraction.num_frac

		fraction.num_frac += 1

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

	def get_num_frac(self):
		return self.num_frac

if __name__ == "__main__":
	q = fraction(4,2)
	q.invert()
	q.reduce()
	
	print(q)
