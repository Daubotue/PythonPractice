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

"""1029 旧键盘 （20 分）"""
# inA = list(input())
# inB = input()
# for i in inB:
#     inA.remove(i) if i in inA else None
# for i in range(len(inA)):
#     if (ord(inA[i])>=ord('a')) and (ord(inA[i])<=ord('z')):
#         inA[i] = chr(ord(inA[i]) - 32)
# res = []
# for i in inA:
#     if i not in res:
#         res.append(i)
# print(''.join(res))

"""1030 完美数列 （25 分）"""
# N, p = [int(i) for i in input().split()]
# sl = sorted([int(i) for i in input().split()])
# res = 0
# for i in range(N):
#     for j in range(i+res, N):
#         if sl[i] * p < sl[j]:
#             break
#         res += 1
# print(res)

"""1031 查验身份证 （15 分）"""
# Z = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
# M = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
# N = int(input())
# flag = 0
# for i in range(N):
#     num = input()
#     if len(num) != 18:
#         print(num)
#         flag = 1
#     else:
#         sum = 0
#         mark = 0
#         for j in range(17):
#             try:
#                 sum += int(num[j]) * Z[j]
#             except:
#                 print(num)
#                 mark = 1
#                 flag = 1
#                 break
#         if mark == 0:
#             if M[sum % 11] != num[-1]:
#                 print(num)
#                 flag = 1
# if flag == 0:
#     print('All passed')

"""1032 挖掘机技术哪家强 （20 分）"""
# N = int(input())
# scores = [0] * (N+1)
# for i in range(N):
#     id, src = list(map(int, input().split()))
#     scores[id] += src
# res = scores.index(max(scores))
# print(res, scores[res])

"""1033 旧键盘打字 （20 分）"""
# broke = input()
# content = input()
# res = str()
# for s in content:
#     if s.isalpha():
#         ch = s.upper()
#     else:
#         ch = s
#     if ch not in broke:
#         if '+' not in broke or (False == ch.isalpha()) or s.islower():
#             res += s
# print(res)

"""1036 跟奥巴马一起编程 （15 分）"""
# N, C = input().split()
# row = (int(N) + 1) // 2
# col = int(N)
# for i in range(row):
#     if i==0 or i==row-1:
#         print(''.join([C]*col))
#     else:
#         print(''.join([C]+[' ']*(col-2)+[C]))

"""1037 在霍格沃茨找零钱 （20 分）"""
# a, b = input().split()
# numA = a.split('.')
# numB = b.split('.')
# moneyA = int(numA[0])*17*29 + int(numA[1])*29 + int(numA[2])
# moneyB = int(numB[0])*17*29 + int(numB[1])*29 + int(numB[2])
# change = moneyB - moneyA
# if change < 0:
#     print('-', end='')
#     change = -change;
# print('%d.%d.%d' % (change//(17*29), (change%(17*29))//29, change%29))

"""1038 统计同成绩学生 （20 分）"""
# N = int(input())
# scr = list(map(int, input().split()))
# M = list(map(int, input().split()))
# for i in range(1, M[0]+1):
#     if i == M[0]:
#         print(scr.count((M[i])))
#     else:
#         print(scr.count(M[i]), end=' ')

"""1039 到底买不买 （20 分）"""
# a = list(input())
# b = list(input())
# pos = 0
# while pos < len(b):
#     if b[pos] in a:
#         a.remove(b[pos])
#         del(b[pos])
#     else:
#         pos += 1
# if len(b) == 0:
#     print('Yes', len(a))
# else:
#     print('No', len(b))

"""1040 有几个PAT （25 分）"""
# ss = input()
# numP, numPA, numPAT = 0, 0, 0
# for i in range(len(ss)):
#     if ss[i] == 'P':
#         numP += 1
#     elif ss[i] == 'A':
#         numPA += numP
#     elif ss[i] == 'T':
#         numPAT += numPA
# print(numPAT % 1000000007)

