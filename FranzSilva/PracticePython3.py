class PythonTree:
    def repalce(self, s, old, new):
        return s.replace(old, new)

    def count_concurrency(self, word):
        words = word.lower().replace(" ","")
        count = {}
        for s in words:
            if s in count:
                count[s] += 1
            else:
                count[s] = 1
        return sorted(count.items())
