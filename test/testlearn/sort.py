#coding:utf8

#冒泡排序
s = [1,3,76,4,3453,87,9]
l = len(s)
for j in range(l):
    for i in range(l-1):
        if s[i] > s[i+1]:
            s[i],s[i+1] = s[i+1] , s[i]

print(s)

# 选择排序
s = [1,3,76,4,3453,87,9]
for i in range(len(s)):
    min_index = i
    for j in range(i+1,len(s)):
        if s[min_index]> s[j]:
            s[min_index],s[j] = s[j],s[min_index]
print(s)


# 快排
def quick_sort(li, start, end):
    # 分治 一分为二
    # start=end ,证明要处理的数据只有一个
    # start>end ,证明右边没有数据
    if start >= end:
        return
    # 定义两个游标，分别指向0和末尾位置
    left = start
    right = end
    # 把0位置的数据，认为是中间值
    mid = li[left]
    while left < right:
        # 让右边游标往左移动，目的是找到小于mid的值，放到left游标位置
        while left < right and li[right] >= mid:
            right -= 1
        li[left] = li[right]
        # 让左边游标往右移动，目的是找到大于mid的值，放到right游标位置
        while left < right and li[left] < mid:
            left += 1
        li[right] = li[left]
    # while结束后，把mid放到中间位置，left=right
    li[left] = mid
    # 递归处理左边的数据
    quick_sort(li, start, left - 1)
    # 递归处理右边的数据
    quick_sort(li, left + 1, end)

# def quicksort(arr,n,start,end):
#     if end<start:
#         return -1
#     else:
#         mid = (start+end)/2
#         if

if __name__ == '__main__':
    l = [6, 5, 4, 3, 2, 1]
    # l = 3 [2,1,5,6,5,4]
    # [2, 1, 5, 6, 5, 4]
    quick_sort(l, 0, len(l) - 1)
    print(l)
    # 稳定性：不稳定
    # 最优时间复杂度：O(nlogn)
    # 最坏时间复杂度：O(n^2)