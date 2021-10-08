# add "muhammed" to variable "name"
#name = "muhammed"
#print (name)

# ========================

# Assign same value to multiple varibles 
a = b = c = "cat"
#print (a)
#print (b)
#print (c)

# ================================

# reuse variable name the last assigment is printed 
colour = "red"
colour = "blue"
#print (colour)

#===============================

#use the below on shell to find out banned keywords 
#help("keywords")

#=================================

#use the below to find out the type of variable 
var = 23 
#print(type(var))

var = "hello_world"
#print(type(var))

#=====================================

#find out the identity of a varible = score variable is saved in pb refrence 
score = 400 
pb = score
identity = id(pb)
##print(identity)
#print (id(pb))

#===================================

#Both score and pb point to same objecr 
score = 100 
pb = score 

#print(type(score))
#print(type(pb))
##print(score)
print(pb)

#====================================

#score and pb point to different objects 
score = 20 
pb = 100 

print (type(score))
print(type(pb))
print(score)
print(pb)

#=====================

#garbage collection
score = 20 
pb = 100
score = 'completed'

print (type(score))
print(type(pb))
print(score)
print(pb)



