#Owen Zhang
#STA247
#Student ID: 998355694
#a2OWENZHANGdemo


source("C:\\Users\\Owen\\Desktop\\university of toronto 2010-2011\\Year 3\\sta247\\a2OWENZHANGfunc.R")

#Question 4
#Part a

print('Try the value 6 in dsidp function')
print(dsidp(6))
#expect value to be 1/9 = 0.1111

print('Try the value 6 in psidp function')
print(psidp(6))
#expect value to be 5/9 = .55555555

print('Try the value of 0.55555555 in qsidp function')
print(qsidp(0.55555555))
#expect value to be 6

#Part b
sample_sizes = c(1:200)
sample_means = c()

for (x in 1:200){
	sample_means = append(sample_means, mean(rsidp(x)))
	}

plot(sample_sizes, sample_means)

#Part c
sample_size = c(1:20)
sample_variances = c()
for (x in 1:20){
	sample_variances = append(sample_variances, var(rsidp(x)))
	}

plot(sample_sizes, sample_variances)

