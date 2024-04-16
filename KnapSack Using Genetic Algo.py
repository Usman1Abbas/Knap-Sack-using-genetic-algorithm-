#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[ ]:





# In[28]:


import math
import random

# Global variables
populationSize = 10
weightList = [1, 3, 7, 4, 5, 6]
valueList = [14, 23, 8, 9, 17, 15]
bagSize = 10
k = 2  
m = 0.1  
max_gen = 100
randomList = [random.random() for _ in range(100)]
randCount = 0

# Step 1: Initialization
def initialise():  
    personList = []
    for _ in range(populationSize):
        person = "".join(str(random.randint(0, 1)) for _ in range(len(weightList)))
        personList.append(person)
    return personList

# Step 2: Fitness Function
def evaluate(pList):
    fitnessList = []
    for person in pList:
        sumWeight = sum(int(weightList[i]) * int(person[i]) for i in range(len(person)))
        sumValue = sum(int(valueList[i]) * int(person[i]) for i in range(len(person)))
        if sumWeight <= bagSize:
            fitnessList.append((person, sumValue))
        else:
            fitnessList.append((person, 0))
    return fitnessList

# Step 3: Selection
def parentSelect(fList):
    parentSelectList = []
    for _ in range(populationSize):
        selected = random.choices(fList, k=k)
        parentSelectList.append(min(selected, key=lambda x: x[1]))
    return parentSelectList

# Step 4: Crossover
def recombine(pList):
    childList = []
    for i in range(0, len(pList), 2):
        parent1, parent2 = pList[i][0], pList[i+1][0]
        crossover_point = random.randint(1, len(parent1) - 1)
        child1 = parent1[:crossover_point] + parent2[crossover_point:]
        child2 = parent2[:crossover_point] + parent1[crossover_point:]
        childList.extend([child1, child2])
    return childList

# Step 5: Mutation
def mutation(cList):
    mutationList = []
    for child in cList:
        mutated_child = ''.join('0' if bit == '1' else '1' if bit == '0' and random.random() < m else bit for bit in child)
        mutationList.append(mutated_child)
    return mutationList

# Step 6: Replacement
def survivorSelect(cList, pList):
    combined = cList + pList
    combined.sort(key=lambda x: x[1], reverse=True)
    return combined[:populationSize]

# Step 7: Termination
def knapsackGA():
    # Step 1: Initialization
    population = initialise()

    for _ in range(max_gen):
        # Step 2: Fitness Function
        fitness = evaluate(population)

        # Step 3: Selection
        parents = parentSelect(fitness)

        # Step 4: Crossover
        children = recombine(parents)

        # Step 5: Mutation
        mutated_children = mutation(children)

        # Step 6: Replacement
        population = survivorSelect(mutated_children, population)

    return population

# Run the genetic algorithm
best_solution = knapsackGA()
print("Best solution:", best_solution[0])


# In[ ]:




