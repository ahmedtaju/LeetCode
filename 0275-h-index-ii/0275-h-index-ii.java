class Solution {
    public int hIndex(int[] citations) {
        int lower = 0;
        int upper = 5000;
        int index = -1;
        
        while(lower < upper) {
            int mid = lower + (upper - lower+1)/2;
            if(graterThanOrEqual(citations,mid,0,citations.length-1) >= mid) {
                lower = mid;
            } else {
                upper = mid-1; 
            }
        }
        
        return lower;
    }

    int graterThanOrEqual(int [] arr , int num , int start , int end) {
        while(start < end) {
            int mid = start + (end - start)/2;

            if(arr[mid] >= num) {
                end = mid;
            } else start = mid+1;
        }

        if(arr[start] < num)
            return 0;

        return arr.length - start;
    }
}