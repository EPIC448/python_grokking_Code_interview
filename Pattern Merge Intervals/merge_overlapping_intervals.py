

'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6]


EXAMple 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.



'''
List = [[1,3],[2,6],[8,10],[15,18]]

class Solution:
    
    class Interval:
        def __init__(self, start, end):
            self.start = start
            self.end = end
    
    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # if there's only one interval there's no merging to be done
        if len(intervals) < 2: return intervals

        # Algo: Sort based on start, end of each interval
        # then iterate through comparing with next element,
        # modifying endpoint of current element if they need to be merged
        # + deleting next element, otherwise leaving them both as is

        # TC: O(NlogN) - Sort list (NlogN), then make one pass of list (N)
        # SC: O(1)     - We merge the intervals in place

        # Sort list based on start of interval, then end of interval if equal
        intervals.sort(key= lambda x: (x[0], x[1]))

        i = 0
        while (i+1) < len(intervals):
            # check for overlap
            # because it's sorted we only need to check if the
            # start of the next interval lies in the current interval
            if intervals[i][0] <= intervals[i+1][0] <= intervals[i][1]:
                
                # if the end of next element is greater than end of current one,
                # we widen the length of current interval to equal it
                if intervals[i+1][1] > intervals[i][1]:
                    intervals[i][1] = intervals[i+1][1]

                # Otherwise the next interval lies inside the current one,
                # so we can just delete it.
                del intervals[i+1]

            # Otherwise no overlap, move on to next comparison
            # We don't increment if we deleted an element
            else:
                i += 1

        return intervals
    