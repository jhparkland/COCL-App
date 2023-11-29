# # Dash의 기본 구조는 app=Dash()와 if __name__은 값 사이에 html 코드를 React의 css-component 형식으로 바인딩하여 구성!
# # Callback은 결국 UseState와 같은 식별 변수로 이를 통해 객체 지향 코드 구현 가능.
# # 한 dropdown에 ID를 설정하고 그 ID에 있는 값(특정 값 선택)이 바뀔 때 마다 Callback 함수가 호출됨. 
# # Input ID 값을 인식해서 그 값에 대한 Callback 함수 출력 결과를 Output 변수가 있는 자리에 출력! (Output ID는 Input ID가 변화될 때 출력될 공간을 지정하는 역할)
# # Output('id','children')에서 'children'은 id값이 있는 공간에 출력하라는 뜻
# # dash_table.DataTable(dict 형태로 값 주는게 자주 쓰임. )
# '''
# @app.callback() => Output, Input으로 구성., Input의 ID와 callbackfunc(ID)를 맞추면 됨
# def callbackfunc(ID):
#    함수의 동작 코드
#     return 동작 결과
# '''
# # 코드를 쓸 때<> 태그 기반이 아닌 html.[태그명](속성) 기반으로 동작하
# # 드롭다운이나 버튼, 입력 폼 같이 사용자와 Interaction할 수 있는 개체에 대해서는 id값을 주고, 그 id 값에 변화하는 것에 따라 

# # CSS 잘 안 먹히면 아래 Dash Div 포맷으로 한 번 더 감싸주기~
# '''
#     html.Div(
#         children=[

#         ],
#         style={"display": "block"} 
#     )
# '''
# # 초기 참고 블로그-https://abluesnake.tistory.com/152
# #===============================================================================================================================================

# from dash import Dash, html, dcc
# import plotly.express as px
# import pandas as pd

# app = Dash(__name__)

# data = {
#     'Categories': ['Category A', 'Category B', 'Category C'],
#     'Values': [30, 40, 30]
# }

# # Create a pie chart using Plotly Express
# fig_pie = px.pie(data, values='Values', names='Categories', title='Example Pie Chart')

# fig_pie.update_layout(
#     #paper_bgcolor='lightgray',  # Change 'lightgray' to the desired color
#     width=380,  # Change width to the desired width
#     height=400  # Change height to the desired height
# )

# app.layout = html.Div(children=[
#     # Website Main Logo
#     html.Div(
#         children="Carbon-Watch",
#         className="header",
#     ),

#     html.Div(
#         children=[
#             # 1st-Column(25%)
#             html.Div(
#                 children=[
#                 dcc.Graph(
#                     id='example-pie-chart',  # Provide a unique ID for the graph
#                     figure=fig_pie  # Pass the Plotly figure to the 'figure' attribute
#                 ),  
#                 html.Div(
#                     children="Net-Zero 달성률",
#                     style={"width": "100%","height": "35%", "background-color":"yellow"},
#                 ),
#                 html.Div(
#                     children="1PC 평균 탄소 배출량",
#                     style={"width": "100%","height": "35%", "background-color":"green"}
#                 ),
#                 html.Div(
#                     children="GPU 전력 비용",
#                     style={"width": "100%","height": "30%", "background-color":"blue"}
#                 ),
#             ],
#             className="column1"
#             ),

#             # 2nd-Column(50%)
#             html.Div(
#                 children=[
#                 html.Div(
#                     children="Net-Zero 달성률",
#                     style={"width": "100%","height": "35%", "background-color":"orange"},
#                 ),
#                 html.Div(
#                     children="1PC 평균 탄소 배출량",
#                     style={"width": "100%","height": "65%", "background-color":"gray"}
#                 ),
#             ],
#             className="column2"
#             ),

#             # 3rd-Column(25%)
#             html.Div(
#                 children=[
#                 html.Div(
#                     children="Net-Zero 달성률",
#                     style={"width": "100%","height": "35%", "background-color":"yellow"},
#                 ),
#                 html.Div(
#                     children="1PC 평균 탄소 배출량",
#                     style={"width": "100%","height": "65%", "background-color":"green"}
#                 ),
#             ],
#             className="column3"
#             ),

#         ],
#         style={"width": "100%","height":"90vh", "align-items": "center", "justify-content": "center", "display": "flex"} 
#     )

# # 전체에 대한 CSS
# ], className="mainpage")


# if __name__ == '__main__':
#     app.run_server(debug=True)