"""1001 害死人不偿命的(3n+1)猜想 (15 分)"""
# n = int(input())
# step = 0
# while n != 1:
#     if n % 2 == 0:
#         n = n / 2
#     else:
#         n = (3 * n + 1) / 2
#     step += 1
# print(step)

"""1002 写出这个数 （20 分）"""
# instr = input()
# sum = 0
# listDic = ['ling', 'yi', 'er', 'san', 'si', 'wu', 'liu', 'qi', 'ba', 'jiu']
# for i in instr:
#     sum += int(i)
# strSum = str(sum)
# flag = True;
# res = str()
# for i in strSum:
#     if flag:
#         res += listDic[int(i)]
#         flag = False
#     else:
#         res += ' ' + listDic[int(i)]
# print(res)

"""1004 成绩排名 （20 分）"""
# n = int(input())
# name = []
# number = []
# score = []
# for i in range(n):
#     ss = input().split()
#     name.append(ss[0])
#     number.append(ss[1])
#     score.append(int(ss[2]))
# maxS, minS = -1, 101
# maxI, minI = 0, 0
# for i in range(n):
#     if score[i] > maxS:
#         maxS = score[i]
#         maxI = i
#     if score[i] < minS:
#         minS = score[i]
#         minI = i
# print(name[maxI], number[maxI])
# print(name[minI], number[minI])

"""1005 继续(3n+1)猜想 （25 分）"""
# n = int(input())
# nums = input().split()
# keys = set()
# res = []
# for num in nums:
#     nNum = int(num)
#     if nNum not in keys:
#         res.append(nNum)
#     while nNum != 1 and nNum not in keys:
#         keys.add(nNum)
#         if nNum % 2 == 0:
#             nNum /= 2
#         else:
#             nNum = (3 * nNum + 1) / 2
#     if nNum in res:
#         res.remove(nNum)
# res.sort(reverse=True)
# for r in res:
#     if r == res[-1]:
#         print(r)
#     else:
#         print(r, end=" ")

"""1006 换个格式输出整数 （15 分）"""
# n = int(input())
# res = str()
# num = n // 100
# res += num * 'B'
# n %= 100
# num = n // 10
# res += num * 'S'
# n %= 10
# for i in range(1, n+1):
#     res += str(i)
# print(res)

"""1007 素数对猜想 （20 分）"""
# import math
# def getPrime(primes, n):
#     array = [0] * (n+1)
#     for i in range(2, int(math.sqrt(n)) + 1):
#         for j in range(i*2, n+1, i):
#             array[j] = 1
#     for i in range(2, n+1):
#         if array[i] == 0:
#             primes.append(i)
#
# n = int(input())
# primes = []
# getPrime(primes, n)
# res = 0
# for i in range(len(primes)-1):
#     if primes[i+1] - primes[i] == 2:
#         res += 1
# print(res)

"""1008 数组元素循环右移问题 （20 分）"""
# list1 = input().split()
# list2 = input().split()
# N = int(list1[0])
# M = int(list1[1])
# a = list2[N-M:]
# b = list2[:N-M]
# print(' '.join(a+b))

"""1009 说反话 （20 分）"""
# s = input().split()
# s.reverse()
# print(' '.join(s))

"""1010 一元多项式求导 （25 分）"""
# lis = list(map(int, input().split()))
# res = []
# for i in range(0, len(lis), 2):
#     if lis[i+1] == 0:
#         continue
#     res.append(str(lis[i] * lis[i+1]))
#     res.append(str(lis[i+1] - 1))
# if res:
#     print(' '.join(res))
# else:
#     print('0 0')

"""1011 A+B 和 C （15 分）"""
# n = int(input())
# for i in range(1, n+1):
#     nums = list(map(int, input().split()))
#     outs = 'true' if nums[0] + nums[1] > nums[2] else 'false'
#     print("Case #%d: %s" % (i, outs))

"""1012 数字分类 （20 分）"""
# nums = list(map(int, input().split()))
# n = nums[0]
# nums.remove(n)
# res = [0 for i in range(5)]
# cnt = [0 for i in range(5)]
# for item in nums:
#     if item % 10 == 0:
#         res[0] += item
#         cnt[0] += 1
#     elif item % 5 == 1:
#         res[1] += (-1)**cnt[1] * item
#         cnt[1] += 1
#     elif item % 5 == 2:
#         res[2] += 1
#         cnt[2] += 1
#     elif item % 5 == 3:
#         res[3] += item
#         cnt[3] += 1
#     elif item % 5 == 4:
#         res[4] = max(res[4], item)
#         cnt[4] += 1
#
# for i in range(5):
#     if cnt[i] == 0:
#         res[i] = 'N'
# res[3] = 'N' if cnt[3] == 0 else round(res[3]/cnt[3], 1)
# for i in range(5):
#     if res[i] != 'N':
#         res[i] = str(res[i])
# print(' '.join(res))

