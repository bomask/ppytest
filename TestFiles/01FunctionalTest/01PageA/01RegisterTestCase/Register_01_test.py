import sys
sys.path.append('F:\\ppytestNew\\SourceFiles\\Task\\publicTask')

from PublicTask import PublicTask
import pytest
import time


def setup_module():
    print("111111111111111111111")


def test_a_smoke():
    x = PublicTask()
    time.sleep(2)
    print("hello!")
    x = PublicTask()
    x.openBrowser("http://www.baidu.com")
