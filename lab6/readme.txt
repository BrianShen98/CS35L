I first met the problem about how to pass multiple local variables to child
threads. And I found that I have 2 option: making those local variables global or
using a struct to store these value. But after choosing to use struct, I found
that it cannot work properly, since every child thread needs a struct to be passed
in and I only created one struct and pass the address of it to all the childthreads. And considering that create struct for every child thread might be too expensive,
I chose to make those variables global instead. And after I implemented this
option, I found that my program still cannot run properly. diff ouputted many
different lines. And I realized that the original code print out the colour of 
each pixel right after it is calculated. With multithreading, I cannot do so since
the order of execution is not sequential. So I used an array to store the colour 
for all the pixels, and print it out after all the child threads finish execution.

And another problem I realized is that I cannot pass the address of a variable
whose value would be updated later in the parent thread, since the value of the
variable passed into the child thread might be altered.

I think my implementation of SRT greatly improve its performance. When the program
is single threaded, it takes 0m44.337s, while using 80 thread the program can
finish executing after 0m2.715.
