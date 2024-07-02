## Quick start
### 1. Clone this [repo](https://github.com/project-kessel/relations-api) and run

```
make relations-api-up
```


### 2. Test it!

```
cd examples
./run_examples.sh
```
output:
```
--Start of CreateTuples--

--End of CreateTuples--

--Start of ReadTuples--
Resource ID: bob_club
Resource Type: group
Relation: member
Subject Type: user
Subject Type: bob
--End of ReadTuples--

--Start of Check request--
allowed
--End of Check request--

--Start of LookupSubjects--
Subject ID: bob
Resource Type: user
--End of LookupSubjects--

--Start of LookupResources--
Resource Type: group
Resource ID: bob_club
--End of LookupResources--
```

### 3. Test validation example

In `run_examples` file change PYTHON_SCRIPT

PYTHON_SCRIPT="client_validations.py"


