# Word Search Kata
 
 ## Prerequisites
 
 In order to run the word search, you will need python installed. This can be installed from 
 https://www.python.org/downloads/ linux comes with python installed by default on Ubuntu.
 
 ## Usage
 
 To use the word search, first clone this repository. Open a terminal and, within the terminal, 
 navigate to the root directory for this repository.
 
 #### Running the unit tests
 The unit tests can be run with the command `python3 WordSearchTest.py`
 
 #### Running the word search on custom inputs
 To run on a custom word grid, first ensure the grid is formatted as a csv with the words to 
 find in the first row, like the following example: 

BONES,KHAN,KIRK,SCOTTY,SPOCK,SULU,UHURA  
U,M,K,H,U,L,K,I,N,V,J,O,C,W,E  
L,L,S,H,K,Z,Z,W,Z,C,G,J,U,Y,G  
H,S,U,P,J,P,R,J,D,H,S,B,X,T,G  
B,R,J,S,O,E,Q,E,T,I,K,K,G,L,E  
A,Y,O,A,G,C,I,R,D,Q,H,R,T,C,D  
S,C,O,T,T,Y,K,Z,R,E,P,P,X,P,F  
B,L,Q,S,L,N,E,E,E,V,U,L,F,M,Z  
O,K,R,I,K,A,M,M,R,M,F,B,A,P,P  
N,U,I,I,Y,H,Q,M,E,M,Q,R,Y,F,S  
E,Y,Z,Y,G,K,Q,J,P,C,Q,W,Y,A,K  
S,J,F,Z,M,Q,I,B,D,B,E,M,K,W,D  
T,G,L,B,H,C,B,E,C,H,T,O,Y,I,K  
O,J,Y,E,U,L,N,C,C,L,Y,B,Z,U,H  
W,Z,M,I,S,U,K,U,R,B,I,D,U,X,S  
K,Y,L,B,Q,Q,P,M,D,F,C,K,E,A,B  

The grid can then be read and solved  using `python3 SolveWordSearch.py path/to/grid/file` it 
will output the solution as a list of found words along with the x and y coordinates of each 
letter. For example, the solution to the above grid would be: 
BONES : [(0,6),(0,7),(0,8),(0,9),(0,10)]  
KHAN : [(5,9),(5,8),(5,7),(5,6)]  
KIRK : [(4,7),(3,7),(2,7),(1,7)]  
SCOTTY : [(0,5),(1,5),(2,5),(3,5),(4,5),(5,5)]  
SPOCK : [(2,1),(3,2),(4,3),(5,4),(6,5)]  
SULU : [(3,3),(2,2),(1,1),(0,0)]  
UHURA : [(4,0),(3,1),(2,2),(1,3),(0,4)]