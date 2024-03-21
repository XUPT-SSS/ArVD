import pandas as pd
import re
from clead_gadget import  clean_gadget
import time

def normalization(source):
    nor_code = []
    for fun in source['sentence']:
        fun =str(fun)
        lines = fun.split('\n')
        # #print(lines)
        #
        code = ''
        for line in lines:
            line = line.strip()
            code += line + ' '
        code = clean_gadget([code])
        nor_code.append(code[0])
        print(code[0])
    return nor_code


def mutrvd(input,output):

    train = pd.read_csv(input)
    #train=train.iloc[69]
    train['sentence'] = normalization(train)
    train.to_csv(output,index=False)

def add_index(input,output):
    df = pd.read_csv(input)
    df.index = df.index + 0
    df.to_csv(output, index=True,index_label='idx')


if __name__ == '__main__':

    mutrvd('/home/yons/person/zc/ArVD/model/xsbt_process/data/d2a_lbv1_function_dev.csv','/home/yons/person/zc/ArVD/model/xsbt_process/data/train_norm.csv')
    #  add index for datasets  ,waring : train 、valid 、test  (index is not same)
    add_index(r'/home/yons/person/zc/ArVD/model/xsbt_process/data/train_norm.csv', r'/home/yons/person/zc/ArVD/model/xsbt_process/data/train_index.csv')

