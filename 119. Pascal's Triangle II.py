class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        current_row = [1]

        for i in range(1, rowIndex + 1):
            new_row = [1]
            for j in range[1,i]:
                new_row.append(current_row[j -1] + current_row[j])
            new_row.append[1]
            current_row = new_row
        return current_row