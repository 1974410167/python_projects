pushed = [1,2,3,4,5]
popped = [4,5,3,2,1]


class Solution:
    def validateStackSequences(self, pushed, popped):

        if not pushed:
            return True

        l = len(pushed)
        push1 = []

        for i in range(l):
            if pushed[i] != popped[0]:
                push1.append(pushed[i])
            else:
                popped.pop(0)

        if popped:
            for j in range(len(popped)):
                if pushed[j] == push1[-1]:
                    push1.pop()


        if push1:
            return False
        return True

s = Solution()
a = s.validateStackSequences(pushed,popped)
print(a)