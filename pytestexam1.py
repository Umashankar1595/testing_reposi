class TestClass:
    def test1(self):
        x = "this"
        assert "h" in x

    def test2(self):
        x = "hello"
        #The hasattr() function returns True if the specified object has the specified attribute, otherwise False.
        assert hasattr(x, "check")
