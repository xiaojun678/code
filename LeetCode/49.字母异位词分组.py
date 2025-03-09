class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d = {}
        for str in strs:
            temp = ''.join(sorted(str))
            if temp not in d:
                d[temp] = []
            d[temp].append(str)
        t = []
        for key in d.keys():
            t.append(d[key])
        return t

s = Solution()

strs = ["eat","tea","tan","ate","nat","bat"]

print(s.groupAnagrams(strs))

"""
数组
哈希表
字符串
排序

改进：
核心思想：由于互为字母异位词的两个字符串包含的字母相同，因此两个字符串中的相同字母出现的次数一定是相同的，
故可以将每个字母出现的次数使用字符串表示，作为哈希表的键。

然后对于每个字符串，键相同的则为字母异位词

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)

        for st in strs:
            counts = [0] * 26
            for ch in st:
                counts[ord(ch) - ord("a")] += 1
            # 需要将 list 转换成 tuple 才能进行哈希
            mp[tuple(counts)].append(st)
        
        return list(mp.values())

作者：力扣官方题解
链接：https://leetcode.cn/problems/group-anagrams/solutions/520469/zi-mu-yi-wei-ci-fen-zu-by-leetcode-solut-gyoc/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
"""
