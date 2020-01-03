class comp:
        def __init__(self, var1, var2):
                self.var1=var1
                self.var2=var2
                print('in init')
        def config(self):
                print('the config is', self.var1,',',self.var2)
comp1=comp('i2',16)
print('hello')
comp1.config()
comp2=comp('i6', 12)
print()
comp2.config()
