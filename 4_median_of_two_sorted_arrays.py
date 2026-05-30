class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = total // 2

        # check A shorter than B
        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True: #BS on shorter A
            i = (l + r) // 2 #A
            j = half - i - 2 #B (-2 because 0-indexed)

            Aleft = A[i] if i >= 0 else float('-inf')
            Aright = A[(i + 1)] if (i+1) < len(A) else float('inf')
            Bleft = B[j] if j >= 0 else float('-inf')
            Bright = B[(j + 1)] if (j+1) < len(B) else float('inf')

            if Aleft <= Bright and Bleft <= Aright:    
                # odd
                if (total % 2):
                    return min(Aright, Bright)
                else: # even
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright: # too big, find smaller
                r = i - 1
            else: # too small, find bigger (Bleft > Aright)
                l = i + 1