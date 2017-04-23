import itertools
#color pets smoke national drink
import time
def imright(h1,h2):
	if  h2-h1 == 1:
		return True
def nextto(h1,h2):
	if abs(h2-h1) == 1:
		return True
def Zebra_Puzzle():
	hourses = first,_,middle,_,_ = [1,2,3,4,5]    #1
	orderings = list(itertools.permutations(hourses))
	for Englishman,Spaniard,Ukrainian,Norwegian,Japanese in orderings:
		if Norwegian is first:    #10
			for Red,Green,Blue,Yellow,Ivory in orderings:
				if Englishman is Red and imright(Ivory,Green) and nextto(Norwegian,Blue):    #2 #6 #15
					for Coffee,Water,Milk,Orange,Tea in orderings:
						if Coffee is Green and Ukrainian is Tea and Milk is middle:    #4 #5 #9
							for OldGold,Kools,Chester,LuckyStri,Parlia in orderings:
								if Kools is Yellow and LuckyStri is Orange and Japanese is Parlia : #8 #13 #14
									for Dog,Fox,Snail,horse,Zebra in orderings:
										if Spaniard is Dog and OldGold is Snail and nextto(Kools,horse) and nextto(Chester,Fox):   #3 #7 #12  #11 #12
											return Water,Zebra

def Time_call(fun,*args):
	time1 = time.clock()
	print(fun(*args))
	time2 = time.clock()
	return time2-time1

print(Time_call(Zebra_Puzzle))