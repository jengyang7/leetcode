class Solution {
    public int[][] merge(int[][] intervals) {
        if (intervals.length <= 1){
            return intervals;
        }

        // step 1: sort the intervals bases on the starting value
        Arrays.sort(intervals, (a, b) -> Integer.compare(a[0], b[0]));

        // step 2: initialize a list to hold the merged intervals
        List<int[]> merged = new ArrayList<>();

        // start with the first interval
        int[] currentInterval = intervals[0];
        merged.add (currentInterval);

        // step 3: iterate through the sorted intervals
        for (int[] interval: intervals) {
            int currentEnd = currentInterval[1];
            int nextStart = interval[0];
            int nextEnd = interval[1];

            if (currentEnd >= nextStart){
                // overlap exist: merge by taking the max end time
                currentInterval[1] = Math.max(currentEnd, nextEnd);
            } else{
                // no overlap: move to next interval and add it to the list
                currentInterval = interval;
                merged.add(currentInterval);
            }
        }

        // step 4: convert list back to a 2D array
        return merged.toArray(new int[merged.size()][]);
    }
}