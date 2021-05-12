# -*- coding: utf-8 -*-
"""
Created on Wed May 12 10:16:11 2021

@author: quann
"""

#import thư viện
import pandas as pd
import math
import numpy as np
from scipy import stats
import xlrd
#Hàm kiểm tra tính phân phối chuẩn dùng Kolmogorov từ X1-X4
def Kolmogorov(data):
    print("Kiểm định Kolmogorov -", data.name)
    k, p = stats.kstest(rvs=data, cdf='norm', args=(np.mean(data), np.std(data)))
    if p > 0.05:
        print("Dữ liệu tuân theo luật phân phối chuẩn")
    else:
        print("Dữ liệu không tuân theo luật phân phối chuẩn")
    print("------------------------------")
    
#Dùng Shapiro từ X1-X5
def Shapiro(data):
    print("Kiểm định Shapiro -", data.name)
    stat, pvalue = stats.shapiro(data)
    if pvalue > 0.05:
        print("Dữ liệu tuân theo luật phân phối chuẩn")
    else:
        print("Dữ liệu không tuân theo luật phân phối chuẩn")
    print("------------------------------")
#Hàm kiểm tra tính đồng nhất về phương sai dùng Bartlett từ X1-X4
def bartlett(a, b, c, d): 
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Kiểm định Bartlett:")
    stat, pvalue = stats.bartlett(a, b, c, d)
    print("Statistic =", stat, "\n",
          "p value =", pvalue)
    if pvalue > 0.05:
        print("Các features đồng nhất về phương sai")
    else:
        print("Các features không đồng nhất về phương sai")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

    
#Dùng Levene từ X1-X5
def levene(a, b, c, d, e):
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("Kiểm định Levene:")
    stat, pvalue = stats.levene(a, b, c, d, e)
    if pvalue > 0.05:
        print("Các features đồng nhất về phương sai")
    else:
        print("Các features không đồng nhất về phương sai")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#Hàm kiểm định ANOVA từ X1-X4
def anova14(a, b, c, d):
    print("Kiểm định ANOVA:")
    stat, pvalue = stats.f_oneway(a, b, c, d)
    print("Stat =", stat, "\n", "p value =", pvalue)
    if pvalue < 0.05:
        print("Có bằng chứng để bác bỏ giả thuyết H0")
    else:
        print("Chưa có bằng chứng để bác bỏ giả thuyết H0")

        
#Hàm kiểm định ANOVA từ X1-X5
def anova15(a, b, c, d, e):
    print("Kiểm định ANOVA:")
    stat, pvalue = stats.f_oneway(a, b, c, d, e)
    print("Stat =", stat, "\n", "p value =", pvalue)
    if pvalue < 0.05:
        print("Có bằng chứng để bác bỏ giả thuyết H0")
    else:
        print("Chưa có bằng chứng để bác bỏ giả thuyết H0")
        
        


#Câu 1: Độ sâu khai quật và khảo cổ học
#Bốn địa điểm khai quật khác nhau tại một khu vực khảo cổ ở New Mexico đã đưa ra những độ sâu sau (cm) cho những khám phá khảo cổ quan trọng.
#X1 = độ sâu tại Địa điểm I
#X2 = độ sâu tại Vị trí II
#X3 = độ sâu tại Vị trí III
#X4 = độ sâu tại Vị trí IV
df1 = pd.read_excel("C:\\Users\\quann\\owan01-1.xls")
x1_1 = df1['X1']
x1_2 = df1['X2']
x1_3 = df1['X3']
x1_4 = df1['X4']

#kiểm tra tính phân phối chuẩn
print(Kolmogorov(x1_1))
print(Kolmogorov(x1_2))
print(Kolmogorov(x1_3))
print(Kolmogorov(x1_4))

#kiểm tra tính đồng nhất về phương sai
print(bartlett(x1_1, x1_2, x1_3, x1_4))

#kiểm định ANOVA

print(anova14(x1_1, x1_2, x1_3, x1_4))




#Câu 2: Độ sâu Khai quật và Khảo cổ Bốn địa điểm khai quật khác nhau tại một khu vực khảo cổ ở New Mexico đã đưa ra những độ sâu sau (cm) cho những khám phá khảo cổ quan trọng.
#X1 = độ sâu tại Địa điểm I
#X2 = độ sâu tại Vị trí II
#X3 = độ sâu tại Vị trí III
#X4 = độ sâu tại Vị trí IV
df2 = pd.read_excel("C:\\Users\\quann\\owan02.xls")
print(df2)
x2_1 = df2['X1']
x2_2 = df2['X2']
x2_3 = df2['X3']
x2_4 = df2['X4']

