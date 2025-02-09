import pytest


class TestNew_demo:

    @pytest.mark.dependency(depends=["add_product"])
    def test_01_piyush(self):
        print("hello piyush")

    @pytest.mark.dependency(name="add_product")
    def test_02_akash(self):
        print("hello akash")