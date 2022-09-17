from typing import List

from attendance import Attendance
from hufe_yiban import HufeYiban

if __name__ == '__main__':
    attendanceList: List[Attendance] = [HufeYiban()]
    for att in attendanceList:
        att.attendance()
