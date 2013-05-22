#Question 2 Board 2

die = function()
{#Simulate a dice toss
x = as.integer(runif(1,1,7))
 return(x)}

#Part a)
Board2 = c(1,2,3,3,5,6,9,8,9)

Board2Matrix = matrix(0,9,9)

Board2Matrix[1,2:9] = 1/6
Board2Matrix[1,3] = 2/6
Board2Matrix[1,4] = 0
Board2Matrix[1,7] = 0
Board2Matrix[1,8] = 0

Board2Matrix[2,3:9] = 1/6
Board2Matrix[2,3] = 2/6
Board2Matrix[2,4] = 0
Board2Matrix[2,7] = 0

Board2Matrix[3,3:9] = 1/6
Board2Matrix[3,9] = 2/6
Board2Matrix[3,4] = 0
Board2Matrix[3,7] = 0

Board2Matrix[5,6:9] = 1/6
Board2Matrix[5,7] = 0
Board2Matrix[5,9] = 2/6

Board2Matrix[6,8:9] = 1/6
Board2Matrix[6,9] = 2/6

Board2Matrix[8,9] = 1/6

Board2Matrix[9,9] = 1

#Part b)
move = function(a) #helper function
{
x = die()
a2 = a + x
if(a2 > 9) {return(a)}
if(a2 == 4) {return(3)}
if(a2 == 7) {return(9)}
else{return(a2)}
}

playgame = function()
{
turns = 0
location = 1
while(location !=9){
	location = move(location)
	turns = turns + 1}

return(turns)
}

#Part d)
playgame2player = function()
{
player1 = playgame()
player2 = playgame()
if(player1 < player2){return('Player1 Wins')}
if(player2 < player1){return('Player2 Wins')}
if(player1 == player2){return('Tie Game')}
}

expturns = function(n){
	sim = 0
	for(x in 1:n){sim = sim + playgame()}
	return(sim/n)
	}

#simulated value for 10000 trials
E_sim = expturns(10000)

#Part e)
M = Board2Matrix

E1 = M
E2 = M%*%M
E3 = M%*%M%*%M
E4 = M%*%M%*%M%*%M
E5 = M%*%M%*%M%*%M%*%M
E6 = M%*%M%*%M%*%M%*%M%*%M
E7 = M%*%M%*%M%*%M%*%M%*%M%*%M
E8 = M%*%M%*%M%*%M%*%M%*%M%*%M%*%M
E9 = M%*%M%*%M%*%M%*%M%*%M%*%M%*%M%*%M

E_theory = E1[1,1] + E2[1,2]*2 + E3[1,3]*3 + E4[1,4]*4 + E5[1,5]*5 +
E6[1,6]*6 + E7[1,7]*7 + E8[1,8]*8 + E9[1,9]*9

Z = E1[1,9] + E2[1,9]*2 + E3[1,9]*3 + E4[1,9]*4 + E5[1,9]*5 +
E6[1,9]*6 + E7[1,9]*7 + E8[1,9]*8 + E9[1,9]*9

#The Expected value for the number of turns necessary from theoretical,
#E_theory is 5.284455
#The Expected value for the number of turns necessary from simulation of
#10000 trials, E_sim is 4.4152
#From these two values we can conclude that the theoretical value does
#not correspond with simulated value, however it is closer than
#Board # 1