#kiểm tra tính phân phối chuẩn
print(Kolmogorov(x1_1))
print(Kolmogorov(x1_2))
print(Kolmogorov(x1_3))
print(Kolmogorov(x1_4))

#kiểm tra tính đồng nhất về phương sai
print(bartlett(x1_1, x1_2, x1_3, x1_4))

#kiểm định ANOVA

print(anova14(x1_1, x1_2, x1_3, x1_4))




#Câu 3: Thuốc nhuộm đỏ Số 40 S.W. Laagakos và F. Mosteller của Đại học Harvard cho chuột ăn các liều thuốc nhuộm đỏ số 40 khác nhau và ghi lại thời gian chết trong nhiều tuần. Kết quả đối với chuột cái, liều lượng và thời gian chết được hiển thị trong dữ liệu
#X1 = thời gian chết cho nhóm kiểm soát
#X2 = thời gian tử vong của nhóm sử dụng liều lượng thấp
#X3 = thời gian tử vong của nhóm sử dụng liều lượng trung bình
#X4 = thời gian tử vong của nhóm dùng liều cao
df3 = pd.read_excel("C:\\Users\\quann\\owan03.xls")
print(df3)
x3_1 = df3['X1']
x3_2 = df3['X2']
x3_3 = df3['X3']
x3_4 = df3['X4']

#kiểm tra tính phân phối chuẩn
print(Kolmogorov(x3_1))
print(Kolmogorov(x3_2))
print(Kolmogorov(x3_3))
print(Kolmogorov(x3_4))

#kiểm tra tính đồng nhất về phương sai
print(bartlett(x3_1, x3_2, x3_3, x3_4))

#kiểm định ANOVA

print(anova14(x3_1, x3_2, x3_3, x3_4))




#Câu 4: Chi phí Khởi sự Kinh doanh Dữ liệu sau thể hiện chi phí khởi động kinh doanh (hàng nghìn đô la) cho các cửa hàng.
#X1 = chi phí khởi động cho bánh pizza
#X2 = chi phí khởi động cho thợ làm bánh / bánh rán
#X3 = chi phí khởi động cho các cửa hàng giày
#X4 = chi phí khởi động cho các cửa hàng quà tặng
#X5 = chi phí khởi động cho các cửa hàng thú cưng
df4 = pd.read_excel("C:\\Users\\quann\\owan04.xls")
print(df4)
x4_1 = df4['X1']
x4_2 = df4['X2']
x4_3 = df4['X3']
x4_4 = df4['X4']
x4_5 = df4['X5']

#kiểm tra tính phân phối chuẩn
print(Shapiro(x4_1))
print(Shapiro(x4_2))
print(Shapiro(x4_3))
print(Shapiro(x4_4))
print(Shapiro(x4_5))

#kiểm tra tính đồng nhất về phương sai
print(levene(x4_1, x4_2, x4_3, x4_4, x4_5))

#kiểm định ANOVA

print(anova15(x4_1, x4_2, x4_3, x4_4, x4_5))




#Câu 5: Cân nặng của các cầu thủ bóng đá Dữ liệu sau đây đại diện cho trọng lượng (pound) của một mẫu ngẫu nhiên các cầu thủ bóng đá chuyên nghiệp trong các đội sau đây.
#X1 = trọng số của người chơi cho Dallas Cowboys
#X2 = trọng lượng của người chơi cho Green Bay Packers
#X3 = trọng số của người chơi cho Denver Broncos
#X4 = trọng lượng của người chơi cho Miami Dolphins
#X5 = trọng lượng của các cầu thủ cho San Francisco Forty Niners
df5 = pd.read_excel("C:\\Users\\quann\\owan05.xls")
print(df5)
x5_1 = df5['X1']
x5_2 = df5['X2']
x5_3 = df5['X3']
x5_4 = df5['X4']
x5_5 = df5['X5']

#kiểm tra tính phân phối chuẩn
print(Shapiro(x5_1))
print(Shapiro(x5_2))
print(Shapiro(x5_3))
print(Shapiro(x5_4))
print(Shapiro(x5_5))

#kiểm tra tính đồng nhất về phương sai
print(levene(x5_1, x5_2, x5_3, x5_4, x5_5))

#kiểm định ANOVA

print(anova15(x5_1, x5_2, x5_3, x5_4, x5_5))