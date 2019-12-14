# -*- coding: utf-8 -*-
__author__ = "chenk"

class OrthogonalArray:
    def __init__(self, col=[], factor={}, split="|"):
        """cols 表示要保留的正交表列，从第一行开始计算；
            factor 表示每个因素的值，根据key的大小确认因子顺序"""
        self.factor = factor
        self.col = []
        for c in col:
            self.col.append(int(c.strip()))
        self.mapping_arr = []
        self.split = split

    def transfer(self, arr):
        """转化正交表的0,1,2...值 为 真实值"""
        arrs = []
        for a in arr:
            tmp = ""
            for i, v in enumerate(a):
                tmp += self.factor.get(str(i))[int(v)] + self.split
            arrs.append(tmp[:-len(self.split)])

        return self.__transfer(arrs)

    def __transfer(self, arr):
        """处理混合正交表中，拆分 合并处理法 中的值
        arr = ['0|0', 'q|1', 'J|6,7,S,X']
        """
        self.mapping_arr
        for each in arr:
            if "," in each:
                for each_split in self.combine(values=each):
                    self.mapping_arr.append(each_split[:-len(self.split)])
            else:
                self.mapping_arr.append(each)

        return self.mapping_arr

    def combine(self, values="J|6,7,S,X|a,b,c"):
        """处理正交结果中， 合并多个值的情况； 将多个合并值，拆分；"""
        combine_list = []
        for value in values.split(self.split):
            if "," in value:
                combine_list = self.__combine(combine_list, value)
            else:
                if not combine_list:
                    combine_list.append(value + self.split)
                else:
                    combine_list_tmp = combine_list
                    combine_list = []
                    for combine_str in combine_list_tmp:
                        combine_list.append(combine_str + self.split)
        return combine_list

    def __combine(self, combine_str_list, values="6,7,S,X"):
        """处理正交结果中， 合并多个值的情况； 将多个合并值，拆分；
        Return a list.
        """
        combine_str_list_dealed = []
        for each_value in values.split(","):
            for combine_str in combine_str_list:
                combine_str_list_dealed.append(combine_str + each_value + self.split)
        return combine_str_list_dealed

    def delete_array(self, arr):
        """删除正交表不需要用到的列的数据"""
        a = []
        for each in arr:
            tmp = ""
            for i in self.col:
                tmp += each[i-1:i]
            a.append(tmp)
        return a

    def read_array(self):
        """读取正交表， 并以列表返回"""
        a = []
        with open(file="conf/array", mode="r", encoding="utf-8") as f:
            tmp = f.readlines()
        for each in tmp:
            a.append(each.replace("\n", ""))
        return a

    def get_mapping_arr(self):
        return self.mapping_arr

def get_insert_sql(arr=None):
    if not arr:
        return
    template = """(cusid,cusid,stkcode,round(RAND()*1234,2),round(RAND()*1234,2),round(RAND()*1234,2),round(RAND()*1234,2),round(RAND()*1234,2),'{0}',money_type,'{1}'),"""
    for each in arr:
        print(template.format(each[0], each[1]))


if __name__ == "__main__":
    cols = [9, 10]
    factors = {0: ['0', 'q', 'R', 'J', 'W', 'f'], 1: ["0", "1", "2", "3", "5", "6,7,S,X"]}
    orthogonal_array = OrthogonalArray(col=cols, factor=factors)
    orthogonal_array.transfer(orthogonal_array.delete_array(orthogonal_array.read_array()))
    for each in orthogonal_array.get_mapping_arr():
        print(each.replace(orthogonal_array.split, "\t"))

    # print(orthogonal_array.combine(values="J|6,7,S,X|a,b,c"))