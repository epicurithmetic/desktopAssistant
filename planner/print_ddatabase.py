# This file contains the code required to print the daily planner in a nice manner.
# In particular we want each subtask layer to have identation.

example = [
    ["First task",
        ["subtask_1",
            ["subsubtask_1","subsubtask_2"]
        ],
        ["subtask_2",
            []
        ]
    ],
    ["Second task",
        ["subtask",
        []]]
    ]

for x in example:
    print(" "*5 + "[ ]" + x[0])


    for y in x[1:]:
        print(" "*10 + "[ ]" + y[0])


        for z in y[1:]:
            if len(z) == 0:
                pass
            else:
                print(" "*15 + "[ ]" + z[0])