"""1041 考试座位号 （15 分）"""
# N = int(input())
# info = []
# for i in range(N):
#     stu = input().split()
#     info.append(stu)
# M = int(input())
# id = input().split()
# for i in id:
#     for single in info:
#         if single[1] == i:
#             print(single[0], single[2])
#             break

"""1042 字符统计 （20 分）"""
# s = input()
# dic = [chr(i) for i in range(ord('a'), ord('z')+1)]
# times = []
# s = s.lower()
# for i in dic:
#     cnt = s.count(i)
#     times.append(cnt)
# res = max(times)
# index = times.index(res)
# print(dic[index], res)

"""1043 输出PATest （20 分）"""
# s = input()
# dic = list('PATest')
# cnts = [0] * 6
# for i in s:
#     if i == 'P':
#         cnts[0] += 1
#     elif i == 'A':
#         cnts[1] += 1
#     elif i == 'T':
#         cnts[2] += 1
#     elif i == 'e':
#         cnts[3] += 1
#     elif i == 's':
#         cnts[4] += 1
#     elif i == 't':
#         cnts[5] += 1
# res = str()
# while max(cnts) > 0:
#     for i in range(6):
#         if cnts[i] != 0:
#             res += dic[i]
#             cnts[i] -= 1
# print(res)

"""1044 火星数字 （20 分）"""
# units = 'tret, jan, feb, mar, apr, may, jun, jly, aug, sep, oct, nov, dec'.split(', ')
# decades = ', tam, hel, maa, huh, tou, kes, hei, elo, syy, lok, mer, jou'.split(', ')
#
# def earth2mars(num):
#     if num > 12:
#         ll = []
#         ll.append(decades[num // 13])
#         if num % 13 != 0:
#             ll.append(units[num % 13])
#         print(' '.join(ll))
#     else:
#         print(units[num % 13])
#
# def mars2earth(num):
#     ll = num.split()
#     res = 0
#     if len(ll) > 1:
#         res = decades.index(ll[0]) * 13 + units.index(ll[1])
#     elif ll[0] in decades:
#         res = decades.index(ll[0]) * 13
#     elif ll[0] in units:
#         res = units.index(ll[0])
#     print(res)
#
# N = int(input())
# for i in range(N):
#     a = input()
#     if a.isdigit():
#         earth2mars(int(a))
#     else:
#         mars2earth(a)

"""1045 快速排序 （25 分）"""
# N = int(input())
# nums = list(map(int, input().split()))
# res = []
# nMax = 0
# for i in range(N):
#     if nums[i] > nMax:
#         nMax = nums[i]
#         res.append(nMax)
#     else:
#         for j in range(len(res)-1, -1, -1):
#             if res[j] >= nums[i]:
#                 del res[j]
#             else:
#                 break
# res.sort()
# print(len(res))
# if len(res) == 0:
#     print("")
# else:
#     for i in range(len(res)):
#         if i == len(res) - 1:
#             print(res[i])
#         else:
#             print(res[i], end=' ')

"""1046 划拳 （15 分）"""
# N = int(input())
# cntA, cntB = 0, 0
# for i in range(N):
#     nums = list(map(int, input().split()))
#     su = nums[0] + nums[2]
#     if su == nums[1] and su != nums[3]:
#         cntB += 1
#     elif su == nums[3] and su != nums[1]:
#         cntA += 1
# print(cntA, cntB)

"""1047 编程团体赛 （20 分）"""
# N = int(input())
# res = {}
# for i in range(N):
#     a = input().split()
#     b = a[0].split('-')
#     if b[0] in res:
#         res[b[0]] += int(a[1])
#     else:
#         res[b[0]] = int(a[1])
# maxKey = str()
# nMax = 0
# for u in res:
#     if res[u] > nMax:
#         nMax = res[u]
#         maxKey = u
# print(maxKey, nMax)

