# -*- coding: utf-8 -*-
"""
Proudly an MIT 6.0001 grad and an MIT 6.0002 student
Thank you very much Eric Grimson, John Guttag and Ana Bell for being my teacher!

DIVIDE AND CONQUER


127 Broken Head Rd, Suffolk Park / Byron Bay NSW 2481

Logarithmic nlogn and x squared algorithmic complexity

Thank you Woolworths for delivering my groceries and thank you Centrelink and Australian Government for my disability support payment income


The list: [690, 484, 878, 23, 585, 304, 885, 773, 494, 345]




The maximum pairwise product: 777030 (878 x 885)
Charles Truscott Watters. More efficient, non pointer linked list algorithm
I love you big bro Tai. Thank you MIT

[Program finished]


Charles Truscott


    for x in range(0, 1000, 1):
        L.append(random.randint(0, 1000))
        
        

"""
import random

def merge_order(P=[], Q=[], R=[], S=[], SPARE = []):
    if len(P) > 2:
        R.append(P[:len(P)//2])
        R.append(P[len(P)//2:])
        merge_order(P[:len(P)//2], P[len(P)//2:], [], [])
    if len(Q) > 2:
        R.append(Q[:len(Q)//2])
        R.append(Q[len(Q)//2:])
        merge_order(Q[:len(Q)//2], Q[len(Q)//2:], [], [])
#    print(R)
    for x in range(0, len(R) - 1, 1):
        if (len(R[x]) == 1 and len(R[x + 1]) == 2) or (len(R[x + 1]) == 1 and len(R[x]) == 2):
            SPARE.append(R[x])
            SPARE.append(R[x + 1])

#            if len(R[x]) == 1 and len(R[x + 1]) == 2:
#                S.append([R[x][0], R[x + 1][0], R[x][0] * R[x + 1][0]])
#                S.append([R[x][0], R[x + 1][1], R[x][0] * R[x + 1][1]])
#            elif len(R[x + 1]) == 1 and len(R[x]) == 2:
#               S.append([R[x][0], R[x + 1][0], R[x][0] * R[x + 1][0]])
#                S.append([R[x][1], R[x + 1][0], R[x][1] * R[x * 1][0]])
        if len(R[x]) == 2:
            SPARE.append(R[x])
#        if len(R[x]) == 1:
#            SPARE.append(R[x])
#    print("SPARE: {}".format(SPARE))
    maximum = 0
    temp = 0
#    for x in range(0, len(SPARE), 1):
#        for y in range(0, len(SPARE), 1):
#            if x != y:
#                if len(SPARE[x]) == 1 and len(SPARE[y]) == 2:
##                    print("Multiplying {} by {}".format(SPARE[x][0], SPARE[y][0]))
#                    temp = SPARE[x][0] * SPARE[y][0]
#                    S.append([SPARE[x][0], SPARE[y][0], temp])
##                    print("Multiplying {} by {}".format(SPARE[x][0], SPARE[y][1]))
#                    temp = SPARE[x][0] * SPARE[y][1]
#                    S.append([SPARE[x][0], SPARE[y][1], temp])
##                    print("Multiplying {} by {}".format(SPARE[y][0], SPARE[y][1]))
#                    temp = SPARE[y][0] * SPARE[y][1]
#                    S.append([SPARE[y][0], SPARE[y][1], temp])
#                elif len(SPARE[x]) == 2 and len(SPARE[y]) == 1:
##                    print("Multiplying {} by {}".format(SPARE[x][0], SPARE[y][0]))
#                    temp = SPARE[x][0] * SPARE[y][0]
#                    S.append([SPARE[x][0], SPARE[y][0], temp])
##                    print("Multiplying {} by {}".format(SPARE[x][1], SPARE[y][0]))
#                    temp = SPARE[x][1] * SPARE[y][0]
#                    S.append([SPARE[x][1], SPARE[y][0], temp])
##                    print("Multiplying {} by {}".format(SPARE[x][0], SPARE[x][1]))
#                    temp = SPARE[x][0] * SPARE[x][1]
#                    S.append([SPARE[x][0], SPARE[x][1], temp])
#                    
#    for q in range(0, len(SPARE), 1):
#        for r in range(0, len(SPARE[q]), 1):
#           for s in range(len(SPARE[q]), -1, 1):
#                temp = SPARE[q][r] * SPARE[q][s]
#    for q in range(len(SPARE), 0, -1):
#        for x in range(0, len(SPARE), 1):
#            for y in range(0, len(SPARE[q]), 1):
#                print("SPARE: {}".format(SPARE[q]))
#                    temp = SPARE[q][y] * SPARE[x][z]
#                    print("{} x {} is {}".format(SPARE[q][y], SPARE[x][z], temp))
                    
#            print(SPARE[x], SPARE[y])
    i = 0
    j = 0
    p = 0
    q = 0
    if len(Q) == 0:
        for x in SPARE:
            for y in SPARE:
                for a in x:
                    for b in y:
                        if x.index(a) != y.index(b):
                            if temp > maximum:
                                maximum = i * j
                                p = i
                                q = j
#                            print("The maximum value is currently: {}".format(maximum))
                            temp = a * b
    #                            print("{} x {} is {}".format(a, b, temp))
                            i = a
                            j = b
        return maximum, p, q
#        for x in range(0, len(SPARE), 1):
#            for y in range(0, len(SPARE), 1):
#                if x != y:
#                    for z in range(len(SPARE[x]) - 1):
#                        for t in range(len(SPARE[y]) - 1):
#                            temp = SPARE[x][z] * SPARE[y][t]
#                            print("{} x {} is {}".format(SPARE[x][z], SPARE[x][t], temp))
#   print(P, Q, R, S, SPARE, len(SPARE))

def main():
#    L = list(int(x) for x in range(1, 1 + 5, 1))
#    L = [1, 2, 3, 4, 5, 6, 20, 21, 21, 2]
    L = []
    for x in range(0, 2500, 1):
        L.append(random.randint(0, 2500))
    maximum, lhs, rhs = merge_order(L, [], [], [])
    print("The list: {}\n\n\n\n".format(L))
    print("The maximum pairwise product: {} ({} x {})".format(maximum, lhs, rhs))
    print("Charles Truscott Watters. More efficient, non pointer linked list algorithm")
    print("I love you big bro Tai. Thank you MIT")
if __name__ == "__main__": main()

"""

The list: [1121, 1553, 922, 1691, 1698, 2266, 2038, 1060, 1010, 170, 704, 2236, 1837, 2453, 713, 1644, 370, 1969, 260, 1956, 1478, 30, 1600, 0, 1935, 16, 616, 1005, 1430, 1800, 1406, 1501, 194, 1274, 498, 1763, 1848, 537, 1364, 686, 242, 1013, 931, 1845, 717, 1563, 1656, 1344, 1590, 2094, 1069, 2200, 1814, 638, 1532, 946, 455, 572, 1142, 495, 615, 1461, 1608, 1583, 1971, 690, 512, 2362, 1141, 926, 1962, 2472, 1854, 2438, 697, 2334, 2473, 1033, 2207, 2488, 709, 935, 2266, 1706, 1053, 1245, 1183, 1810, 1875, 1465, 1265, 2399, 745, 1141, 2056, 1072, 678, 1167, 2179, 1817, 1731, 2133, 714, 1929, 1630, 765, 2249, 213, 1233, 163, 961, 1120, 2271, 2288, 1651, 1439, 1301, 924, 405, 155, 775, 1530, 1502, 1292, 1836, 324, 544, 1794, 709, 1772, 2108, 1737, 2372, 1247, 542, 222, 1106, 2058, 366, 1543, 1293, 199, 2255, 1247, 2004, 1119, 232, 5, 2274, 1271, 2409, 2127, 649, 1896, 439, 493, 1841, 1152, 1217, 832, 2029, 160, 755, 1063, 683, 1466, 1820, 2179, 89, 176, 1999, 2487, 1518, 2134, 1296, 723, 1384, 551, 729, 1596, 623, 142, 1948, 786, 2440, 534, 811, 1072, 714, 375, 2220, 775, 2039, 1153, 769, 877, 962, 418, 671, 219, 121, 1630, 1634, 1419, 2118, 2229, 641, 1421, 1102, 155, 1734, 1486, 2115, 1794, 617, 828, 1907, 218, 2331, 1234, 737, 1042, 1348, 266, 982, 602, 2443, 1396, 892, 120, 1925, 704, 1367, 383, 1160, 975, 881, 2045, 168, 1919, 746, 175, 2398, 459, 730, 1598, 621, 2323, 1337, 1818, 949, 1650, 2399, 1527, 825, 2457, 115, 1632, 920, 1809, 501, 880, 867, 391, 949, 1769, 2341, 2350, 2014, 700, 2096, 747, 2019, 1291, 417, 114, 2394, 2486, 2055, 175, 695, 404, 2223, 1697, 1409, 1561, 471, 717, 1606, 1554, 1200, 34, 9, 1547, 497, 1853, 1448, 1258, 751, 1390, 1729, 2233, 2373, 22, 1318, 348, 1761, 1728, 1937, 210, 2479, 606, 2138, 2076, 1326, 556, 164, 2333, 434, 544, 1390, 242, 235, 1646, 1377, 1902, 466, 1553, 2386, 622, 2176, 2115, 1987, 2490, 1776, 1773, 1480, 544, 967, 724, 143, 2043, 2046, 825, 518, 986, 1852, 1305, 1320, 1979, 1298, 2258, 10, 1249, 2113, 678, 867, 1333, 1520, 388, 234, 2033, 976, 1674, 1107, 2194, 530, 771, 1667, 1335, 84, 1858, 2121, 1091, 2174, 528, 2166, 1880, 282, 383, 1059, 1116, 1186, 2038, 183, 1916, 1413, 2099, 521, 2272, 1810, 2011, 778, 2162, 1105, 121, 1189, 2102, 1543, 2410, 24, 164, 762, 1870, 175, 1282, 1699, 834, 2028, 1054, 1976, 1274, 1297, 82, 1968, 1240, 2055, 1311, 1401, 13, 809, 909, 1507, 1923, 854, 2247, 70, 1193, 2242, 2458, 248, 99, 736, 98, 1492, 304, 1360, 2056, 1897, 2422, 435, 690, 636, 1694, 1029, 2119, 1150, 143, 840, 706, 71, 1734, 134, 653, 1671, 682, 1978, 629, 1874, 2415, 99, 1740, 564, 1277, 544, 1447, 52, 2275, 1247, 225, 539, 767, 2020, 2053, 1170, 761, 1740, 2033, 1584, 1974, 1317, 60, 369, 921, 1281, 2327, 1365, 2270, 703, 2432, 2080, 1247, 1694, 1314, 393, 2265, 209, 2391, 986, 44, 953, 1400, 1857, 2405, 653, 1599, 2124, 967, 581, 1902, 1763, 1821, 2223, 922, 1305, 22, 1615, 1904, 455, 668, 1466, 1718, 2232, 1351, 574, 71, 499, 207, 453, 258, 793, 1541, 821, 979, 128, 1194, 422, 407, 2327, 1282, 1237, 709, 2382, 871, 1114, 1256, 1304, 144, 2083, 2314, 2060, 1054, 1340, 1737, 1795, 2338, 1803, 279, 1680, 2089, 2368, 937, 1507, 2088, 2292, 1981, 417, 338, 193, 1610, 2450, 1975, 56, 1442, 1540, 1276, 847, 724, 486, 1607, 454, 554, 1131, 2474, 611, 2466, 872, 21, 1790, 1205, 645, 1098, 415, 2108, 228, 2343, 1135, 1730, 2376, 1399, 738, 871, 743, 1425, 933, 2100, 851, 184, 2263, 2445, 75, 521, 2098, 1378, 176, 2370, 888, 308, 1330, 1783, 748, 591, 2443, 1463, 1071, 588, 1246, 161, 908, 502, 1985, 2338, 2172, 1005, 1346, 2081, 208, 2093, 2351, 216, 1261, 455, 1795, 591, 1529, 2354, 2228, 1022, 539, 257, 2316, 557, 927, 1493, 871, 644, 1195, 1570, 2091, 2231, 1687, 1878, 1514, 1277, 2110, 1192, 1448, 1573, 927, 2163, 1845, 623, 884, 1457, 1133, 1, 604, 361, 1389, 1352, 822, 983, 1039, 2205, 2499, 2012, 175, 2146, 149, 2446, 421, 1798, 1993, 569, 26, 230, 2276, 702, 517, 1185, 1988, 420, 1400, 1395, 68, 181, 91, 303, 1658, 1332, 320, 425, 1417, 821, 744, 1628, 936, 469, 26, 582, 1132, 2480, 1678, 2099, 674, 729, 1261, 691, 1898, 1345, 2487, 469, 2119, 585, 78, 1034, 1249, 676, 1026, 1353, 231, 2358, 1247, 2363, 1330, 1301, 2043, 1847, 1442, 971, 2203, 512, 1983, 205, 1544, 1204, 1262, 1336, 1734, 324, 2470, 2496, 1747, 1887, 1363, 121, 81, 603, 1910, 720, 2244, 596, 117, 1928, 2022, 102, 383, 1635, 172, 2276, 1853, 1469, 2402, 1808, 1397, 74, 2103, 572, 1539, 987, 2088, 2345, 2078, 1477, 2093, 66, 1528, 1550, 1247, 2307, 1443, 1169, 2179, 1799, 533, 1878, 1004, 643, 1678, 2038, 1876, 1178, 775, 1205, 1672, 2136, 1214, 664, 2157, 2156, 76, 2148, 193, 1292, 1384, 2148, 478, 1756, 1288, 451, 1865, 348, 2366, 1454, 613, 1662, 345, 2418, 2035, 985, 1527, 2344, 555, 403, 117, 1060, 1800, 658, 1798, 845, 1167, 704, 918, 1322, 746, 649, 2467, 838, 2357, 1160, 987, 386, 1679, 1008, 1788, 2324, 217, 157, 403, 2009, 51, 653, 1198, 1540, 2139, 734, 2141, 2481, 1703, 1523, 29, 575, 1024, 1931, 1970, 623, 377, 2004, 1194, 928, 4, 783, 1950, 46, 239, 941, 2116, 932, 1738, 1302, 523, 904, 1262, 2288, 1592, 816, 2016, 385, 2435, 1314, 134, 921, 160, 243, 1323, 1013, 1977, 363, 1566, 1965, 1009, 2163, 503, 1436, 2138, 2156, 1414, 2202, 2408, 1800, 1449, 2011, 1947, 526, 2027, 922, 156, 1387, 911, 2422, 2132, 1686, 1477, 254, 2312, 2007, 721, 2168, 18, 2200, 1941, 82, 873, 707, 198, 148, 69, 1208, 7, 253, 606, 2498, 2463, 2204, 2333, 2486, 2054, 3, 2174, 1114, 2038, 243, 1788, 1300, 2500, 410, 2204, 278, 2069, 1247, 417, 567, 996, 224, 2153, 1834, 1602, 2025, 540, 1501, 2258, 1695, 335, 836, 1029, 998, 1331, 816, 1318, 1890, 42, 447, 321, 667, 335, 866, 2049, 609, 1728, 1053, 587, 2329, 1946, 1048, 896, 1871, 1899, 1962, 1602, 1791, 1101, 844, 2210, 225, 901, 857, 2047, 1399, 1943, 2379, 409, 855, 1669, 685, 769, 1246, 1046, 48, 2184, 1265, 496, 572, 2131, 1860, 2012, 2354, 466, 1835, 1356, 2416, 1111, 1204, 1022, 852, 561, 2462, 494, 2398, 1928, 557, 1938, 161, 738, 1167, 1448, 1573, 1012, 2112, 559, 2333, 2040, 2093, 1543, 1176, 1570, 1427, 627, 1166, 1282, 854, 1365, 2089, 1587, 944, 1343, 1994, 2084, 1791, 1371, 1367, 625, 192, 493, 153, 1952, 1064, 2003, 1230, 828, 2189, 2353, 2064, 1745, 98, 1193, 2225, 1046, 6, 995, 1154, 2192, 1602, 483, 671, 1101, 1789, 536, 1157, 1743, 855, 1749, 2042, 1317, 2464, 69, 2148, 2140, 787, 1669, 1210, 1126, 1452, 736, 174, 2096, 1739, 600, 90, 1926, 747, 904, 912, 175, 823, 1666, 1918, 973, 79, 2056, 1263, 373, 1436, 1891, 1578, 1821, 2028, 465, 926, 31, 2150, 1943, 2199, 1785, 338, 472, 1790, 1396, 325, 1524, 884, 2010, 78, 1603, 2082, 1898, 1627, 1039, 1756, 2121, 1888, 2011, 953, 951, 806, 1142, 1651, 1392, 2345, 731, 1619, 1886, 1299, 1088, 2178, 1459, 690, 2409, 732, 1884, 804, 589, 2205, 1734, 811, 567, 1338, 84, 770, 562, 1428, 12, 252, 803, 500, 1638, 1000, 767, 1051, 1704, 397, 1781, 161, 324, 167, 1805, 1834, 881, 1160, 1163, 454, 1705, 1222, 1581, 932, 2313, 7, 1261, 820, 2364, 1858, 966, 589, 454, 2289, 1543, 462, 2345, 2260, 2477, 2119, 945, 2416, 1675, 320, 1917, 316, 56, 1644, 1019, 729, 1590, 2391, 1864, 633, 200, 1822, 1461, 2196, 413, 1813, 722, 1354, 2475, 641, 677, 2397, 631, 85, 633, 874, 1632, 1523, 771, 872, 578, 925, 1384, 2153, 1291, 2467, 1420, 2142, 1577, 1494, 2431, 255, 387, 1177, 1539, 2080, 454, 2362, 689, 2158, 2085, 1296, 1077, 1581, 1190, 460, 2142, 1236, 1443, 1474, 519, 2259, 1390, 1081, 1147, 1992, 2186, 631, 926, 707, 374, 826, 2100, 1528, 243, 538, 1567, 2428, 2453, 7, 504, 1043, 176, 733, 926, 1455, 2004, 2003, 2007, 1268, 1432, 1517, 1384, 2171, 1180, 869, 14, 1466, 18, 1110, 2304, 1164, 863, 880, 1868, 1664, 1703, 930, 930, 469, 2180, 938, 2274, 2499, 1750, 1802, 154, 2066, 2123, 120, 208, 1295, 1644, 1539, 555, 2484, 418, 81, 224, 355, 1608, 1535, 408, 231, 178, 330, 824, 837, 1941, 1776, 11, 2324, 1187, 969, 2479, 1295, 224, 1841, 3, 2107, 2292, 2430, 1872, 1398, 53, 1287, 1353, 1043, 351, 335, 1366, 899, 1426, 719, 307, 2428, 1198, 1988, 261, 1390, 1951, 980, 189, 893, 1919, 1734, 675, 1504, 2268, 2066, 469, 2482, 1078, 370, 1846, 266, 2349, 622, 1452, 2267, 2326, 2413, 170, 1855, 2056, 1189, 62, 69, 1832, 1407, 345, 2332, 2110, 2313, 2284, 723, 1789, 347, 388, 171, 614, 1816, 1955, 2254, 1953, 15, 1785, 921, 1096, 2283, 36, 2423, 1648, 1075, 669, 967, 678, 522, 813, 2363, 670, 2268, 2104, 1243, 1121, 600, 2498, 1551, 2179, 724, 435, 1189, 1251, 1399, 1755, 680, 1604, 1475, 1543, 1283, 584, 1444, 498, 677, 1815, 80, 1903, 641, 1611, 1460, 676, 1052, 2189, 2154, 1588, 2175, 1452, 2467, 2134, 816, 68, 1555, 995, 2268, 2198, 151, 270, 2043, 856, 755, 1989, 2317, 487, 248, 2204, 1781, 781, 2156, 1666, 2143, 1753, 906, 597, 1529, 1425, 1030, 1694, 2308, 379, 1230, 201, 1702, 1726, 1455, 42, 767, 1271, 448, 678, 824, 1418, 739, 1301, 1616, 1530, 886, 529, 2139, 430, 2326, 564, 1938, 1590, 1705, 1343, 99, 2367, 2200, 66, 2395, 663, 2092, 858, 2003, 1630, 2205, 1015, 1418, 599, 1832, 459, 922, 1876, 1800, 1159, 1794, 877, 20, 1090, 2009, 1088, 1645, 1153, 2430, 227, 623, 1453, 2078, 828, 293, 2236, 495, 1634, 1795, 1919, 949, 1701, 1507, 553, 779, 2380, 2303, 891, 1391, 1328, 1203, 1050, 1065, 1964, 1387, 535, 173, 900, 2477, 2418, 369, 2064, 1579, 1667, 1541, 1499, 203, 2319, 2363, 1318, 1666, 1845, 471, 2098, 616, 2048, 833, 1321, 1436, 1079, 1640, 203, 2101, 57, 1733, 2275, 1010, 1058, 2476, 516, 451, 1677, 1033, 41, 591, 1352, 347, 1903, 268, 1016, 1426, 2107, 1821, 2276, 1689, 1449, 1049, 2243, 1272, 642, 1848, 44, 896, 1067, 199, 2058, 1864, 1215, 2108, 121, 2263, 2183, 893, 1145, 402, 907, 2475, 1883, 1726, 2120, 690, 716, 364, 1368, 11, 1205, 1173, 2143, 740, 2464, 2114, 1673, 458, 2087, 1632, 2242, 849, 1424, 96, 998, 856, 1368, 762, 1705, 1005, 1094, 1641, 1909, 1177, 1046, 1875, 462, 893, 1941, 1590, 1655, 1377, 251, 952, 916, 1477, 441, 1639, 227, 1742, 1548, 1991, 1170, 1909, 814, 1745, 1540, 2370, 2226, 1457, 449, 591, 1886, 1763, 487, 38, 1660, 846, 1897, 1792, 99, 1331, 24, 1996, 681, 1476, 1284, 1697, 1189, 1259, 1658, 1118, 2449, 1073, 2481, 1303, 2256, 121, 1027, 1942, 1643, 2328, 1912, 1706, 10, 317, 2331, 2475, 1284, 1834, 1627, 1539, 1111, 2118, 1645, 1330, 158, 634, 1703, 285, 818, 1336, 776, 2100, 552, 788, 398, 705, 339, 1164, 2044, 207, 2340, 280, 2026, 257, 1053, 403, 1698, 388, 1977, 524, 1178, 2019, 1199, 2394, 494, 1078, 1251, 962, 1689, 2167, 2265, 2108, 2439, 1683, 255, 1730, 713, 780, 1500, 118, 1850, 2315, 2274, 1310, 274, 2454, 1829, 2407, 1312, 1197, 1709, 1959, 2124, 2258, 1328, 465, 1125, 1290, 2181, 38, 610, 1813, 1975, 1771, 2341, 1215, 1926, 2245, 1082, 222, 985, 1351, 2027, 2065, 458, 874, 1399, 2091, 68, 1870, 602, 469, 2054, 834, 1483, 741, 2243, 1696, 2295, 207, 2113, 2350, 1772, 2460, 1343, 338, 920, 450, 985, 2320, 1398, 231, 1881, 1507, 63, 526, 2071, 2093, 867, 53, 1444, 1197, 388, 1357, 740, 92, 720, 552, 776, 921, 976, 1227, 753, 173, 1317, 610, 1395, 1535, 1395, 2408, 576, 1792, 369, 1310, 2083, 2067, 1270, 259, 1796, 120, 66, 2418, 1605, 124, 614, 2130, 1417, 1467, 1505, 114, 360, 2301, 1454, 472, 1386, 1899, 754, 1807, 553, 29, 499, 1907, 1074, 1275, 1538, 190, 1253, 2313, 381, 1318, 1941, 2104, 1202, 1013, 330, 1289, 616, 1829, 1914, 1781, 1992, 602, 1644, 540, 1064, 581, 944, 135, 2185, 325, 998, 32, 340, 63, 1818, 1795, 2075, 1661, 2337, 1766, 80, 832, 1850, 2417, 114, 2238, 1141, 353, 1619, 502, 195, 512, 2111, 2018, 1536, 2022, 1513, 313, 833, 2427, 2207, 2500, 2409, 2366, 2063, 254, 1351, 1106, 1128, 2268, 784, 259, 1382, 200, 69, 236, 734, 2230, 950, 2071, 2013, 2266, 1968, 1818, 819, 2251, 451, 1620, 2027, 2418, 1248, 2450, 1649, 1105, 458, 1740, 546, 489, 2329, 1292, 422, 920, 745, 426, 2256, 31, 966, 1846, 2037, 1972, 612, 2267, 1021, 2364, 1266, 1726, 1830, 1400, 967, 2127, 1634, 965, 2082, 806, 1455, 610, 173, 193, 2107, 2004, 2233, 779, 180, 1950, 20, 1565, 287, 239, 1712, 71, 368, 1586, 32, 44, 514, 2158, 1228, 2225, 1478, 2210, 1327, 40, 2486, 300, 902, 850, 250, 1084, 988, 201, 1273, 2044, 1389, 215, 759, 1342, 904, 837, 1896, 1637, 1150, 1266, 1062, 1599, 755, 810, 1658, 1524, 1558, 609, 2222, 1922, 1341, 2222, 1957, 2250, 549, 544, 1766, 301, 1047, 368, 1201, 1692, 1467, 315, 1014, 1257, 464, 290, 2109, 509, 871, 1201, 1178, 163, 1899, 2437, 2340, 2182, 737, 1657, 1414, 468, 225, 1203, 2335, 846, 814, 2359, 409, 1273, 2316, 683, 1037, 709, 133, 2180, 1704, 2408, 2431, 966, 177, 314, 1832, 2257, 1071, 1468, 460, 572, 2014, 1891, 594, 2172, 2389, 2043, 242, 480, 922, 1344, 1609, 1905, 161, 2144, 1291, 874, 1408, 270, 1087, 2378, 1171, 957, 1847, 1471, 189, 961, 2402, 1090, 1949, 931, 1087, 1433, 562, 2242, 1291, 395, 1460, 901, 208, 2131, 2303, 2185, 2302, 644, 571, 549, 898, 2147, 1686, 2215, 123, 2499, 313, 848, 1539, 1884, 644, 995, 622, 1664, 68, 1689, 2110, 2312, 2249, 2080, 744, 1810, 1384, 1131, 1263, 853, 644, 1817, 1572, 1955, 1312, 1181, 901, 2428, 1457, 269, 259, 1157, 1379, 390, 560, 2014, 2281, 501, 562, 2147, 22, 1135, 1879, 2240, 116, 973, 1517, 688, 2190, 1207, 717, 1605, 1364, 389, 2043, 1578, 2239, 8, 1433, 950, 221, 983, 2483, 407, 49, 1897, 1217, 2411, 1834, 2147, 708, 2374, 1345, 1708, 2222, 2438, 655, 362, 1372, 1800, 1354, 181, 865, 437, 1299, 2309, 1681, 2032, 1357, 2452, 1575, 2458, 1855, 924, 1304, 1265, 2081, 884, 973, 1910, 1751, 487, 1559, 146, 2103, 549, 2386, 568, 643, 1164, 1358, 2352, 2019, 1732, 2433, 1474, 2092, 1417, 2102, 2286, 1175, 1805, 708, 991, 1169, 1810, 100, 989, 2432, 1153, 1772, 1957, 143, 769, 1209, 943, 1244, 168, 212, 2004, 2027, 1298, 587, 1393, 407, 22, 626, 1971, 1481, 643, 650, 1738, 1425, 326, 1491, 794, 981, 861, 55, 2210, 206, 2170, 542, 773, 1814, 1071, 50, 777, 648, 2300, 2053, 1417, 2404, 1050, 2368, 2464, 94, 2095, 986, 1444, 700, 1392, 2338, 56, 2255, 356, 2222, 2239, 1433, 18, 1886, 2303, 1415, 1445, 1618, 499, 350, 102, 876, 1117, 127, 2276, 482, 631, 1379, 2469, 2322, 844, 840, 427, 764, 707, 1888, 2441, 134, 2375, 2459, 325, 496, 317, 2045, 1672, 1420, 1650, 1179, 1620, 1142, 957, 339, 480, 1862, 240]




The maximum pairwise product: 6247500 (2499 x 2500)
Charles Truscott Watters. More efficient, non pointer linked list algorithm
I love you big bro Tai. Thank you MIT

[Program finished]

CAT S60 with thermal camera on Google Android and Pydroid

"""