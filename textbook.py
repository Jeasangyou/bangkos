Raw_input=[]
while True:
    line = input().strip()  
    if not line:
        break
    Raw_input.append(line.split())

N_M = Raw_input[0]
#print(N_M)

Book_per_pile=[]
for i in range(1, len(Raw_input), 2):
    Book_per_pile.extend(Raw_input[i])
BookNo=[]
for i in range(2, len(Raw_input), 2):
    BookNo.append(Raw_input[i])

#print(Book_per_pile)
#print(BookNo)
matrix=[]
for row in (BookNo):
    if len(row)<int(max(Book_per_pile)):
        row.extend([0]*(int(max(Book_per_pile))-len(row)))
    matrix.append(row)

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        matrix[i][j] = int(matrix[i][j])

#print("matrix:", matrix)

#for row in matrix:
    #print(row)

for row in matrix:    
    if not all(int(row[i]) >= int(row[i+1]) for i in range(len(row) - 1)):
        print("NO")
        break
    else:
        n=len(matrix[0])
        columns = []
        for col_idx in range(n):
            column = [matrix[row_idx][col_idx] for row_idx in range(len(matrix))]
            columns.append(column)

        #for col in columns:
            #print(col)

        final_columns=[]
        for col in columns:
            filtered_col = [item for item in col if item != 0]
            final_columns.append(filtered_col)

        #print(final_columns)

        result = []
        for lst in reversed(final_columns):
            sorted_lst = sorted(lst)  
            result.extend(sorted_lst)

        #print(result)

        if result==sorted(result):
            #print(result, sorted(result))
            print("YES")
            break
        else:
            print("NO")