"""1049 数列的片段和 （20 分）"""
# N = int(input())
# nums = list(map(float, input().split()))
# res = 0
# for i in range(len(nums)):
#     res += nums[i] * (i+1) * (len(nums)-i)
# print("%.2f" % res)

"""1050 螺旋矩阵 （25 分）"""
# import numpy as np
# import math
#
# N = int(input())
# cols = int(math.sqrt(N))
# rows = 0
# while (N % cols != 0):
#     cols -= 1
# rows = N // cols
# nums = list(map(int, input().split()))
# nums.sort(reverse=True)
# mat = np.zeros([rows, cols], np.uint8)
# k = 0
# i, j = 0, 0
# XL, XR, YU, YD = 0, cols, 0, rows
# while k < N:
#     while k<N and j<XR:
#         mat[i, j] = nums[k]
#         j += 1
#         k += 1
#     j -= 1
#     YU += 1
#     i += 1
#     while k<N and i<YD:
#         mat[i, j] = nums[k]
#         i += 1
#         k += 1
#     i -= 1
#     XR -= 1
#     j -= 1
#     while k<N and j>=XL:
#         mat[i, j] = nums[k]
#         j -= 1
#         k += 1
#     j += 1
#     YD -= 1
#     i -= 1
#     while k<N and i>=YU:
#         mat[i, j] = nums[k]
#         i -= 1
#         k += 1
#     i += 1
#     XL += 1
#     j += 1
# for i in range(mat.shape[0]):
#     for j in range(mat.shape[1]):
#         if j == mat.shape[1]-1:
#             print(mat[i, j])
#         else:
#             print(mat[i, j], end=' ')

"""1051 复数乘法 （15 分）"""
# import math
# nums = list(map(float, input().split()))
# A1 = nums[0] * math.cos(nums[1])
# B1 = nums[0] * math.sin(nums[1])
# A2 = nums[2] * math.cos(nums[3])
# B2 = nums[2] * math.sin(nums[3])
# A = A1 * A2 - B1 * B2
# B = A1 * B2 + B1 * A2
# if A>=-0.005 and A<0:
#     print('0.00', end='')
# else:
#     print('%.2f' % A, end='')
# if B >= 0:
#     print('+%.2fi' % B)
# elif B>=-0.005 and B<0:
#     print('+0.00i')
# else:
#     print('%.2fi' % B)

"""1053 住房空置率 （20 分）"""
# N, e, D = input().split()
# N, e, D = int(N), float(e), int(D)
# num1, num2 = 0, 0
# for i in range(N):
#     days = input().split()
#     cnt = 0
#     for j in range(1, int(days[0])+1):
#         if float(days[j]) < e:
#             cnt += 1
#     if cnt/int(days[0]) > 0.5 and int(days[0]) <= D:
#         num1 += 1
#     elif cnt/int(days[0]) > 0.5 and int(days[0]) > D:
#         num2 += 1
# print('%.1f%% %.1f%%' % (100*num1/N, 100*num2/N))

"""1054 求平均值 （20 分）"""
# import re
#
# def matchNum(num):
#     reg = r'^[-]?(\d{0,3}|1000)$|^[-]?\d{0,3}\.\d{0,2}$|^[-]?1000\.0{0,2}$'
#     m = re.match(reg, num)
#     if m:
#         return True
#     else:
#         return False
#
# N = int(input())
# nums = input().strip().split()
# k, sum = 0, 0.0
# for i in range(N):
#     if matchNum(nums[i]):
#        k += 1
#        sum += float(nums[i])
#     else:
#         print('ERROR: %s is not a legal number' % nums[i])
# if k == 0:
#     print('The average of 0 numbers is Undefined')
# elif k == 1:
#     print('The average of 1 number is %.2f' % sum)
# else:
#     print('The average of %d numbers is %.2f' % (k, sum/k))

