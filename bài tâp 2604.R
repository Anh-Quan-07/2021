setwd('C:\\Users\\DELL\\PythonProject')

#Cau 1
answer <- 0
for (j in 3:5){ answer <- j+answer }
answer

answer1 <- 10
for (j in 3:5){ answer1 <- j+answer1 }
answer1

answer2 <- 10
for (j in 3:5){ answer2 <- j*answer2 }
answer2

#Cau 2
5*prod(3:5)  #nhan 1 dãy so voi khoang cach 1 don vi

#Cau 3
answer3 <- 0
for (j in 1:100){ answer3 <- j+answer3 }
answer3

sum(1:100)

#Cau 4
answer4 <- 1
for (j in 1:50){ answer4 <- j*answer4 }
answer4

prod(1:50)

#Cau 5
radius <- 3:20
volume <- 4*pi*radius^3/3
conversion <- data.frame(Radius=radius, volume=volume)
conversion

#Cau 6
factor_day <- factor(conversion, order = TRUE, levels =c('radius','volume'))
factor_day
sapply(conversion,length)
sapply(conversion,sum)
sapply(conversion,mean)
sapply(conversion,cumsum)