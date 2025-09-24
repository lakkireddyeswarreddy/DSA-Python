from collections import deque

class MovingAverage:
    
    def __init__(self, size):
        self.size = 0
        self.max_size=size
        self.queue = deque(maxlen=size)
        self.sum=0
        
    def next(self, val:int) -> float:
        if self.size == self.max_size:
            self.sum-=self.queue.popleft()
        else:
            self.size+=1
        self.queue.append(val)
        self.sum+=val
        return self.sum/self.size
    
# obj=MovingAverage(3)
# print(obj.next(1))
# print(obj.next(10))
# print(obj.next(3))
# print(obj.next(5))


class SnakeGame:
    
    def __init__(self, width:int, height:int, food : list[list[int]]):
        self.width = width
        self.height = height
        self.food = deque()
        self.food.extend(food)
        self.score = 0
        self.current_position=[0,0]
        
    def move(self, direction:str) -> int :
        
        match direction:
            case "L":
                if self.current_position[-1]<=0:
                    return -1
                self.current_position[-1]-=1

            case "R":
                if self.current_position[-1]>=self.width:
                    return -1
                self.current_position[-1]+=1

            case "U":
                if self.current_position[0]<=0:
                    return -1
                self.current_position[0]-=1

            case "D":
                if self.current_position[0]>=self.height:
                    return -1
                self.current_position[0]+=1

                
        if self.food and self.current_position == self.food[0]:
            self.score+=1
            self.food.popleft()
            
        return self.score
                
        
obj = SnakeGame(2, 2, [])
print(obj.move("R"))
# print(obj.move("D"))
print(obj.move("R"))
# print(obj.move("U"))
# print(obj.move("L"))
# print(obj.move("U"))





        
    