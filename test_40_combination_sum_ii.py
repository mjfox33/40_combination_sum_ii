from code_40_combination_sum_ii import Solution

def test_example_1():
    s = Solution()
    candidates = [1,1]
    target = 2
    output = [[1,1]]
    assert s.combinationSum2(candidates, target) == output

def test_example_2():
    s = Solution()
    candidates = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
    target = 27
    output = []
    assert s.combinationSum2(candidates, target) == output