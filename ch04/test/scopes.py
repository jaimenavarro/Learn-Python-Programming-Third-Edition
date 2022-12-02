def outer_scope():
    test = 1

    def inner_scope():
        global test
        test = 2
        print("inner: ", test)

    inner_scope()
    print("outer", test)


test = 0
outer_scope()
print("global", test)

