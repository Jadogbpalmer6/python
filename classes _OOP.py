import time
class math_ops:
	def __init__(self,var1,var2):
		self.var1=var1
		self.var2=var2

	def sum_2(self):
		return self.var1+self.var2
	def deference_2(self):
		return self.var1-self.var2
	def division(self):
		try:
			m=self.var1/self.var2
			return m
		except Exception as e:
			print('Exception', e, 'occured')
		
def main():
    x=int(input('enter the first number you wish to calculate:'))
    y=int(input('enter the second number you wish to calculate:'))
    jado = math_ops(x,y)
    jadi = math_ops(4,2)
    jado.mathh=jadi
    print('deff', jado.mathh.sum_2())
    summ = jado.sum_2()
    deff = jado.deference_2()
    print('the sum',x,'+',y ,'is', summ, 'and the diference', x,'-',y,' is', deff)
    print(int(jado.division()))
    time.sleep(100)

if __name__ == '__main__':
	main()
