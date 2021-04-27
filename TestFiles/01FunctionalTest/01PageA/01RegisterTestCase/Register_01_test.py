import time
import pytest
from SourceFiles.Task.publicTask.PublicTask import PublicTask


def test_a_smoke():
    x = PublicTask()
    time.sleep(2)
    print("hello!")
    x.openBrowser("https://www.baidu.com")
