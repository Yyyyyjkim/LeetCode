import re

class Solution:
    def calPoints(self, ops: List[str]) -> int:
        num_list = []
        for i,word in enumerate(ops):
          if re.match("-*\d+",word):
            num_list.append(int(word))
          elif word=="C":
            num_list = num_list[:(len(num_list)-1)]
          elif word=="D":
            num_list.append(num_list[len(num_list)-1]*2)
          elif word=="+":
            num_list.append(sum(num_list[(len(num_list)-2):]))
        return sum(num_list)

ops = ["5","2","C","D","+"]
ops = ["5","-2","4","C","D","9","+","+"]