class Division:
    def __init__(self, number1: int, number2: int, maxtasks: int=32):
        self.number1 = number1
        self.number2 = number2
        self.maxtasks = maxtasks
        
    def calcClose(self, num1: int, num2: int) -> int:
        return num1 - num1 % num2

    def numberToList(self, number: int) -> list:
        return [int(x) for x in str(number)]
    
    def printCalculation(self) -> None:
        number1_list = self.numberToList(self.number1)

        eq_str = str(self.number1) + " : " + str(self.number2) + " = " + str(self.number1 / self.number2)
        print(eq_str)

        tasks = 1
        self.number1 = number1_list[tasks-1]
        rest = self.number1 % self.number2
        while((rest != 0 or tasks < len(number1_list)) and tasks <= self.maxtasks): # Max maxtasks calculation (Period/Irrational)
            close = self.calcClose(self.number1, self.number2)
            print(" " * (tasks - 2) + str(close), "\n" + " " * (tasks - 2) + "---")
            
            if(tasks < len(number1_list)): self.number1 = (self.number1 - close) * 10 + number1_list[tasks]
            else: self.number1 = (self.number1 - close) * 10
            
            print(" " * (tasks - 1) + str(self.number1))
            tasks += 1
            rest = self.number1 % self.number2
            
        if(tasks != self.maxtasks + 1): print(" " * (tasks - 2) + str(self.number1), "\n" + " " * (tasks - 2) + "--", "\n" + " " * (tasks - 1) + "0")
        else: print("The task could not be fully calculated. [Tasks: " + str(self.maxtasks) + "]")
        
    def calculate(self) -> float:
        return self.number1 / self.number2

# Examples        
# Division(10, 7).printCalculation()
Division(349, 8).printCalculation()