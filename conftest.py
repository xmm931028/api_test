import time
import pytest
from _pytest import terminal


def pytest_terminal_summary(terminalreporter, exitstatus, config):
    '''收集测试结果'''
    total = terminalreporter._numcollected
    passed= len([i for i in terminalreporter.stats.get('passed', []) if i.when != 'teardown'])
    failed=len([i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown'])
    error=len([i for i in terminalreporter.stats.get('error', []) if i.when != 'teardown'])
    skipped=len([i for i in terminalreporter.stats.get('skipped', []) if i.when != 'teardown'])
    successful = len(terminalreporter.stats.get('passed', []))/terminalreporter._numcollected*100
    # terminalreporter._sessionstarttime 会话开始时间
    duration = time.time() - terminalreporter._sessionstarttime
    fail_case_message = [i for i in terminalreporter.stats.get('failed', []) if i.when != 'teardown']
    # print('total times: %.2f' % duration, 'seconds')

    with open("result.txt", "w") as fp:
        fp.write("TOTAL=%s" % total + "\n")
        fp.write("PASSED=%s" % passed + "\n")
        fp.write("FAILED=%s" % failed + "\n")
        fp.write("ERROR=%s" % error + "\n")
        fp.write("SKIPPED=%s" % skipped + "\n")
        fp.write("SUCCESSFUL=%.2f%%" % successful + "\n")
        fp.write("TOTAL_TIMES=%.2fs" % duration + "\n")

        #将失败的测试案例和错误消息写入文件
        failed_cases = [report.nodeid for report in terminalreporter.stats.get('failed',[]) if report.when !='teardown']
        for case in failed_cases:
            fp.write(f"FAILED_CASE={case}"+"\n")





