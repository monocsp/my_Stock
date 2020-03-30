import time
import win32com.client
import pandas as pd

class CREON(object):
    """대신증권 크레온 API"""

    def __init__(self):
        # 연결 여부 체크
        self.objCpCybos = win32com.client.Dispatch("CpUtil.CpCybos")
        bConnect = self.objCpCybos.IsConnect
        if (bConnect == 0):
            print("PLUS가 정상적으로 연결되지 않음. ")
            exit()

    def setMethod(self, code, char, from_yyyymmdd=None, to_yyyymmdd=None, count=None):
        """
        count는 보통 상식의 데이터 개수가 아니다.
        여기서는 한번 요청 시 가져와지는 데이터의 개수이다.
        한번 요청 시 최대 2856개 가능하다.

        원하는 데이터 개수가 있으면 to_yyyymmdd 로 가져온 다음에 잘라서 사용한다.
        하루에 분단위 데이터가 381개이다. (* 마지막 10분은 동시호가)

        """
        # object 구하기
        self.objStockChart = win32com.client.Dispatch("CpSysDib.StockChart")
        self.objStockChart.SetInputValue(0, code)  # 종목코드

        if to_yyyymmdd:
            self.objStockChart.SetInputValue(1, ord('1'))  # 요청 구분 '1': 기간, '2': 개수
            self.objStockChart.SetInputValue(2, from_yyyymmdd)  # To 날짜
            self.objStockChart.SetInputValue(3, to_yyyymmdd)  # From 날짜
        elif count:
            self.objStockChart.SetInputValue(1, ord('2'))  # 개수로 받기
            self.objStockChart.SetInputValue(4, count)  # 조회 개수
        else:
            raise print("기간을 입력해주세요.")

        self.objStockChart.SetInputValue(5, [0, 1, 2, 3, 4, 5, 8])  # 요청항목 - 날짜, 시간,시가,고가,저가,종가,거래량
        self.objStockChart.SetInputValue(6, ord(char))  # '차트 주기 - 분/틱
        self.objStockChart.SetInputValue(7, 1)  # 분틱차트 주기

        self.objStockChart.SetInputValue(9, ord('1'))  # 수정주가 사용

        self.data = {
            "date": [],
            "time": [],
            "open": [],
            "high": [],
            "low": [],
            "close": [],
            "vol": [],
        }

    def checkRequest(self):

        self.objStockChart.BlockRequest()

        rqStatus = self.objStockChart.GetDibStatus()

        if rqStatus != 0:
            return False

        #         else:
        #             print("통신상태 양호, 누적 개수 {}".format(len(self.data["date"])))

        self.count = self.objStockChart.GetHeaderValue(3)

        if self.count <= 1:
            return False

        return int(self.count)

    def checkRemainTime(self):

        # 연속 요청 가능 여부 체크
        remainTime = self.objCpCybos.LimitRequestRemainTime / 1000.
        remainCount = self.objCpCybos.GetLimitRemainCount(1)  # 시세 제한

        if remainCount <= 0:
            print("15초당 60건으로 제한합니다.")
            time.sleep(remainTime)

    def getStockPriceMin(self):

        while 1:

            self.checkRemainTime()
            rows = self.checkRequest()

            if rows:

                for i in range(rows):
                    self.data["date"].append(self.objStockChart.GetDataValue(0, i))
                    self.data["time"].append(self.objStockChart.GetDataValue(1, i))
                    self.data["open"].append(self.objStockChart.GetDataValue(2, i))
                    self.data["high"].append(self.objStockChart.GetDataValue(3, i))
                    self.data["low"].append(self.objStockChart.GetDataValue(4, i))
                    self.data["close"].append(self.objStockChart.GetDataValue(5, i))
                    self.data["vol"].append(self.objStockChart.GetDataValue(6, i))
            else:

                break

        return self.data

creon = CREON()
creon.setMethod(code="A005930", char="m", from_yyyymmdd=20200101, to_yyyymmdd=10000101)
%%time
samsung = creon.getStockPriceMin()
tmp = pd.DataFrame(samsung)
tmp.tail()
creon.setMethod(code="A005930", char="D", from_yyyymmdd=20200101, to_yyyymmdd=10000101)
%%time
samsung = creon.getStockPriceMin()
tmp = pd.DataFrame(samsung)
tmp.tail()