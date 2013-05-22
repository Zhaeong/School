#Question 2

#Part a)
h = function(x)
{return(x^6+x^9+(cos(x))^4)}


x = integrate(h,0,1)

#Part b)
randomvalue = function() #helper function
{return(c(runif(1),runif(1,0,2.2)))}

spattercast = function(n){
total = 0
under = 0
for(x in 1:n){
	randpoint = randomvalue()
	curvey = h(randpoint[1])
	if(randpoint[2]<=curvey){
		total = total + 1
		under = under + 1}
	if(randpoint[2]>curvey){total = total +1}
	}
return((under/total)*2.2)}

accurcast = function(d){
	#returns the amount of point necessary for decimal value d
	points = 10
	while(round(0.8215314,d)!=round(spattercast(points),n)){
	points = points + 100
	print(points)}
	return(points)
}

#one_decimal_accuracy = accurcast(1)
#two_decimal_accuracy = accurcast(2)
#three_decimal_accuracy = accurcast(3)
#four_decimal_accuracy = accurcast(4)
#five_decimal_accuracy = accurcast(5)
#six_decimal_accuracy = accurcast(6)
#These functions would take too long to find value so 
#they are commented out

#Part c)

#The approximate value is show in the table here
#Decimal Accuracy | Amount of points needed
#      1          | 10000
#      2          | 100000
#      3          | 1000000
#      4          | 5000000
#      5          | 10000000
#      6          | 500000000


#round(10000,1) = 0.8
#round(100000,2) = 0.82
#round(1000000,3) = 0.822
#round(5000000,4) = 0.8215
#round(10000000,5) = 0.82153
#round(500000000,6) = 0.821531

#From this relationship we can see that accuracy to more decimal places require
#more points to be plotted in a spattercast method
