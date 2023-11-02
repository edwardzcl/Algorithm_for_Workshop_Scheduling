
import os
import sys
import numpy as np
import random
 
#需要解决的问题
#传入的path为当前文档所在路径之后的拼接路径
def Get_Problem(path):
    if os.path.exists(path):
        #提取txt文件中的数据
        with open(path,'r') as data:
            List=data.readlines()
            # print(List)
            P=[]
            for line in List:
                list_ = []
                for j in range(len(line)):
                    try:
                        if line[j].isdigit() and line[j + 1].isdigit():
                            list_.append(int(line[j]) * 10 + int(line[j + 1]))
                            k = line[j]
                        if line[j - 1].isdigit() and line[j].isdigit() and j != 0:
                            pass
 
                        elif line[j].isdigit() :
                            if line[j +1].isspace() and j+1<len(line):
                                list_.append(int(line[j]))
                    except Exception as e:
                        print('可能出错，记得检查',e)
                        pass
                P.append(list_)
            for k in P:
                    if k==[]:
                        P.remove(k)
            #将提取到的数据转化为具体的FJSP问题
            J_number=P[0][0]   #工件数
            M_number=P[0][1]   #机器数
 
            Problem=[]
            for J_num in range(1,len(P)):
                O_num=P[J_num][0] #工件的工序数
                for Oij in range(O_num):
                    O_j = []
                    next=1
                    while next<len(P[J_num]):
                        M_Oj=[0 for Oji in range(M_number) ]
                        M_able = P[J_num][next]  # 加工第一道工序的可选机器数
                        able_set=P[J_num][next+1:next+1+M_able*2]
                        next=next+1+M_able*2
                        for i_able in range(0,len(able_set),2):
                            M_Oj[able_set[i_able]-1]=able_set[i_able+1]
                        O_j.append(M_Oj)
                Problem.append(O_j)
            for i_1 in range(len(Problem)):
                for j_1 in range(len(Problem[i_1])):
                    for k_1 in range(len(Problem[i_1][j_1])):
                        if Problem[i_1][j_1][k_1]==0:
                            Problem[i_1][j_1][k_1]=9999
            # Max_len = []
            # for i_p in range(len(Problem)):
            #     Max_len.append(len(Problem[i_p]))
            # Max_Operation_len=max(Max_len)
            # for i_l in range(len(Problem)):
            #     if len(Problem[i_l])<Max_Operation_len:
            #         M_ky=[0 for Oji in range(M_number)]
            #         Problem_fake=Problem[i_l]
            #         Problem_fake.append(M_ky)
            #         Problem[i_l]=Problem_fake
            # Problem=np.array(Problem)
            # print(Problem)
    else:
        print('路径有问题')
    return Problem ,J_number,M_number
 
 
Processing_time,J_num,M_num=Get_Problem('/data/zcl/project/aps/FJSP_example/Monaldo/Fjsp/Job_Data/Brandimarte_Data/Text/Mk01.fjs')
print("Processing completed !!!")