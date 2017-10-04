As I stated before, the defect in the specifications was that the customer
did not mean to say to swap adjacent items, but instead swap any two items.
The implementation for this specification was completely missing to in the
supplied python code. There was just the function name and an empty
implementation. Also, the display method for the output was also completely
empty in its implementation. In order to implement a correct
implementation, I had to use a double for loop. The outer loop iterated
over every item in the input list except the last index. The inner loop
iterated over the entire input list, but started at the next index after
the current index of the inner loop. So, on every iteration of that inner
loop, there will be one current index from the outer loop and one current
index from the inner loop. So then, the code inside the inner loop will
create a new list that is the same as the input list, but has the two
selected items swapped. This new list is then added to the output. Because
of the way the loop iterations were set up, there are no duplicate lists or
faulty lists created.  It is important that this lab is validated and
verified. The requirements for this lab are supplied by a customer, so in
order to perform validation I had to look over the requirements in the lab
assignment, figure out what exactly the desired output is, and then discuss
these requirements with the customer to try to understand exactly what
their wants are. Also, after I finished an implementation of the system, I
demonstrated the program to the customer to verify that it is what they
desire, as well as if they have anything they want changed. After I have
figured out all the requirements for the program and started to implement
the system, it is important that I verify that the system works. That is
make sure the program meets the customers needs on a technical level
outside of demonstration. In order to perform verification, I had to test
the program. So, other than the two supplied test cases, I add a good
amount of extra test cases in order to ensure that everything is working as
intended based on the requirements.
