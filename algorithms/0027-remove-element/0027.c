int removeElement(int* nums, int numsSize, int val) {
    int i = 0;
    int j = numsSize;
    
    while (i < j) {
        if (nums[i] == val) {
            nums[i] = nums[j - 1]; 
            j--; 

        } else i++;
    }
    
    return j; 
}