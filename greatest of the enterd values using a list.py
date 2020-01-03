from time import*
from classes_OOP import math_ops

def print_list(list):
        print(list)
##def sort_list_low_to_high(list):
##        count=1
##        for elements in list:
##                count_2=count
##                while count_2>0 and list[count_2]<list[count_2-1]:
##                        temp1=list[count_2]
##                        list[count_2]=list[count_2-1]
##                        list[count_2-1]=temp1
##                        count_2=count_2-1
##                count=count+1


def main():
        sammation = math_ops
        print(sammation.sum_2(3,3))
        list_items=[]
        maximum=int(input(" enter the first element"))
        enterd_value=maximum
        minimum=maximum
        list_items.append(maximum)
        while enterd_value!=0:
                enterd_value=int(input("enter the value to append:  "))
                list_items.append(enterd_value)

                if maximum<enterd_value :
                        maximum=enterd_value
                if minimum>enterd_value and enterd_value!=0:
                        minimum=enterd_value
        print("the maximum element is:", maximum)
        print("and the minimum element is :", minimum)
        print()
        print_list(list_items)
##        sort_list_low_to_high(list_items)
##        print()
##        print_list(list_items)
##        sleep(1000)

if __name__ == '__main__':
	main()


