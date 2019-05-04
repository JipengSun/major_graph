# major_graph
Extract knowledge points from slides.
## 2019.03.04
Design the initial 5 tier hierachy structure for knowledge in slides. 
## 2019.03.08
Build the KG Demo by csv importing
## 2019.05.02
1. NEO4J was used to visualize test data, MERGE operation has been well studied.
2. Level search for the candidate test data.
3. Py2neo has been studied but be discarded due to its buggy design for merge operations. Alternatively, saving the data to CSV file and loading CSV by CQL is quite acceptable.
## 2019.05.03
1. Build groundtruth graph for test ppt
2. Make trials on similarity based and local based building strategies.
