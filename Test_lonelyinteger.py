import pytest
from lonelyinteger import *


@pytest.mark.parametrize(arr,[3],indirect=True)
def test_lonelyint(arr,arr1):
    integer1.lonelyint(arr,n)
    assert arr==arr1






