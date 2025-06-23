class Solution:
    def reverseStr(self, s: str, k: int) -> str:

        # chunks = [s[i:i+k] for i in range(0, len(s), k)]
        # op = []
        # for i, chunk in enumerate(chunks):
        #     if i%2 == 0:
        #         chunk = chunk[::-1]
        #     op.append(chunk)
        # # print(op)
        # return "".join(op)
            s = list(s)
            for i in range(0, len(s), 2 * k):
                s[i:i + k] = reversed(s[i:i + k])
            return "".join(s)

        