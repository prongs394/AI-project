import cv2
import random

img = cv2.imread('Im001_1.tif', 1)


cv2.imshow('image', img)

cv2.waitKey(00)


cv2.imwrite('copy.tif', img)

# making an initial generation with 100 chromosomes  each chromosome has 3 genes
generation = []
for x in range(0, 100):
    chromosome = []
    for y in range(0, 3):
        gene = []
        for z in range(0, 3):
            n = random.randint(0, 255)
            gene.append(n)
        chromosome.append(gene)
    generation.append(chromosome)

# now we will color the picture with these 100 chromosomes and rate each chromosome.


rate = []   #in rate we will have rating of 100 chromosomes
for i in range(0 , 100):
    rate.append(394)
for c in range(0,100) : #we will color img with chromosome c and rate it
    rateforc = 0
    for x in range(0 , 257):
        for y in range(0 , 257):
            c0 = ((img[x][y][0]-generation[c][0][0])**2 + (img[x][y][1]-generation[c][0][1])**2 + (img[x][y][2]-generation[c][0][2])**2)**(0.5)
            c1 = ((img[x][y][0]-generation[c][1][0])**2 + (img[x][y][1]-generation[c][1][1])**2 + (img[x][y][2]-generation[c][1][2])**2)**(0.5)
            c2 = ((img[x][y][0]-generation[c][2][0])**2 + (img[x][y][1]-generation[c][2][1])**2 + (img[x][y][2]-generation[c][2][2])**2)**(0.5)
            if(c0 == min(c0,c1,c2)):
                rateforc = rateforc + c0
            elif(c1 == min(c0,c1,c2)):
                rateforc = rateforc + c1
            elif(c2 == min(c0,c1,c2)):
                rateforc = rateforc + c2
    rate[c] = rateforc/(257*257)

# now we will sort the chromosomes with their ratings. 0 is worst 99 is best (0 has highest distance and 99 has lowest)
for i in range(0, 99):
    for j in range(i, 100):
        if (rate[i] < rate[j]):
            temp = rate[j]
            rate[j] = rate[i]
            rate[i] = temp
            temp2 = generation[j]
            generation[j] = generation[i]
            generation[i] = temp2
print("rate initial:" , rate)
#print(generation)

#best chromosome so far is 99th we will save it:
bestchromosome = generation[99]
bestrate = rate[99]
copy = img
print("initial has chromosome:",bestchromosome, "and rate:",bestrate)

colorsused=[0,0,0]
for x in range(0, 257):
    for y in range(0, 257):
        c0 = ((img[x][y][0] - bestchromosome[0][0]) ** 2 + (img[x][y][1] - bestchromosome[0][1]) ** 2 + (
                img[x][y][2] - bestchromosome[0][2]) ** 2) ** (0.5)
        c1 = ((img[x][y][0] - bestchromosome[1][0]) ** 2 + (img[x][y][1] - bestchromosome[1][1]) ** 2 + (
                img[x][y][2] - bestchromosome[1][2]) ** 2) ** (0.5)
        c2 = ((img[x][y][0] - bestchromosome[2][0]) ** 2 + (img[x][y][1] - bestchromosome[2][1]) ** 2 + (
                img[x][y][2] - bestchromosome[2][2]) ** 2) ** (0.5)
        if (c0 == min(c0, c1, c2)):
            colorsused[0]=colorsused[0]+1
            copy[x][y][0] = bestchromosome[0][0]
            copy[x][y][1] = bestchromosome[0][1]
            copy[x][y][2] = bestchromosome[0][2]

        elif (c1 == min(c0, c1, c2)):
            colorsused[1]=colorsused[1]+1
            copy[x][y][0] = bestchromosome[1][0]
            copy[x][y][1] = bestchromosome[1][1]
            copy[x][y][2] = bestchromosome[1][2]
        elif (c2 == min(c0, c1, c2)):
            colorsused[2]=colorsused[2]+1
            copy[x][y][0] = bestchromosome[2][0]
            copy[x][y][1] = bestchromosome[2][1]
            copy[x][y][2] = bestchromosome[2][2]

print("colors used:" , colorsused)
cv2.imshow('befor 15 loop', copy)
cv2.waitKey(00)


