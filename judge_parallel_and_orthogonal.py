INPUT_DATA = [[3],
            [0, 0, 3, 0, 0, 2, 3, 3],
            [0, 0, 3, 0, 1, 1, 1, 4],
            [0, 0, 3, 0, 1, 1, 2, 2]]

VECTORS_NUMBER = 4

class Segment():
    

class Vector():
    x , y = 0, 0
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, vector):
        return self.__class__(self.x + vector.x, self.y + vector.y)

    def __sub__(self, vector):
        return self.__class__(self.x - vector.x, self.y - vector.y)

    def __mul__(self, vector):
        return self.__class__(self.x * vector.x, self.y * vector.y)

    def __truediv__(self, vector):
        return self.__class__(self.x / vector.x, self.y / vector.y)

def main():
    q = INPUT_DATA[0]
    for query_index in range(1, q + 1):
        #for vector_num in range(VECTORS_NUMBER):
        vec_p0 = Vector(INPUT_DATA[query_index, 0], INPUT_DATA[query_index, 1])
        vec_p1 = Vector(INPUT_DATA[query_index, 2], INPUT_DATA[query_index, 3])
        vec_p2 = Vector(INPUT_DATA[query_index, 4], INPUT_DATA[query_index, 5])
        vec_p3 = Vector(INPUT_DATA[query_index, 6], INPUT_DATA[query_index, 7])
        judge_parallel_and_orthogonal(vec_p0=vec_p0, vec_p1=vec_p1, vec_p2=vec_p2, vec_p3=vec_p3)

def judge_parallel_and_orthogonal(vec_p0, vec_p1, vec_p2, vec_p3):

def 

if __name__ == "__main__":
    main()