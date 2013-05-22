
SIDP = 998355694

dsidp = function(d)
 {
    probabilities = c(0/9, 0/9, 0/9, 1/9, 1/9, 2/9, 1/9, 0/9, 1/9, 3/9)
    return ( probabilities[d + 1])
  }


psidp = function(d)
  {
    cumulative_prob = 0
    for (i in 0:(d-1)) {
        cumulative_prob = cumulative_prob + dsidp(i)
     }
    return (cumulative_prob)
   }


qsidp = function(d)
  {
    cdf = c()
    for (i in 0:9) {
        cdf = append(cdf, psidp(i))
     }
    if (d == 1 || d > cdf[9] ) {
        return (9) } 
    counter = 1
    while (cdf[counter] < d) {
        counter = counter + 1
     }
    return (counter - 1)
  }


rsidp = function(n)
  {
    unif_random = c(runif(n))
    student_random = c()
    for (item in unif_random) {
       student_random = append(student_random, qsidp(item))
  }
    return (student_random)
 }