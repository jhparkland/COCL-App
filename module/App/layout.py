from dash import Dash, dcc, html
import dash_bootstrap_components as dbc
import plotly.express as px
import plotly.graph_objs as go

class LayoutManager:
    """
    앱 레이아웃 정의
    """

    def __init__(self, app):
        self.app = app # Dash 인스턴스

        # 그래프
        self.ev_use_fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])]) # 전력 사용량 그래프
        self.ev_use_fig.update_layout(margin=dict(l=0, r=0, t=40, b=0), title=f'서버 #: 전력 사용량')

        self.carbon_emission_fig = go.Figure(data=[go.Indicator(mode = "number+gauge+delta",
                                                                 gauge = {'shape': "bullet"},    
                                                                 delta = {'reference': 300}, 
                                                                 value = 220,
                                                                 domain = {'x': [0.1, 1], 'y': [0.2, 0.9]},
                                                                 title = {'text': "Avg order size"})]) # 탄소 배출량 그래프
        
        self.carbon_emission_fig.update_layout(margin=dict(l=0, r=0, t=40, b=0), title=f'서버 #: 탄소 배출량')

        self.gpu_freq_fig = go.Figure(data=[go.Indicator(mode = "gauge+number",
                                                        value = 450,
                                                        title = {'text': "Speed"},
                                                        domain = {'x': [0, 1], 'y': [0, 1]})]) # GPU 사용량 그래프
        self.gpu_freq_fig.update_layout(margin=dict(l=0, r=0, t=40, b=0), title=f'서버 #: GPU 주파수')

        self.carbon_density_fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])]) # 탄소 밀도 그래프
        self.carbon_density_fig.update_layout(margin=dict(l=0, r=0, t=40, b=0), title=f'지역 #: 탄소 밀집도')

        self.energy_output_fig = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])]) # 에너지 출력 그래프
        self.energy_output_fig.update_layout(margin=dict(l=0, r=0, t=40, b=0), title=f'지역 #: 에너지 출처')

        self.geo = go.Figure(data=go.Scattergeo(
            lon = [126.9780],
            lat = [37.5665],
            text = ['Seoul'],
            mode = 'markers',
            marker_color = 'rgb(255, 0, 0)',
            ))
        self.geo.update_layout(
            title = '물리적 서버 위치',
            geo_scope='asia',
            margin=dict(l=0, r=0, t=40, b=0)
        )   


        # 로고(추후 이미지로 대체)
        self.Logo = html.H1(
            "Carbon-friendly",
            className="bg-dark text-white p-2 mb-2 text-center"
        )

        
        self.controls = dbc.Card(
            self.Logo,
            body=True,
        )
        
        # 리소스 모니터
        self.resources = dbc.Container(
                        dbc.Card([html.H2("Computing Info🖥️(여기 약간 실시간 프로세서,  gpu 사용량 조회 시키기)"), 
                                html.Div("CPU", id = 'cpu'), 
                                html.Br(), 
                                html.Div("Memory", id = 'ram'), 
                                html.Br(), 
                                html.Div("GPU", id = 'gpu')],
                                body=True)
                    )
        
        # footer
        self.footer = html.Div([
                        html.P("© 2023 Data Science Lab All Rights Reserved."),
                        html.P([
                            html.P("49315. 부산광역시 사하구 낙동대로 550번길 37(하단동) 동아대학교 공과대학1호관 4층 423호"),
                            html.A("Lab Website", href="https://www.datasciencelabs.org/", target='_blank'),
                            html.A("Contact Us", href="https://github.com/datascience-labs", target='_blank'),
                            html.A("Maker github", href="https://github.com/jhparkland", target='_blank'),])
                        ],className="footer")


    def create_layout(self):
        """
        앱 레이아웃 생성

        Returns:
            _type_: 사전에 정의된 레이아웃 요소로 부터 레이아웃 생성
        """
        return dbc.Container([
                dbc.Row([
                    dbc.Col([
                        self.controls,
                        dbc.Row(
                            self.resources
                        )
                    ], width=3),

                    dbc.Col([
                    
                        dbc.Row([
                            dbc.Col(dbc.Card([html.Div(dcc.Graph(figure=self.ev_use_fig))], body=True, ), width=4),
                            dbc.Col(dbc.Card([html.Div(dcc.Graph(figure=self.carbon_emission_fig))], body=True, ), width=4),
                            dbc.Col(dbc.Card([html.Div(dcc.Graph(figure=self.gpu_freq_fig))], body=True, ), width=4),
                        ]),
                        dbc.Row([
                            dbc.Col(dbc.Card([html.Div(dcc.Graph(figure=self.geo))], body=True))
                        ]),
                        dbc.Row([
                            dbc.Col(dbc.Card([html.Div(dcc.Graph(figure=self.carbon_density_fig))], body=True, ), width=6),
                            dbc.Col(dbc.Card([html.Div(dcc.Graph(figure=self.energy_output_fig))], body=True, ), width=6),
                        ]),

                    ], width=9),

                ]),
                
                self.footer,
                
                
            ],fluid=True, className="dbc dbc-ag-grid",)