# now we will make 50 children
children = []
for i in range(0 , 50):
    n = random.randint(0, 99)
    m = random.randint(0, 99)
    gene0=[(generation[n][0][0]+generation[m][0][0])/2 , (generation[n][0][1]+generation[m][0][1])/2 , (generation[n][0][2]+generation[m][0][2])/2]
    gene1=[(generation[n][1][0]+generation[m][1][0])/2 , (generation[n][1][1]+generation[m][1][1])/2 , (generation[n][1][2]+generation[m][1][2])/2]
    gene2=[(generation[n][2][0]+generation[m][2][0])/2 , (generation[n][2][1]+generation[m][2][1])/2 , (generation[n][2][2]+generation[m][2][2])/2]
    # we have to do mutation on genes
    chance = random.randint(0, 9)
    if(chance == 0):
        gene0[0] = gene0[0]**(0.5)
        gene0[1] = gene0[1]**(0.5)
        gene0[2] = gene0[2]**(0.5)
        gene1[0] = gene1[0] ** (0.5)
        gene1[1] = gene1[1] ** (0.5)
        gene1[2] = gene1[2] ** (0.5)
        gene2[0] = gene2[0]**(0.5)
        gene2[1] = gene2[1]**(0.5)
        gene2[2] = gene2[2]**(0.5)
    child = []
    child.append(gene0)
    child.append(gene1)
    child.append(gene2)
    children.append(child)


#we will replace chidlren with 0 to 49 th chromosomes in the last generation:
for i in range(0 , 50):
    generation[i] = children[i]

print("finished initial")
#now we will have to do this 20 more times to make 20 generations
for numofgenerations in range (0,20):
    print("doing generation:",numofgenerations)

    for c in range(0, 99):  # we will color img with chromosome c and rate it
        rateforc = -1
        for x in range(0, 257):
            for y in range(0, 257):
                c0 = ((img[x][y][0] - generation[c][0][0]) ** 2 + (img[x][y][1] - generation[c][0][1]) ** 2 + (img[x][y][2] - generation[c][0][2]) ** 2) ** (0.5)
                c1 = ((img[x][y][0] - generation[c][1][0]) ** 2 + (img[x][y][1] - generation[c][1][1]) ** 2 + (img[x][y][2] - generation[c][1][2]) ** 2) ** (0.5)
                c2 = ((img[x][y][0] - generation[c][2][0]) ** 2 + (img[x][y][1] - generation[c][2][1]) ** 2 + (img[x][y][2] - generation[c][2][2]) ** 2) ** (0.5)
                if (c0 == min(c0, c1, c2)):
                    rateforc = rateforc + c0
                elif (c1 == min(c0, c1, c2)):
                    rateforc = rateforc + c1
                elif (c2 == min(c0, c1, c2)):
                    rateforc = rateforc + c2
        rate[c] = rateforc/(257*257)

    # now we will sort the chromosomes with their ratings. 0 = is worst 99 is best (0 has highest distance and 99 has lowest)
    for i in range(0, 99):
        for j in range(i, 100):
            if (rate[i] < rate[j]):
                temp = rate[j]
                rate[j] = rate[i]
                rate[i] = temp
                temp2 = generation[j]
                generation[j] = generation[i]
                generation[i] = temp2

    # best chromosome so far is 99th we will save it:
    if (bestrate > rate[99]):
        print("previous best:",bestchromosome," new best:",generation[99], "previous rate:",bestrate,"new rate:",rate[99])
        bestchromosome = generation[99]
        bestrate = rate[99]

    # now we will make 50 children
    children = []
    for i in range(0, 50):
        n = random.randint(0, 99)
        m = random.randint(0, 99)
        gene0=[(generation[n][0][0]+generation[m][0][0])/2 , (generation[n][0][1]+generation[m][0][1])/2 , (generation[n][0][2]+generation[m][0][2])/2]
        gene1=[(generation[n][1][0]+generation[m][1][0])/2 , (generation[n][1][1]+generation[m][1][1])/2 , (generation[n][1][2]+generation[m][1][2])/2]
        gene2=[(generation[n][2][0]+generation[m][2][0])/2 , (generation[n][2][1]+generation[m][2][1])/2 , (generation[n][2][2]+generation[m][2][2])/2]
        # now we have to do mutation on genes
        chance = random.randint(0, 9)
        if (chance == 0):
            gene0[0] = gene0[0] ** (0.5)
            gene0[1] = gene0[1] ** (0.5)
            gene0[2] = gene0[2] ** (0.5)

            gene1[0] = gene1[0] ** (0.5)
            gene1[1] = gene1[1] ** (0.5)
            gene1[2] = gene1[2] ** (0.5)

            gene2[0] = gene2[0] ** (0.5)
            gene2[1] = gene2[1] ** (0.5)
            gene2[2] = gene2[2] ** (0.5)


        child = []
        child.append(gene0)
        child.append(gene1)
        child.append(gene2)
        children.append(child)
    # we will replace chidlren with 0 to 49 th chromosomes in the last generation:
    for i in range(0, 50):
        generation[i] = children[i]
    copy = img
    for x in range(0, 257):
        for y in range(0, 257):
            c0 = ((img[x][y][0] - bestchromosome[0][0]) ** 2 + (img[x][y][1] - bestchromosome[0][1]) ** 2 + (
                    img[x][y][2] - bestchromosome[0][2]) ** 2) ** (0.5)
            c1 = ((img[x][y][0] - bestchromosome[1][0]) ** 2 + (img[x][y][1] - bestchromosome[1][1]) ** 2 + (
                    img[x][y][2] - bestchromosome[1][2]) ** 2) ** (0.5)
            c2 = ((img[x][y][0] - bestchromosome[2][0]) ** 2 + (img[x][y][1] - bestchromosome[2][1]) ** 2 + (
                    img[x][y][2] - bestchromosome[2][2]) ** 2) ** (0.5)
            if (c0 == min(c0, c1, c2)):
                copy[x][y][0] = bestchromosome[0][0]
                copy[x][y][1] = bestchromosome[0][1]
                copy[x][y][2] = bestchromosome[0][2]

            elif (c1 == min(c0, c1, c2)):
                copy[x][y][0] = bestchromosome[1][0]
                copy[x][y][1] = bestchromosome[1][1]
                copy[x][y][2] = bestchromosome[1][2]
            elif (c2 == min(c0, c1, c2)):
                copy[x][y][0] = bestchromosome[2][0]
                copy[x][y][1] = bestchromosome[2][1]
                copy[x][y][2] = bestchromosome[2][2]
    print("chromosome used to color:",bestchromosome)
    print("and here rate is:",rate,"and bestrate is:",bestrate)

    cv2.imshow('copynow', copy)
    cv2.waitKey(00)