"""1055 集体照 （25 分）"""
# N, K = list(map(int, input().split()))
# lst = []
# for i in range(N):
#     [name, height] = input().split()
#     lst.append([name, int(height)])
# lst.sort(key=lambda x: (-x[1], x[0]))
# rows = N // K
# col = N - (K-1) * rows
# pRow = [lst[:col]]+[lst[col+i*rows:col+(i+1)*rows] for i in range(K-1)]
# for i in range(K):
#     length = len(pRow[i])
#     res = ['']*length
#     mid = length // 2
#     cnt = 1
#     res[mid] = pRow[i][0][0]
#     for j in range(1, length, 2):
#         if j == length - 1:
#             res[mid-cnt] = pRow[i][j][0]
#         else:
#             res[mid-cnt] = pRow[i][j][0]
#             res[mid+cnt] = pRow[i][j+1][0]
#             cnt += 1
#     print(' '.join(res))

"""1061 判断题 （15 分)"""
# N, M = map(int, input().split())
# scores = list(map(int, input().split()))
# answers = input().split()
# for i in range(N):
#     stu = input().split()
#     tot = 0
#     for j in range(M):
#         if stu[j] == answers[j]:
#            tot += scores[j]
#     print(tot)

"""1062 最简分数 （20 分)"""
# def isMini(denom, num):
#     a = max(denom, num)
#     b = min(denom, num)
#     while b:
#         c = a % b
#         a, b = b, c
#     if a == 1:
#         return True
#     else:
#         return False
#
#
# A, B, K = input().split()
# K = int(K)
# N1, M1 = map(int, A.split('/'))
# N2, M2 = map(int, B.split('/'))
# l1 = min(float(N1) / M1, float(N2) / M2)
# l2 = max(float(N1) / M1, float(N2) / M2)
# res = []
# tot = 0
# for i in range(1, K):
#     rs = float(i) / K
#     if rs >= l2:
#         break
#     elif rs > l1:
#         if isMini(i, K):
#             res.append(i)
#             tot += 1
# for i in range(0, tot-1):
#     print('%d/%d' % (res[i], K), end=' ')
# print('%d/%d' % (res[tot-1], K))

"""1063 计算谱半径 （20 分)"""
# import math
# N = int(input())
# res = 0
# for i in range(N):
#     a, b = map(int, input().split())
#     res = max(res, a*a+b*b)
# print("%.2f" % math.sqrt(res))

"""1064 朋友数 （20 分)"""
# def calSum(num):
#     sum = 0
#     while num:
#         sum += num % 10
#         num = int(num / 10)
#     return sum
#
# N = int(input())
# res = []
# nums = list(map(int, input().split()))
# nLen = 0
# for i in range(N):
#     sum = calSum(nums[i])
#     if sum not in res:
#         res.append(sum)
#         nLen += 1
#
# print(nLen)
# res.sort(key=lambda x: x)
# for i in range(nLen-1):
#     print(res[i], end=" ")
# print(res[nLen-1])

"""1065 单身狗 （25 分)"""
# N = int(input())
# dic = {}
# for i in range(N):
#     a, b = input().split()
#     dic[a] = b
# M = int(input())
# persons = input().split()
# personsSet = set(persons)
# keySet = set(dic.keys())
# for per in personsSet:
#     if (per in keySet) and (dic[per] in personsSet):
#         persons.remove(per)
#         persons.remove(dic[per])
# print(len(persons))
# if len(persons) > 0:
#     persons.sort(key= lambda x: x)
#     result = ' '.join(persons)
#     print(result)

"""1066 图像过滤 （15 分)"""
# M, N, A, B, C = map(int, input().split())
# for i in range(M):
#     pixels = list(input().split())
#     res = []
#     for pix in pixels:
#         if A <= int(pix) <= B:
#             res.append('{:03d}'.format(C))
#         else:
#             res.append('{:03d}'.format(int(pix)))
#     print(' '.join(res))

