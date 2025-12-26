class Solution:
    def two_sum(self,nums,target):
        diction={}
        for i in range(len(nums)):
            compl=target-nums[i]
            if compl in diction:
                return [diction[compl],i]
            diction[nums[i]]=i

def main():
    nums=[2,4,6,1,10,14,11,7]
    obj=Solution()
    result=obj.two_sum(nums,12)
    print("Result",result)

if __name__=="__main__":
    main()