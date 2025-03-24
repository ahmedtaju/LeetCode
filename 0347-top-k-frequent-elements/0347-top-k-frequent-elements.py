class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap={}
        l=[]
        for i in nums:
            if i in hashMap:
                hashMap[i]+=1
            else:
                hashMap[i]=1
        sorted_items = sorted(hashMap.items(), key=lambda item: item[1], reverse=True)
        top_k_elements = dict(sorted_items[:k])

        return (top_k_elements.keys())
        
        