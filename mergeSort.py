def merge(l_a, r_a):
    """
    ？把两个有序数组，按照谁小填入新的数组里，如果又没访问完的，就直接在后面追加。
    """
    # 临时数组
    tmp = []
    # 首位下标初始化
    l_ids = r_ids = 0

    # 如果标没有超过两个数组的大小就循环
    while l_ids < len(l_a) and r_ids < len(r_a):
        # 比较大小，谁小就先放到tmp里
        if l_a[l_ids] < r_a[r_ids]:
            tmp.append(l_a[l_ids])
            # 如果第一个数组的只放进去了，就比较下一个
            l_ids += 1
        else:
            tmp.append(r_a[r_ids])
            r_ids += 1

    # 循环跳出证明有一组放完了，剩下的就直接追加
    if l_ids == len(l_a):
        tmp = tmp + r_a[r_ids:]
    else:
        tmp = tmp + l_a[l_ids:]
    return tmp


def mergeSort(array):
    """
    ？归并排序
    """
    array_length = len(array)
    # 停止递归
    if array_length < 2:
        return array
    # 求中间值，要把数组一分为二
    middle = array_length >> 1
    # 用递归分别把数组分割到最小
    left_array = mergeSort(array[:middle])
    right_array = mergeSort(array[middle:])
    # 合并数组
    return merge(left_array, right_array)


if __name__ == "__main__":
    list1 = [14, 2, 34, 43, 21, 19]
    print(mergeSort(list1))
