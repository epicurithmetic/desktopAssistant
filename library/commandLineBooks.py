# An attempt at command-line art: books...?

d = "|"
l = "-"
u = "_"
s =" "


# Book 1
book1_row1 = s + 3*u + s
book1_row2 = d + 3*s + d
book1_row3 = d + 3*l + d
book1_row4 = d + 3*s + d
book1_row5 = d + 3*s + d
book1_row6 = d + 3*s + d
book1_row7 = d + 3*s + d
book1_row8 = d + 3*s + d
book1_row9 = d + 3*s + d
book1_row10 = d + 3*s + d
book1_row11 = d + 3*l + d
book1_row12 = d + 3*s + d
book1_row13 = d + 3*u + d

book1_rows = [book1_row1,
        book1_row2,
        book1_row3,
        book1_row4,
        book1_row5,
        book1_row6,
        book1_row7,
        book1_row8,
        book1_row9,
        book1_row10,
        book1_row11,
        book1_row12,
        book1_row13]

width_book1 = len(book1_row1)

# Book 2
book2_row1 = s*(width_book1)
book2_row2 = s*(width_book1)
book2_row3 = s*(width_book1)
book2_row4 = s*(width_book1)
book2_row5 = s*(width_book1)
book2_row6 = s + 3*u + s
book2_row7 = d + 3*s + d
book2_row8 = d + 3*l + d
book2_row9 = d + 3*s + d
book2_row10 = d + 3*s + d
book2_row11 = d + 3*s + d
book2_row12 = d + 3*l + d
book2_row13 = d + 3*u + d

book2_rows = [book2_row1,
        book2_row2,
        book2_row3,
        book2_row4,
        book2_row5,
        book2_row6,
        book2_row7,
        book2_row8,
        book2_row9,
        book2_row10,
        book2_row11,
        book2_row12,
        book2_row13]

# Book 3
book3_row1 = s*(width_book1)
book3_row2 = s*(width_book1)
book3_row3 = s + 3*u + s
book3_row4 = d + 3*s + d
book3_row5 = d + 3*l + d
book3_row6 = d + 3*s + d
book3_row7 = d + 3*s + d
book3_row8 = d + 3*s + d
book3_row9 = d + 3*s + d
book3_row10 = d + 3*s + d
book3_row11 = d + 3*s + d
book3_row12 = d + 3*l + d
book3_row13 = d + 3*u + d

book3_rows = [book3_row1,
        book3_row2,
        book3_row3,
        book3_row4,
        book3_row5,
        book3_row6,
        book3_row7,
        book3_row8,
        book3_row9,
        book3_row10,
        book3_row11,
        book3_row12,
        book3_row13]

# Book 4
book4_row1 = s*width_book1
book4_row2 = s*width_book1
book4_row3 = s*width_book1
book4_row4 = s + 3*u + s
book4_row5 = d + 3*s + d
book4_row6 = d + 3*l + d
book4_row7 = d + 3*s + d
book4_row8 = d + 3*s + d
book4_row9 = d + 3*s + d
book4_row10 = d + 3*s + d
book4_row11 = d + 3*s + d
book4_row12 = d + 3*l + d
book4_row13 = d + 3*u + d

book4_rows = [book4_row1,
        book4_row2,
        book4_row3,
        book4_row4,
        book4_row5,
        book4_row6,
        book4_row7,
        book4_row8,
        book4_row9,
        book4_row10,
        book4_row11,
        book4_row12,
        book4_row13]


shelf_indent = 15
shelf = [shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s,
        shelf_indent*s]


# Stack the shelf.
for i in range(0,len(shelf)):
    shelf[i] += book4_rows[i] + book3_rows[i] + book1_rows[i] + book2_rows[i]
    shelf[i] += book4_rows[i] + book2_rows[i] + book4_rows[i] + book2_rows[i]
    shelf[i] += book2_rows[i] + book1_rows[i] + book1_rows[i] + book3_rows[i]
    shelf[i] += book4_rows[i] + book3_rows[i] + book1_rows[i] + book2_rows[i]
    shelf[i] += book4_rows[i] + book2_rows[i] + book4_rows[i] + book2_rows[i]
    shelf[i] += book2_rows[i] + book1_rows[i] + book1_rows[i] + book3_rows[i]
    shelf[i] += book2_rows[i] + book1_rows[i] + book1_rows[i] + book3_rows[i]

def bookShelf():

    for i in range(0,len(shelf)):
        print(shelf[i])
