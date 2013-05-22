#
#  a1.R  -  generate personalized starting numbers for assignment 1
#  2012/09/12
#

#***  Change the seed value to your student number.  ***
set.seed( 987654321 )

a  =  sort( sample(2:16)[1:3] ) / 17.
x  =  round(a[2],3)   #P(A)
y  =  round(a[3],3)   #P(A or B)
z  =  round(a[1]/a[2],3)   #P(B|A)

print( paste( "P(A) = ", x ) )
print( paste( "P(A or B) = ", y ) )
print( paste( "P(B|A) = ", z ) )


