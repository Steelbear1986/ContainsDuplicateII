class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        p={}
        for i, nums[i]  in enumerate(nums):
           p[i]=nums[i]
        p={k: v for k, v in sorted(p.items(), key=lambda item: item[1])}
        key=[]
        val=[]
        for m,v in p.items():
            if v in val  or len(val)==0:
                    val.append(v)
                    key.append(m)
            if v not in val :
                    val=[]
                    key=[]
                    val.append(v)
                    key.append(m)
            if len(val)==2:
                        if (abs(key[0]-key[1])>k):
                                key.pop(0)
                                val.pop(0)
                        elif len(val)==2 :
                                return  (abs(key[0] - key[1]) <= k)
        return False

