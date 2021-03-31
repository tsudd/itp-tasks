from collections import defaultdict

class recursivedict():

    def __init__(self):
        self._value = None
        
    def __getitem__(self, key):
        if self._value is None:
            self._value = defaultdict(recursivedict)
        return self._value[key]
    
    def __setitem__(self, key, value):
        if self._value is None:
            self._value = defaultdict(recursivedict)
        self._value[key] = value
    
    def __str__(self):
        if self._value is None:
            return "{}"
        ans = ""
        for (key, value) in self._value.items():
            if (len(ans) > 0):
                ans += ", "
            ans += f"'{key}': {value}"
        ans = "{" + ans + "}"
        return ans


def solve():

    test = recursivedict()
    print('type(test) =', type(test))

    print('test[0] =', test[0])

    test["a"] = 1
    print('test["a"] =', test["a"])

    test["b"][13] = 42
    test["b"][0.123] = "whattheduck"
    test["b"][0.123] = "ahokay"
    test["b"][1.0][0] = "ohwow"

    print('test =', test)

#solve()