# Dung Abstract Argumentation Framework Package - V 1.0 (2020)

### Developed by Agustina Dinamarca
### agustinadinamarca@gmail.com

This repository contains a Python implementation of Dung's theory. For details about the Abstract Argumentation Framework (AF) proposed by Dung in 1995 read the following article:
```
Dung-1995.pdf
```
To test the implementation run the examples in the *Jupyter* Notebook attached.

The set of arguments *A* and the set of attack relationships *attacks* between the arguments must be specified. 
Example:
```
A = {"a", "b", "c"}
attacks = {("b", "c"), ("c", "a")}
```
In this example, a tuple like ```("b", "c")``` represents an attack: "b" represents
an attack against "c". 

Four acceptability semantics were implemented:
* Stable
* Complete
* Grounded
* Preferred

For each argument *a* in *A* we can define its status under a given semantics:
* Skeptically accepted
* Credulously accepted
* Rejected

