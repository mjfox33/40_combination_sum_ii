class Solution:
    def combinationSum2(self, candidates: list[int], target: int) -> list[list[int]]:
        #candidates.sort() # just to ensure they are in order
        result = []
        candidates.sort()

        def combination(current_index, current_path, current_sum):
            if current_sum > target:
                return
            
            if target==current_sum:
                result.append(current_path)
                return
            
            for i in range(current_index, len(candidates)):
                if i > current_index and candidates[i] == candidates[i-1]:
                    continue
                combination(i+1, current_path+[candidates[i]], current_sum+candidates[i])
                
        combination(0,[],0)
        return result