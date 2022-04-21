import random

P = 1
E = 1
Y = 0
Sida = 0.2
Alpha = 0.1
IsConvergnece = 0
Weight01 = 0.3  #random.random() - 0.5
Weight02 = -0.1 #random.random() - 0.5
And_TruthTable = [[0, 0, 0], [0, 1, 0], [1, 0, 0], [1, 1, 1]] #[x1, x2, x1 AND x2]
Or_TruthTable  = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 1]] #[x1, x2, x1 OR x2]
Xor_TruthTable = [[0, 0, 0], [0, 1, 1], [1, 0, 1], [1, 1, 0]] #[x1, x2, x1 XOR x2]


while (not IsConvergnece):
    IsConvergnece = 1
    print()
    print("Epoch " + str(P) + "  ---------------------\n")
    print("x1\tx2\tYd\tw1\tw2\tY\te")
    for testData in And_TruthTable:
        Y = testData[0] * Weight01 + testData[1] * Weight02 - Sida

        #Step Function
        if (Y > 0): Y = 1
        else: Y = 0

        #CorrectWeight
        if (Y != testData[2]):
            IsConvergnece = 0
            E = testData[2] - Y
            Weight01 = Weight01 + Alpha * testData[0] * E
            Weight02 = Weight02 + Alpha * testData[1] * E
        else: E = 0
        
        print(str(testData[0]) +"\t"+ str(testData[1]) +"\t"+ str(testData[2]) +"\t"+ \
            str(round(Weight01, 2)) +"\t"+ str(round(Weight02, 2)) +"\t"+ str(Y) +"\t"+ str(E))
    
    P += 1

print("\n\nConvergence!")
