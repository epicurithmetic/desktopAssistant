# This file contains the code required to print the daily planner in a nice manner.
# In particular we want each subtask layer to have identation and either [ ] or [X]
# to distinguish complete from incomplete tasks. 

example = [
    ["First task",
        ["subtask_1","subtask_2"]
    ],
    ["Second task",
        ["subtask"]
    ]
]

for x in example:
    print(" "*5 + "[ ]" + x[0])


    for y in x[1:]:
        print(" "*10 + "[ ]" + y[0])