"""1013 数素数 （20 分）"""
# import math
# def calPrime(listP):
#     n = 200000
#     sqrtn = int(math.sqrt(n) + 1)
#     nums = [0] * n
#     for i in range(2, sqrtn):
#         for j in range(2*i, n, i):
#             nums[j] = 1
#     for i in range(2, n):
#         if nums[i] == 0:
#             listP.append(str(i))
#
# inNums = list(map(int, input().split()))
# M, N = inNums[0], inNums[1]
# listP = []
# calPrime(listP)
# res = []
# for i in range(M-1, N, 10):
#     if i+10 > N:
#         res.append(' '.join(listP[i:N]))
#     else:
#         res.append(' '.join(listP[i:i+10]))
# for i in range(0, len(res)):
#     print(res[i])

"""1014 福尔摩斯的约会 （20 分）"""
# str1 = input()
# str2 = input()
# str3 = input()
# str4 = input()
# days = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']
# hhs = [chr(i) for i in range(ord('A'), ord('Z')+1)]
# for i in range(min(len(str1), len(str2))):
#     if 'A'<=str1[i]<='G' and str1[i]==str2[i]:
#         k = i
#         day = days[hhs.index(str1[i])]
#         break
# for i in range(k+1, min(len(str1), len(str2))):
#     if 'A'<=str1[i]<='N' and str1[i]==str2[i]:
#         hh = str(10 + hhs.index(str1[i]))
#         break
#     elif '0'<=str1[i]<='9' and str1[i]==str2[i]:
#         hh = '0' + str1[i]
#         break
# for i in range(min(len(str3), len(str4))):
#     if str3[i].isalpha() and str3[i] == str4[i]:
#         if i < 10:
#             mm = '0' + str(i)
#         else:
#             mm = str(i)
#         break
# print("%s %s:%s" % (day, hh, mm))

"""1015 德才论 （25 分）"""
# nums = list(map(int, input().split()))
# N, L, H = nums[0], nums[1], nums[2]
# list1 = []
# list2 = []
# list3 = []
# list4 = []
# for i in range(N):
#     datas = tuple(map(int, input().split()))
#     if datas[1]>=H and datas[2]>=H:
#         list1.append(datas)
#     elif datas[1]>=H and L<=datas[2]<H:
#         list2.append(datas)
#     elif datas[1]>=L and datas[2]>=L and datas[1]>=datas[2]:
#         list3.append(datas)
#     elif datas[1]>=L and datas[2]>=L:
#         list4.append(datas)
# list1.sort(key=lambda lt: ((-lt[1] - lt[2]), -lt[1], lt[0]))
# list2.sort(key=lambda lt: ((-lt[1] - lt[2]), -lt[1], lt[0]))
# list3.sort(key=lambda lt: ((-lt[1] - lt[2]), -lt[1], lt[0]))
# list4.sort(key=lambda lt: ((-lt[1] - lt[2]), -lt[1], lt[0]))
# print(len(list1) + len(list2) + len(list3) + len(list4))
# for i in range(len(list1)):
#     print("%d %d %d" % (list1[i][0], list1[i][1], list1[i][2]))
# for i in range(len(list2)):
#     print("%d %d %d" % (list2[i][0], list2[i][1], list2[i][2]))
# for i in range(len(list3)):
#     print("%d %d %d" % (list3[i][0], list3[i][1], list3[i][2]))
# for i in range(len(list4)):
#     print("%d %d %d" % (list4[i][0], list4[i][1], list4[i][2]))

"""1016 部分A+B （15 分）"""
# nums = input().split()
# strA, strB = str(), str()
# for i in range(len(nums[0])):
#     if nums[1] == nums[0][i]:
#         strA += nums[1]
# for i in range(len(nums[2])):
#     if nums[3] == nums[2][i]:
#         strB += nums[3]
# if strA is str():
#     strA = '0'
# if strB is str():
#     strB = '0'
# print(int(strA) + int(strB))

"""1017 A除以B （20 分）"""
# nums = list(map(int, input().split()))
# Q = nums[0] // nums[1]
# R = nums[0] % nums[1]
# print(Q, R)

