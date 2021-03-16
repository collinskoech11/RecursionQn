# Question 1 (7 points):
## Purpose: To practice recursion with a wrapper function
## Degree of Difficulty: Easy.
In the lecture slides, you may have attempted an exercise to print out all the characters in a string in reverse
using recursion. For this question, you’ll tackle a similar task: printing out all of the WORDS in a string in
reverse. You can assume that separate words in a string are always separated by at least one space.
Sample Run
Assuming our original sentence was DO I CHOOSE YOU PIKACHU, your function should produce the follow-
ing output 1 :


`PIKACHU YOU CHOOSE I DO`


All of the words should be printed on the same line. It is okay if you end up having a trailing space after
the last word.
Program Design
When you write programs to solve problems using loops, very often the code doesn’t jump right into a
loop first thing. Often, there’s a bit of set-up that happens first. The same can be true of recursion.
To solve this problem, you should write TWO functions. The first function should be called something
like reverse_phrase() and must have a SINGLE parameter: the string that represents the sentence to be
reversed. This function should not itself be recursive. It simply does any necessary set-up before calling
your second (recursive) function, which is where the real work will be done.
Your second function should be called something like reverse_phrase_recursive(). It can have any num-
ber of parameters that you think you need, and those parameters can be of any data type that you think
will be easiest to work with. This function must be recursive and is not allowed to use loops in any way.
To test your program, the "main" part of your program should simply call reverse_phrase() with the string
you want to reverse as an argument.
What to Hand In
• A document called a8q1.py containing your finished program, as described above.
Be sure to include your name, NSID, student number, course number and lecture section and laboratory
section at the top of all files.
## Evaluation
• 1 mark: The wrapper function reverse_phrase() performs some reasonable setup that makes the
recursive function easier to write.
• 1 mark: The base case of the recursive function is correct.
• 1 mark: The recursive function has reasonable parameters for solving the problem.
• 2 marks: The recursive case of the recursive function has the correct behaviour
• 2 marks: The doc-string for BOTH functions is sufficiently descriptive, indicating its purpose and re-
quirements.
1 If
Jedi master Yoda played Pokemon, he would need a tool like your program.
Page 2Department of Computer Science
176 Thorvaldson Building
110 Science Place, Saskatoon, SK, S7N 5C9, Canada
Telephine: (306) 966-4886, Facimile: (306) 966-4884
• -2 marks: Global variables and/or loops are used in the recursive function.
• -1 mark: for missing name, NSID and student number at top of file
Page 3
CMPT 141/113
Winter 2021
Introduction to Computer ScienceCMPT 141/113
Department of Computer Science
176 Thorvaldson Building
110 Science Place, Saskatoon, SK, S7N 5C9, Canada
Telephine: (306) 966-4886, Facimile: (306) 966-4884
Winter 2021
Introduction to Computer Science


