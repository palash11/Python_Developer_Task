#Python_Developer_Task

Task 1 ->
I was not able to write a recursive function.
the process described below will have a high time complexity and I was not able to optimize the solution
First loop will iterate through the values inside key 100gm and then another loop will iterate to all the keys inside the key "100gm" and after that when the key "sub_cat is reached" the values of quntity can be changed
This one more loop is only subjective to the key "sub_cat" that is why I have entered an else condition that will take the values of key "quantity" and change it directly.

Task 3 ->
Here the main logic behind the code is that we will have a high, low and mid value.
high and low is the range in which random numbers are generated
So to generate random number which biased to higher number the range would be [mid, high]
So if the range is [1,10] and numbers greater than 5 will be generated 73 times.
To generate random number which is lower the range would be [low, mid-1] and so numbers less than 5 will be generated 23 times when the function is run 100 times.

The function works as follows:-
To generate a random number a number is passed within the range to the function _randbelow(n).
This function checks whether the number is valid or not and then converts into binary and passes it to getranbits(k) which takes that number and 
1. firstly rounds of the number if any float value is generated 
2. and then using the os module's urandom function it converts into a key which is similar to one created when we create a django project.
3. That key is encoded into hexadecimal and sice it return an string it is converted to int. 
4. Finally a bitwise right shift is done to trim excess values 
5. This final value is return to _randbelow() which in turn return this value to the the randint(low,high) which return the random number to the main function.

