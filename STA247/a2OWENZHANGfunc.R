#Owen Zhang
#Student ID = 998355694
#STA247
#a2OWENZHANGfunc

SIDP = c(9,9,8,3,5,5,6,9,4)

frq = function(n)
{	
#This function returns the the number of times the number n occurs in SIDP
#This makes the rest of the function usable with any student number

	number = 0
	for (x in 1:9)
		{if(n == SIDP[x]) 
			{number = number + 1}
		}
	return(number)
}

dsidp = function(d)
{ 
	dist = c(frq(0),frq(1),frq(2),frq(3),frq(4),frq(5),frq(6),frq(7),frq(8),frq(9))
 
	probability = dist/9
	return(probability[d+1])
}

psidp = function(d)
{
	acprob = 0
	for (x in 1:d)
		{acprob = acprob + dsidp(x)}
	return(acprob)
}

qsidp = function(p)
{
	val = 0
	for(x in 0:9){
		val = val + dsidp(x)
		if(val >= p) 
			{return(x)}
		}
}

rsidp = function(n)
{
	ranunif = runif(n)
	ransid = c()
	for(x in ranunif){
		ransid = append(ransid, qsidp(x))
		}
	return(ransid)
}