# Question 2 (6 points):
## Purpose: To practice recursion with a simple example.
Degree of Difficulty: Easy.
Population growth at a constant annual growth rate of r% is governed by a simple equation:
`P n = P n−1 + r · P n−1`
where P n is the population in the n-th year, and P n−1 is the population in the previous year. Here r is a
number between 0.0 and 1.0 representing a percentage (e.g. 0.3 = 30%). You can see that to get the new
population you simply add r% of the previous population to the previous population to obtain the new
population for the next year.
The above formula assumes that population can grow forever with no restrictions. In reality, population
growth is restricted by available resources such as food or energy.
If the environment can only support a maximum population of K, then the growth rate r in the equation
above has to be further multiplied by (1 − P (n−1) /K). With this added to the model, the population growth
will slow as the population approaches K.
## Write a recursive function that takes four parameters:
• The initial population in year 1.
• The year n for which we want to compute the population.
• The annual growth rate r (a floating point value between 0.0 and 1.0, e.g. 0.2 means 20%).
• The maximum population K that the environment can support.
and returns the population in year n.
To verify that your program works, test your function with r = 0.01 (i.e. 8% growth rate), K=10000, and an
initial population of 900. Using these parameters, compute the population for years 1 through 100. Create
and display a line plot using matplotlib of the population over time.
Finally, use your function to solve the following problem: For initial population of 7 billion, an annual growth
rate of 1.1%, and a maximum population of 10 billion, determine how many years it will take until the pop-
ulation exceeds 9.9 billion. Print your answer to the console.
## What to hand in
• Your code for this question in a file called a8q2.py.
• A file (TXT/PDF/DOC) containing a copy of your program’s console output showing how many years
you determined it would take for the population to exceed 9.9 billion.
## Evaluation
• 1 mark: correct base case of recursive function
• 2 marks: correct recursive case of recursive function
• 1 mark: program displays a line plot
• 2 marks: solution to final problem calculated correctly and copy of console output is provided in a
separate file.
• -2 marks: Global variables and/or loops are used in the recursive function.
• -1 mark: for missing name, NSID and student number at top of file
Page 4CMPT 141/113
Department of Computer Science
176 Thorvaldson Building
110 Science Place, Saskatoon, SK, S7N 5C9, Canada
Telephine: (306) 966-4886, Facimile: (306) 966-4884
Winter 2021
Introduction to Computer Science
Question 3 (12 points):
## Purpose: To practice building a recursive algorithm, to review arrays and list comprehensions, to do some-
thing real
Degree of Difficulty: Tricky. Dr. Stanley style
Representing the complexity of curves in two dimensional space is often done by calculating a fractal di-
mension. For a curve in 2D space, calculating the fractal dimension returns a number between 1 (a line) and
2 (a filled 2D shape). The closer the number is to two, the gnarlier and more complex the curve. This kind
of calculation has direct application in geomatics, image processing, and spatial analytics. Some simple
fractal curves can have their fractal dimension calculated from first principles. Most, however, require an
approximation. One popular approximation is the box counting method. 2
Box counting covers an image with boxes, like tiles, then asks how many boxes contain the curve. The pro-
cess is repeated for ever smaller boxes, until enough points are found to calculate the dimension according
to:
dim box (S) =
log(N  )
log(1/)
(1)
where dim box (S) is the fractal dimension, N  is the number of boxes containing the curve at the scale of ,
and 1/ is the inverse of the scale. In the following exercise, the scaling factor is always 12 so the inverse will
always be 2. A classic example of fractal dimension is determining the complexity of the British coastline,
as shown in Fig 1.
Knowing that we have to make a bunch of boxes and count pixels in them isn’t necessarily recursive. You
could imagine dividing an image up into squares, like tiles, then counting each iteratively from top left to
bottom right, like reading in English. However, this can lead to issues if your increment or origin shifts. A
potentially more principled way of making smaller squares is called a quadtree expansion.
In a quadtree expansion, you take the original image, and divide it into four equal squares. (This often
requires padding the image to be exactly square, but we will ignore this issue and assume we have a
perfectly square image). Each square made from the first square is then further subdivided into four smaller
squares, and so on, until a minimum number of pixels remains in each square. This forms a special kind of
data structure called a tree, where the parent is made of four children, and so on down the line, making
something that looks like a Christmas tree. By ensuring that all smaller squares are exactly contained in
larger squares, issues related to origin and resolution choice can be reduced. An example of a quadtree
geometry and part of the resulting tree are shown in Fig. 2. 3
Program Design
You have been provided with a starter file (a8q3-starter.py) which contains several functions. The first
function open_image uses the PIL library to open an image, convert it to a numpy array, and make it binary
(black and white). The output of this function is a numpy array containing 1 (for not part of a curve) or 0
(for part of a curve). Curves are drawn black on white, simply because they look cooler that way. The
second function calculates whether or not a numpy array contains at least one zero by using the special
numpy function texttttall() which literally checks to see if all elements of the provided array are not zero.
Because we know that the curve is zero, if all() returns False then an image must contain at least some
of the curve. Finally, you have been given a plot and fit function plot_line_fit which take x and y arrays
(in this case the log of the inverse scale and box count) and plots those points and the best fit line through
them. The slope of the line (which is an approximation of the dimension according to the equation above)
is returned. Finally you have also been given the header of the main recursive function you have to write
split_into_four, which takes an image, an integer corresponding to the level (how many splits) and list
2 https://en.wikipedia.org/wiki/Minkowski%E2%80%93Bouligand_dimension
3 https://en.wikipedia.org/wiki/Quadtree#/media/File:Quad_tree_bitmap.svg
Page 5Department of Computer Science
176 Thorvaldson Building
110 Science Place, Saskatoon, SK, S7N 5C9, Canada
Telephine: (306) 966-4886, Facimile: (306) 966-4884
CMPT 141/113
Winter 2021
Introduction to Computer Science
Figure 1: Box counting method enclosing the coast of Britain in ever smaller squares
Figure 2: Example image and quadtree expansion. The squares are labelled clockwise starting at the top
left for every image. White nodes in the tree represent completely white squares, black nodes in the tree
represent completely black squares and grey nodes represent a mixture of black and white squares at that
specific resolution. Note that because we want to compute the fractal dimension our stopping conditions will
be slightly different.
Page 6CMPT 141/113
Department of Computer Science
176 Thorvaldson Building
110 Science Place, Saskatoon, SK, S7N 5C9, Canada
Telephine: (306) 966-4886, Facimile: (306) 966-4884
Winter 2021
Introduction to Computer Science
containing the counts for each level. In the main function area, you have been given the number of levels,
which is based on a formula related to the size of the tree that is being built.
You are required to write two pieces of code, one to complete the function split_into_four, and one to
complete the main calls to perform the following:
1. prompt the user for the name of the file on the command line.
2. open an image using open_image. Several images of fractals have been supplied with the assignment.
3. use a list comprehension to create a list of num_levels length full of zeros to contain the count at each
level and print the results.
4. use a list comprehension to initialize the scale variable. It should be the inverse of the length of one
side. If the base case is 1, then the next scale would be 1/2, then 1/4, then 1/8 and so on, meaning
your list should contain 2, 4, 8 and so on.
5. create a quadtree decomposition of the image and count the number of blocks at each level con-
taining the curve by completing split_into_four, and print the returned results. Use a recursive
implementation. The image should not be split if has no curve or if it is 4 pixels by 4 pixels or smaller.
6. plot log(scale) vs log(count) as in equation 1 using plot_line_fit and print the returned value.
Items 1, 2, 3, and 5 are review in using functions, arrays and lists. Item 5 is the recursive portion of this
assignment. Item 5 is both easy, and fiendishly difficult. If you try to hack your way through designing the
recursion, you are likely to tie yourself in knots. This part of the question needs to be done on paper first,
working carefully through the logic. Read the above closely, because it essentially tells you what to do.
One of the elegant properties of recursion is how it can take difficult problems, and express the solution
in a relatively small number of lines of code. My solution added 17 lines to the split_into_four function.
Fewer lines are possible, but I went with a more readable version for the solution. If you have added more
than 25 lines of code to split_into_four, you are probably headed in the wrong direction.
HINT: numpy arrays have a property called shape, which returns a numpy array containing the number of
elements in the array. For example if I had a two dimensional array with three rows and four columns then
print(my_array.shape) would output [3,4]. This will come in handy when writing split_into_four.
NOTE: The text before Program Design is meant to provide context. Everything you need to complete the
assignment is in the Program Design section and the starter file. Don’t get hung up on fractal dimension
and quadtrees if they are just confusing you.
What to Hand In
• A document called a8q3.py containing your finished program, as described above.
• A pdf containing sample output for one of the included fractal images including the figure generated
by plot_line_fits.
Be sure to include your name, NSID, student number, course number and lecture section and laboratory
section at the top of all files.
Evaluation
• 1 mark: File name read from the console.
• 1 mark: Image file read
• 1 mark: num_levels is a list initialized to zero using a list comprehension
• 1 mark: scale is a list initialized correctly using a list comprehension
Page 7Department of Computer Science
176 Thorvaldson Building
110 Science Place, Saskatoon, SK, S7N 5C9, Canada
Telephine: (306) 966-4886, Facimile: (306) 966-4884
CMPT 141/113
Winter 2021
Introduction to Computer Science
• 1 mark: The base case of the recursive function is correct.
• 2 marks: The recursive case of the recursive function has the correct behaviour
• 2 marks: The doc-string is sufficiently descriptive, indicating its purpose and requirements.
• 2 marks: The console output is correct
• 1 mark: The matplotlib graph output is correct
• -2 marks: Global variables and/or loops are used in the recursive function.
• -1 mark: for missing name, NSID and student number at top of file
Sample Run


Please enter the filename : frac1 . png
`[4 , 16 , 55 , 191 , 642 , 1981]`
`[2 , 4 , 8 , 16 , 32 , 64]`
`1. 78 67 263 828664404`


Page