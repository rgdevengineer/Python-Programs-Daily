
'''
Find the Median of a Sorted Array Using Merge
Input: Two sorted arrays: [1, 3] and [2]
Output: 2.0
'''

def find_median_sorted_arrays(nums1, nums2):
    merged = []
    i = j = 0

    # Merge step (like in merge sort)
    while i < len(nums1) and j < len(nums2):
        if nums1[i] <= nums2[j]:
            merged.append(nums1[i])
            i += 1
        else:
            merged.append(nums2[j])
            j += 1

    # Append remaining elements
    while i < len(nums1):
        merged.append(nums1[i])
        i += 1
    while j < len(nums2):
        merged.append(nums2[j])
        j += 1

    n = len(merged)
    if n % 2 == 1:
        return float(merged[n // 2])
    else:
        mid1 = merged[n // 2 - 1]
        mid2 = merged[n // 2]
        return (mid1 + mid2) / 2.0
