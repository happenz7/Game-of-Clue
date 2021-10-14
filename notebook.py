#Attempted Notebook Class
#def markNotebook(self,Player,cross,check,question):

#Crossing and Marking different players, rooms or weapons
def cross(self,Player):
    return cross

def check(self):
    return check

def question(self):
    return check


#Table represented by Array
rows1 = int(6)
columns1 = int(6)
grid1 = []
i1 = int(0)
for i1 in range(rows1):
    if cross:
        grid1.append("X")
    elif check:
        grid1.append("Y")
    elif question:
        grid1.append("?")
    else:
        grid3.append("_")
for i1 in range(columns1):
    print(grid1)


rows2 = int(6)
columns2 = int(6)
grid2 = []
i2 = int(0)
for i2 in range(rows2):
    if cross:
        grid2.append("X")
    elif check:
        grid2.append("Y")
    elif question:
        grid2.append("?")
    else:
        grid2.append("_")
for i2 in range(columns2):
    print(grid2)


rows3 = int(6)
columns3 = int(9)
grid3 = []
i3 = int(0)
for i3 in range(rows3):
    if cross:
        grid3.append("X")
    elif check:
        grid3.append("Y")
    elif question:
        grid3.append("?")
    else:
        grid3.append("_")
for i3 in range(columns3):
    print(grid3)


#ToString type function to allow certain letters to represent different checking and marking acitivies

# def str(self):
#     field = "_"
#     for i in range(rows):
#         for i in range(columns):
#             if cross:
#                 field = field + "X"
#             elif check:
#                 field = field + "Y"
#             elif question:
#                 field = field + "?"
#             elif ebyPlayer:
#                 field = field + "E"
#
#             print(field)
#


