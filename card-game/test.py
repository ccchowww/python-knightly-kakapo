code = 'attackvar = "a" +"b" + "c"'
exec(code)
# Global scope
xd = 1

def funcScope():
    # global xd     # global to refer to variables in global scope
    xd = 5
    xxx = 20
    xxy = 100
    def nestedFunctionScope():
        nonlocal xd     # nonlocal to refer to variables from scope directly above current scope
        nonlocal xxy # chain nonlocal declaration
        xd = 10
        xxx = 30    # reassign without nonlocal declaration, no change above
        def superNestedFunctionScope():
            nonlocal xxx    # this changes xxx in nestedFunctionScope, but not in funcScope.
            nonlocal xxy    # can chain nonlocal declarations to go up further than one scope.
            global xd
            xxx = 50
            xxy = 200
            xd = 420 # can change global from any deeper place

        superNestedFunctionScope()
        print(xxx, "xxx nestedFuncScope")
        print(xd, "xd nestedFuncScope")

    nestedFunctionScope()
    print(xxx, "xxx funcScope")
    print(xd, "xd funcScope")
    print(xxy, "xxy funcScope")

funcScope()
print(xd, "xd global")

#this is deep