#Parking Lot

lot = matrix('X',4,22)
lot[1,] = ' '
lot[4,] = ' '
lot[,1] = ' '
lot[,22] = ' '


vacant_interval = rexp(1,rate=0.01)

oneor = function(){
	num = round(runif(1),0)
	if(num == 0){return(1)}
	if(num == 1){return(4)}
	}

randvacspot = function(){
#returns the coordinates of a random vacancy
	randrow = as.integer(runif(1,2,3))
	randcol = as.integer(runif(1,2,21))
	coord = c(randrow,randcol)
	return(coord)}
	

randomcar = function(){
#returns the coordinates of a random car
	randcol = as.integer(runif(1,1,22))
	randrow = oneor()
	coord = c(randrow,randcol)
	return(coord)}



takespot = function(row,col,matrix){
	if(row == 1){
		if(matrix[2,matrix] == 'O'){
			lot[2,matrix] = 'C'
			lot[1,matrix] = ' '}}
	if(row == 4){
		if(lot[3,matrix]== 'O'){
		lot[3,matrix] = 'C'
		lot[4,matrix] = ' '}}
}

carmove = function(row,col,matrix){
	row = row
	col = col
	if(row==1 & col!=22){
		matrix[1,col+1] = 'C'
		matrix[1,col]= ' '
		takespot(1,col+1,matrix)
		}
	if(row==4 & col!=1){
		matrix[1,col-1] = 'C'
		matrix[1,col]= ' '
		takespot(1,col-1,matrix)
		}
	if(col==1 & row!=1){
		matrix[row-1,col] = 'C'
		matrix[row,1]= ' '
		}
	if(col==22 & row!=4){
		matrix[row+1,col] = 'C'
		matrix[row,1]= ' '
		}
}

#Simulation
Time = 0
car1 = randomcar()
lot[car1[1],car1[2]] = 'C1'

car2 = randomcar()
if(car2[1] == car1[1] &car2[2] == car1[2]){car2 = randomcar()}
#so that car1 != car2
lot[car2[1],car2[2]] = 'C2'

vacant = randvacspot()
lot[vacant[1],vacant[2]] = 'O'