"""1067 试密码 （20 分)"""
# code, N = input().split()
# N = int(N)
# while N > 0:
#     N -= 1
#     inp = input()
#     if inp == '#':
#         break
#     if inp == code:
#         print("Welcome in")
#         break
#     else:
#         if N == 0:
#             print("Wrong password:", inp)
#             print("Account locked")
#         else:
#             print("Wrong password:", inp)

"""1068 万绿丛中一点红 （20 分)"""
# import math
# def isValid(row, col, N, M, pic, ep):
#     uRow = max(row-1, 0)
#     dRow = min(row+1, N-1)
#     lCol = max(0, col-1)
#     rCol = min(M-1, col+1)
#     for r in range(uRow, dRow+1):
#         for c in range(lCol, rCol+1):
#             if (row!=r and col!=c) and math.fabs(pic[row][col]-pic[r][c])<=ep:
#                 return False
#     return True
#
#
# M, N, TOL = map(int, input().split())
# pic = []
# for row in range(N):
#     r = list(map(int, input().split()))
#     pic.append(r)
# dic = {}
# for row in range(N):
#     for col in range(M):
#         if pic[row][col] not in dic.keys():
#             dic[pic[row][col]] = 0
#         dic[pic[row][col]] += 1
# res = []
# for row in range(N):
#     for col in range(M):
#         if (dic[pic[row][col]]==1) and isValid(row, col, N, M, pic, TOL):
#             s = "({0}, {1}): {2}".format(col+1, row+1, pic[row][col])
#             res.append(s)
# if len(res) == 0:
#     print("Not Exist")
# elif len(res) == 1:
#     print(res[0])
# else:
#     print("Not Unique")

"""1069 微博转发抽奖 （20 分)"""
# M, N, S = map(int, input().split())
# bingo = set()
# nameId = []
# for i in range(M):
#     id = input()
#     nameId.append(id)
# index = S-1
# while index < M:
#     if nameId[index] not in bingo:
#         print(nameId[index])
#         bingo.add(nameId[index])
#         index += N
#     else:
#         while index+1 < M:
#             index += 1
#             if nameId[index] not in bingo:
#                 print(nameId[index])
#                 bingo.add(nameId[index])
#                 index += N
#                 break
# if len(bingo) == 0:
#     print("Keep going...")

"""1070 结绳 （25 分)"""
# N = int(input())
# lenLope = list(map(int, input().split()))
# lenLope.sort(key=lambda x: x)
# res = int((lenLope[0] + lenLope[1]) / 2)
# for lp in lenLope[2:]:
#     res = int((res + lp) / 2)
# print(res)

"""1071 小赌怡情 （15 分)"""
# T, K = map(int, input().split())
# for i in range(K):
#     n1, b, t, n2 = map(int, input().split())
#     if T < t:
#         print("Not enough tokens.  Total = %d." % T)
#         continue
#     elif b == 0:
#         if n1 > n2:
#             T += t
#             print("Win %d!  Total = %d." % (t, T))
#         else:
#             T -= t
#             print("Lose %d.  Total = %d." % (t, T))
#     elif b == 1:
#         if n1 < n2:
#             T += t
#             print("Win %d!  Total = %d." % (t, T))
#         else:
#             T -= t
#             print("Lose %d.  Total = %d." % (t, T))
#     if T == 0:
#         print("Game Over.")
#         break

"""1072 开学寄语 （20 分)"""
# N, M = map(int, input().split())
# ilegal = input().split()
# numPeople = 0
# numStuff = 0
# for i in range(N):
#     person = input().split()
#     allStuff = person[2:]
#     res = []
#     for st in allStuff:
#         if st in ilegal:
#             res.append(st)
#             numStuff += 1
#     if len(res) > 0:
#         numPeople += 1
#         print("%s: %s" % (person[0], ' '.join(res)))
# print("%d %d" % (numPeople, numStuff))