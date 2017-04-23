import itertools

def imright (h1,h2):
	return h2-h1 == 1
def nextto(h1,h2):
	return abs(h2-h1) == 1

def Zebra_Puzzle():
	hourses = first,_,middle,_,_ = [1,2,3,4,5]    #1
	orderings = list(itertools.permutations(hourses))
	return next((Water,Zebra)

			for Englishman,Spaniard,Ukrainian,Norwegian,Japanese in orderings
			if Norwegian is first	 #10
			for Red,Green,Blue,Yellow,Ivory in orderings
			if Englishman is Red 	#2
			if imright(Ivory,Green) 	#6
			if nextto(Norwegian,Blue)	#15
			for Coffee,Water,Milk,Orange,Tea in orderings
			if Coffee is Green 		#4
			if Ukrainian is Tea 	#5
			if Milk is middle		#9
			for OldGold,Kools,Chester,LuckyStri,Parlia in orderings
			if Kools is Yellow 		#8
			if LuckyStri is Orange 		#13
			if Japanese is Parlia 		#14
			for Dog,Fox,Snail,horse,Zebra in orderings
			if Spaniard is Dog 		#3
			if OldGold is Snail 	#7
			if nextto(Kools,horse) 		#12
			if nextto(Chester,Fox)		#11

		)

print(Zebra_Puzzle())