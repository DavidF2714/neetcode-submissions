class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            res.append(str(len(s)))
            res.append('#')
            res.append(s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        dec = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j+=1
            _len = int(s[i:j])
            i = j+1
            j = i + _len
            dec.append(s[i:j])
            i = j
        
        return dec
