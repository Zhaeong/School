#Owen Zhang
#Student ID: 998355694
#STA247

#Question 2

SIDP = c(0/9,0/9,0/9,1/9,1/9,2/9,1/9,0/9,1/9,3/9)

#D ~ SIDP

#Calculate E(D)
#Use the formula E(x) = sum of all values of x(x * f(x))
#Where f(x) is the pmf
Ex = 0
for(x in 0:9){
	Ex = Ex + (x * SIDP[x+1])
	}
print(Ex)
#E(D) = 6.444444

#Calculate Var(D)
#Use the formula Var(x) = E(x^2) - (E(x))^2
Ex2 = 0
for(x in 0:9){
	Ex2 = Ex2 + (x^2 * SIDP[x+1])
	}
print(Ex2 - Ex^2)
#Var(D) = 46.4444 - 6.444^2
#Var(D) = 4.91358



