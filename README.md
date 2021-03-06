Algorithms Final Project 
Group: Meaghan Grogan, John Merrigan, Jacqueline Pace, Marion Conklin, and Jack Bomba



For this project we are going to tackle the above problem which uses a directed graph for speech recognition. Part a) of the question asks us to come up with an algorithm that returns a sequence of sounds which is represented by a path within the graph to see if that particular sound or sequence exists. The graph would be a directed, weighted graph, with the edges being the probability of the sounds following their predecessors. This could also be executed using a probability matrix. The probability matrix would be # of sounds X # of sounds, and any entries in the probability matrix would be the probability of the sound following another sound. The second paragraph of part a) provides additional information regarding the probabilities of selecting each edge as part of a path. This information will help us to determine the big O of our proposed solution and its time complexity. Our proposed solution will require an implementation of a search algorithm. This past week we learned about and implemented BFS and DFS, and given that the sequence is a finite number of length k, a variation of the BFS algorithm (rather than the DFS algorithm, which would take longer and check more paths than necessary) would be an optimal approach to this problem. Our solution would start at the vertex V0 and search every possible path until the particular sequence s is found. We will figure out the specific inner-workings of this particular algorithm as we proceed with our project. Part b) of the question asks us to return the most probable path, which again will require us to use the probability information provided in part a). 

Since there are five of us in this group, we want to make sure that each of us are doing a sufficient amount of work that is both challenging and enriching. We have created a shared GitHub repository to which each of us can submit code snippets without crashing the overall program if there is an error. Our plan right now is to each compose a proposed solution to part a), meet on a few occasions to discuss our solutions and ultimately craft one final solution for which we will then solve the big O and run time as requested in part a) and part b). We plan to meet before each of the checkpoints to discuss and report our progress, challenges, and findings.

For Checkpoint 2: 

How many lines of code written

Analysis of complexity for all important parts of the code

Progress on solving theory problem (status of proofs)

What challenges you're facing

Lessons learned so far