"""1018 锤子剪刀布 （20 分）"""
# N = int(input())
# x, y, z = 0, 0, 0
# nums1 = [0, 0, 0]
# nums2 = [0, 0, 0]
# type = ['B', 'C', 'J']
# for i in range(N):
#     res = input().split()
#     if res[0] == res[1]:
#         y += 1
#     elif res[0] == 'C' and res[1] == 'J':
#         x += 1
#         nums1[1] += 1
#     elif res[0] == 'C' and res[1] == 'B':
#         z += 1
#         nums2[0] += 1
#     elif res[0] == 'J' and res[1] == 'C':
#         z += 1
#         nums2[1] += 1
#     elif res[0] == 'J' and res[1] == 'B':
#         x += 1
#         nums1[2] += 1
#     elif res[0] == 'B' and res[1] == 'C':
#         x += 1
#         nums1[0] += 1
#     elif res[0] == 'B' and res[1] == 'J':
#         z += 1
#         nums2[2] += 1
# print(x, y, z)
# print(z, y, x)
# print(type[nums1.index(max(nums1))], type[nums2.index(max(nums2))])

"""1019 数字黑洞 （20 分）"""
# def heid(s):
#     big = ''.join(sorted(s, reverse=True))
#     small = ''.join(sorted(s))
#     res = str(int(big) - int(small))
#     if len(res) < 4:
#         res = '0' *(4-len(res)) + res
#     print("%s - %s = %s" % (big, small, res))
#     return res
#
# num = input()
# if len(num) < 4:
#     num += '0' * (4-len(num))
# str1 = heid(num)
# while str1 != '0000':
#     if str1 == '6174':
#         break
#     str1 = heid(str1)

"""1020 月饼 （25 分）"""
# N, D = list(map(int, input().split()))
# goods = list(map(float, input().split()))
# price = list(map(float, input().split()))
# rates = {i: price[i]/goods[i] for i in range(N)}
# order = sorted(rates, key=lambda i: rates[i], reverse=True)
# res = 0
# for i in order:
#     if D > goods[i]:
#         res += price[i]
#         D -= goods[i]
#     else:
#         res += rates[i] * D
#         break
# print("%.2f" % res)

"""1021 个位数统计 （15 分）"""
# n = input()
# for i in range(10):
#     num = n.count(str(i))
#     if num != 0:
#         print("%d:%d" % (i, num))

"""1022 D进制的A+B （20 分）"""
# def radix(num, rad):
#     if num == 0:
#         return '0'
#     res = str()
#     while num != 0:
#         mod = num % rad
#         res = str(mod) + res
#         num = num // rad
#     return res
#
# A, B, D = list(map(int, input().split()))
# sum = A + B
# print(radix(sum, D))

"""1023 组个最小数 （20 分）"""
# nums = list(map(int, input().split()))
# res = []
# for i, d in enumerate(nums[1:], start=1):
#     if d != 0:
#         nums[i] -= 1
#         res.append(str(i))
#         break
# for i, d in enumerate(nums, start=0):
#     if d != 0:
#         res.append(d*str(i))
# print(''.join(res))

"""1024 科学计数法 （20 分）"""
# num = input()
# res = '' if num[0]=='+' else '-'
# digit, index = num[1:].split('E')
# A, B = digit.split('.')
# length = int(index)
# if length == 0:
#   print(res+A+'.'+B)
# elif length > 0:
#   if length > len(B):
#     print(res+A+B+'0'*(length-len(B)))
#   else:
#     print(res+A+B[:length]+'.'+B[length:])
# else:
#   print(res+'0.'+(-length-1)*'0'+A+B)

"""1026 程序运行时间 （15 分）"""
# C1, C2 = list(map(int, input().split()))
# C = (C2 - C1 + 50) // 100
# hh = C // 3600
# mm = (C % 3600) // 60
# ss = C % 60
# print("%02d:%02d:%02d" % (hh, mm, ss))

"""1027 打印沙漏 （20 分）"""
# import math
# Nn, ch = input().split()
# N = math.floor(math.sqrt((int(Nn)+1) // 2))
# len = 2*N-1
# for i in range(N):
#     print((' '*i) + (ch*(len-2*i)))
# for i in range(1, N):
#     print((' '*((len-1)//2-i)) + (ch*(2*i+1)))
# print(int(Nn) - 2*N*N+1)

"""1028 人口普查 （20 分）"""
# n = int(input())
# res = 0
# youngMan, olderMan = '2015/09/06', '1714/09/06'
# yName, oName = str(), str()
# for i in range(n):
#     name, year = input().split()
#     if year > '2014/09/06' or year < '1814/09/06':
#         continue
#     else:
#         res += 1
#         if year > olderMan:
#             olderMan = year
#             oName = name
#         if year < youngMan:
#             youngMan = year
#             yName = name
# if res == 0:
#     print(0)
# else:
#     print(res, yName, oName)