copy = img
for x in range(0, 257):
    for y in range(0, 257):
        c0 = ((img[x][y][0] - bestchromosome[0][0]) ** 2 + (img[x][y][1] - bestchromosome[0][1]) ** 2 + (
                    img[x][y][2] - bestchromosome[0][2]) ** 2) ** (0.5)
        c1 = ((img[x][y][0] - bestchromosome[1][0]) ** 2 + (img[x][y][1] - bestchromosome[1][1]) ** 2 + (
                    img[x][y][2] - bestchromosome[1][2]) ** 2) ** (0.5)
        c2 = ((img[x][y][0] - bestchromosome[2][0]) ** 2 + (img[x][y][1] - bestchromosome[2][1]) ** 2 + (
                    img[x][y][2] - bestchromosome[2][2]) ** 2) ** (0.5)
        if (c0 == min(c0, c1, c2)):
            copy[x][y][0] = bestchromosome[0][0]
            copy[x][y][1] = bestchromosome[0][1]
            copy[x][y][2] = bestchromosome[0][2]

        elif (c1 == min(c0, c1, c2)):
            copy[x][y][0] = bestchromosome[1][0]
            copy[x][y][1] = bestchromosome[1][1]
            copy[x][y][2] = bestchromosome[1][2]
        elif (c2 == min(c0, c1, c2)):
            copy[x][y][0] = bestchromosome[2][0]
            copy[x][y][1] = bestchromosome[2][1]
            copy[x][y][2] = bestchromosome[2][2]


#print("best chromosome:",generation[c])
#print(copy)
cv2.imshow('copy', copy)
cv2.waitKey(00)
