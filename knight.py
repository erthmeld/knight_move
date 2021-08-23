VOWELS='AEIOUY'

class GeneCrumpler:
    """ My matrix path traversal class
    
    Class object instantiates matrix and provides methods to solve
    path traversal problems. All path traversal problems should reset
    __paths attribute to empty dict on completion to avoid invalid 
    results when multiple path traversals are called on the same object

    Attr:
        __matrix (list[list]): The __matrix of values to be traversed
        __validMoves (list[tuple]): All possible valid moves (default is knight set)
        __paths (dict[str,int]): Store all valids __paths for a given traversal action
    """

    __matrix = [['A','B','C','','E'],\
              ['','G','H','I','J'],\
              ['K','L','M','N','O'],\
              ['P','Q','R','S','T'],\
              ['U','V','','','Y']]
    __validMoves=[(-2,-1),(-2,1),(-1,-2),(-1,2),(1,-2),(1,2),(2,-1),(2,1)]
    __paths = {}

    def __init__(self) -> None:
        pass
        
    def solve__Matrix(self):
        """ Method to solve matrix path traversal problem for all start
        positions itteratively.
        
        Returns:
            int: Total valid __paths found
        """
        
        for r in range(0,5):
            for c in range(0,5):
                self.__findPaths((r,c),0,'',0)
        solutionPaths = len(self.__paths)
        #print(self.__paths)
        self.__paths = {}
        return solutionPaths

    def __findPaths(self,currPos,currMove,currPath,totVowels):
        """ Private method to find all valid unique paths through the 
        object's __matrix attribute using moves defined by the __validMoves 
        attribute from a specified starting point. 

        This method is recursive and for each complete valid traversal adds 
        a dict entry to the objects __paths attribute with the key being the 
        currPath parameter and a value of 1.
        
        Params:
            currPos(tuple(int,int)): Current row, col position on matrix
            currMove(int): Number of moves completed as of function call
            currPath(str): String concatination of all previous position char 
            values in traversal order
            totVowels(int): number of vowels in currPath as of function call
        """
        
        currPath += self.__matrix[currPos[0]][currPos[1]]
        currVal = self.__matrix[currPos[0]][currPos[1]]
        if currVal in VOWELS:
            totVowels += 1
        if currMove >= 7:
            self.__paths[currPath] = 1
            return
        for move in self.__validMoves:
            if 4 >= currPos[0] + move[0] >= 0 and 4 >= currPos[1] + move[1] >= 0:
                nextVal = self.__matrix[currPos[0] + move[0]][currPos[1] + move[1]]
                if nextVal == '':
                    continue
                if nextVal in VOWELS and totVowels == 2:
                    continue
                newPos = (currPos[0] + move[0],currPos[1] + move[1])
                newMove = currMove + 1
                self.__findPaths(newPos, newMove, currPath, totVowels)

def main():
    """ Instantiate class object and call method to solve matrix
    path traversal problem.
    """
    
    me = GeneCrumpler()
    print(me.solve__Matrix())

if __name__ == "__main__":
    # execute only if run as a script
    main()