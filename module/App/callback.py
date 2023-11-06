from dash import Dash, dcc, html, Output, Input, State, callback_context
from module.Firebase.firebase import FirebaseManager
from flask_socketio import SocketIO
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go

"""
firebase의 realtime DB는 데이터가 업데이트 혹은 추가되는 경우 이벤트가 발생함.
이를 잘 활용해서 실시간으로 데이터 업데이트를 추적할 수 있음.

github : https://github.com/nhorvath/Pyrebase4

"""

class CallbackManager:
    """
    앱 콜백 정의
    """

    def __init__(self, app, server):
        self.app = app # Dash에 대한 객체
        self.server = server # server에 대한 객체
        self.firebase = FirebaseManager() # Firebase에 대한 객체
        self.__user = None # 현재 로그인한 사용자

        
    def resources_callback(self):
        """
        사용자 컴퓨터 자원 정보 출력 콜백
        """
        pass

    def carbon_emission_fig_callback(self):
        """
        탄소 배출 그래프 출력 콜백
        데이터를 받아와서 실시간 그래프 업데이트
        """
        pass

    def gpu_freq_fig_callback(self):
        """
        GPU 주파수 그래프 출력 콜백
        데이터를 받아와서 실시간 그래프 업데이트
        """
        pass

    def carbon_density_fig_callback(self):
        """
        탄소 집약도 그래프 출력 콜백
        데이터를 받아와서 실시간 그래프 업데이트
        API : https://app.electricitymaps.com/zone/KR
        """
        pass

    def energy_output_fig_callback(self):
        """
        에너지 출처 그래프 출력
        https://app.electricitymaps.com/zone/KR
        위 사이트에서 데이터 받아서 사용 (가능 여부는 개발 담당이 판단)
        """
        pass

    def geo_callback(self):
        """
        현재 딥러닝 학습이 진행되는 컴퓨터의 물리적 위치 출력
        firebase와 통신이 필요
        """
        pass
    