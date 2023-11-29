# Dash의 기본 구조는 app=Dash()와 if __name__은 값 사이에 html 코드를 React의 css-component 형식으로 바인딩하여 구성!
# Callback은 결국 UseState와 같은 식별 변수로 이를 통해 객체 지향 코드 구현 가능.
# 한 dropdown에 ID를 설정하고 그 ID에 있는 값(특정 값 선택)이 바뀔 때 마다 Callback 함수가 호출됨. 
# Input ID 값을 인식해서 그 값에 대한 Callback 함수 출력 결과를 Output 변수가 있는 자리에 출력! (Output ID는 Input ID가 변화될 때 출력될 공간을 지정하는 역할)
# Output('id','children')에서 'children'은 id값이 있는 공간에 출력하라는 뜻
# dash_table.DataTable(dict 형태로 값 주는게 자주 쓰임. )
'''
@app.callback() => Output, Input으로 구성., Input의 ID와 callbackfunc(ID)를 맞추면 됨
def callbackfunc(ID):
   함수의 동작 코드
    return 동작 결과
'''
# 코드를 쓸 때<> 태그 기반이 아닌 html.[태그명](속성) 기반으로 동작하
# 드롭다운이나 버튼, 입력 폼 같이 사용자와 Interaction할 수 있는 개체에 대해서는 id값을 주고, 그 id 값에 변화하는 것에 따라 

# CSS 잘 안 먹히면 아래 Dash Div 포맷으로 한 번 더 감싸주기~
'''
    html.Div(
        children=[

        ],
        style={"display": "block"} 
    )
'''
# 초기 참고 블로그-https://abluesnake.tistory.com/152
#===============================================================================================================================================

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd
import numpy as np
import plotly.graph_objs as go

app = Dash(__name__)

# Pie Chart
data = {
    'Categories': ['Category A', 'Category B'],
    'Values': [80, 20]
}

# Create a pie chart using Plotly Express
fig_pie = px.pie(data, values='Values', names='Categories', title='Net-Zero 달성률')

fig_pie.update_layout(
    margin=dict(l=30, r=30, t=30, b=30),
    width=340,  # Change width to the desired width
    height=300,  # Change height to the desired height
    title_x=0.5  # Set the title's x-position to 0.5 (center)
)

# Pie Chart
data2 = {
    'Categories': ['Category A', 'Category B'],
    'Values': [60, 40]
}

# Create a pie chart using Plotly Express
fig_pie2 = px.pie(data2, values='Values', names='Categories', title='평균 탄소 배출량(1PC)')

fig_pie2.update_layout(
    #paper_bgcolor='lightgray',  # Change 'lightgray' to the desired color
    margin=dict(l=30, r=30, t=30, b=30),
    width=340,  # Change width to the desired width
    height=300,  # Change height to the desired height
    title_x=0.5  # Set the title's x-position to 0.5 (center)
)

# line chart
hours = pd.date_range('2023-01-01', periods=12, freq='H')
power_consumed = [15, 14, 15, 16, 18, 20, 21, 22, 20, 18, 17, 16]  # Example values for power consumed
power_produced = [5, 7, 9, 12, 15, 18, 19, 18, 16, 14, 12, 9]  # Example values for power produced

# Create the line chart using Plotly graph objects
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=hours, y=power_consumed, mode='lines+markers', name='Sum of Power Consumed'))
fig_line.add_trace(go.Scatter(x=hours, y=power_produced, mode='lines+markers', name='Amount of Power Produced'))

fig_line.update_layout(
    title='2023년도 11월 전력 소모-생산량 총계',
    xaxis_title='Time',
    yaxis_title='Power',
    legend=dict(
        orientation="h",  # Set the orientation of the legend to 'h' (horizontal)
        yanchor="bottom",  # Anchor the legend to the bottom of the plot
        y=1.02,  # Move the legend slightly above the top of the plot (value > 1 moves it above)
        xanchor="right",  # Anchor the legend to the right side of the plot
        x=1  # Set the legend position to the right side
    ),
    title_x=0.5  # Set the title's x-position to 0.5 (center)
)

# stacked bar chart
classrooms = ['601', '602', '603', '604', '605', '606', '607', '608', '609', '610']
data = {
    'Classroom': classrooms * 2,  # Repeat classrooms for two categories
    'Subjects': [5, 3, 7, 8, 23, 16, 9, 31, 14, 18] + [17, 13, 8, 15, 4, 14, 15, 11, 16, 17],  # Example values for subjects
    'l': ['딥러닝 활용 실습 과목'] * 10 + ['이론 과목'] * 10,  # Categories for legends
}

# Create Stacked bar chart using Plotly Express
fig_stacked_bar = px.bar(data_frame=data, x='Classroom', y='Subjects', color='l', barmode='stack',
                        width=1000, height=600)


fig_stacked_bar.update_layout(
    width=850,  # Change width to the desired width
    height=550,  # Change height to the desired height
    title={
        'text': '강의실별 이론/실습 수업 비중',
        'x': 0.35,  # Centering the title
        'y': 0.95  # Adjusting title's vertical position
    },
    legend=dict(
        orientation="h",  # Set the orientation of the legend to 'h' (horizontal)
        yanchor="bottom",  # Anchor the legend to the bottom of the plot
        y=1.02,  # Move the legend slightly above the top of the plot (value > 1 moves it above)
        xanchor="right",  # Anchor the legend to the right side of the plot
        x=1  # Set the legend position to the right side
    ),
)


time_intervals = ['9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM',
                  '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM']
y_values = [23, 12, 3, 23, 56, 23, 4, 6, 2, 2, 1, 6]

# Define a color scale using HEX codes for the gradient
colorscale = [
    [0, '#FFC300'],  # Start color
    [0.5, '#FF5733'],  # Middle color
    [1, '#C70039']   # End color
]

# Creating the horizontal bar chart with a color gradient
fig_horiz_bar1 = go.Figure(data=[go.Bar(
    y=time_intervals,  # Assigning categories to the y-axis
    x=y_values,        # Assigning values to the x-axis
    orientation='h',  # Setting the orientation to horizontal
    marker=dict(
        color=y_values,    # Assigning colors based on y_values
        colorscale=colorscale,  # Applying the defined colorscale
        colorbar=dict(title='Color Scale'),  # Adding color scale
    ),
)])

# Customizing layout
fig_horiz_bar1.update_layout(
    title='이론 과목의 시간대별 분포',  # Adding a title
    xaxis_title='Values',           # Labeling x-axis
    yaxis_title='Categories',       # Labeling y-axis
    height=500,                     # Setting the height of the chart
    width=450,
    title_x=0.5  
)

time_intervals = ['9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM',
                  '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM']
y_values = [23, 12, 3, 23, 56, 23, 4, 6, 2, 2, 1, 6]

# Define the Inferno color scale
colorscale = px.colors.sequential.Agsunset

# Creating the horizontal bar chart with Inferno color scale
fig_horiz_bar2 = go.Figure(data=[go.Bar(
    y=time_intervals,  # Assigning categories to the y-axis
    x=y_values,        # Assigning values to the x-axis
    orientation='h',   # Setting the orientation to horizontal
    marker=dict(
        color=y_values,    # Assigning colors based on y_values
        colorscale=colorscale,  # Applying the defined colorscale
        colorbar=dict(title='Color Scale'),  # Adding color scale
    ),
    
)])

# Customizing layout
fig_horiz_bar2.update_layout(
    title='실습 과목(딥러닝)의 시간대별 분포',  # Adding a title
    xaxis_title='Values',           # Labeling x-axis
    yaxis_title='Categories',       # Labeling y-axis
    height=450,                     # Setting the height of the chart
    width=450,
)

# last gpu bar-line
times = ['9:00 AM', '10:00 AM', '11:00 AM', '12:00 PM', '1:00 PM', '2:00 PM',
                  '3:00 PM', '4:00 PM', '5:00 PM', '6:00 PM']
values_bar = [5,9,13,21,24,19,10,5,3,2]
values_line = [7,14,15,23,27,23,14,11,4,3]

# Create a bar trace
trace_bar = go.Bar(
    x=times,
    y=values_bar,
    name='Bar Chart'
)

# Create a line trace
trace_line = go.Scatter(
    x=times,
    y=values_line,
    mode='lines+markers',
    name='Line Chart'
)

# Create the figure with both traces
fig_gpu = go.Figure()
fig_gpu.add_trace(trace_bar)
fig_gpu.add_trace(trace_line)

# Update layout settings
fig_gpu.update_layout(
    margin=dict(l=30, r=30, t=30, b=30),
    title='실습과목에서 GPU에 소모되는 전력',
    xaxis_title='Categories',
    yaxis_title='Values',
    height=350,                     # Setting the height of the chart
    width=450,
    legend=dict(
        orientation="h",  # Set the orientation of the legend to 'h' (horizontal)
        yanchor="bottom",  # Anchor the legend to the bottom of the plot
        y=1.02,  # Move the legend slightly above the top of the plot (value > 1 moves it above)
        xanchor="right",  # Anchor the legend to the right side of the plot
        x=1  # Set the legend position to the right side
    ),
    title_x=0.5  # Set the title's x-position to 0.5 (center)
)



app.layout = html.Div(children=[
    
    # Website Main Logo
    html.Div(
        children="Carbon-Watch",
        className="header",
    ),

    html.Div(
        children=[
            # 1st-Column(25%)
            html.Div(
                children=[
                html.Br(),
                html.Div(
                    dcc.Graph(
                        id='example-pie-chart',  # Provide a unique ID for the graph
                        figure=fig_pie  # Pass the Plotly figure to the 'figure' attribute
                    ),
                    style={"width": "100%","height": "30%"},
                ),
                html.Div(
                    dcc.Graph(
                        id='example-pie-chart',  # Provide a unique ID for the graph
                        figure=fig_pie2  # Pass the Plotly figure to the 'figure' attribute
                    ),
                    style={"width": "100%","height": "30%"},
                ),
                html.Div(
                    dcc.Graph(
                        id='example-pie-chart',  # Provide a unique ID for the graph
                        figure=fig_gpu  # Pass the Plotly figure to the 'figure' attribute
                    ),
                    style={"width": "100%","height": "40%"},
                ),
            ],
            className="column1"
            ),

            # 2nd-Column(50%)
            html.Div(
                children=[
                html.Div(
                    dcc.Graph(
                        id='example-pie-chart',  # Provide a unique ID for the graph
                        figure=fig_line  # Pass the Plotly figure to the 'figure' attribute
                    ),
                    style={"width": "100%","height": "35%","text-align":"center"},
                ),
                html.Br(),
                html.Br(),
                html.Div(
                    dcc.Graph(
                        id='example-pie-chart',  # Provide a unique ID for the graph
                        figure=fig_stacked_bar # Pass the Plotly figure to the 'figure' attribute
                    ),
                    style={"width": "100%","height": "65%"}
                ),
            ],
            className="column2"
            ),

            # 3rd-Column(25%)
            html.Div(
                children=[
                html.Div(
                    dcc.Graph(
                        id='example-pie-chart',  # Provide a unique ID for the graph
                        figure=fig_horiz_bar1 # Pass the Plotly figure to the 'figure' attribute
                    ),
                    style={"width": "100%","height": "35%"},
                ),
                html.Br(),
                html.Br(),
                html.Br(),
                html.Div(
                    dcc.Graph(
                        id='example-pie-chart',  # Provide a unique ID for the graph
                        figure=fig_horiz_bar2 # Pass the Plotly figure to the 'figure' attribute
                    ),
                    style={"width": "100%","height": "65%"}
                ),
            ],
            className="column3"
            ),

        ],
        style={"width": "100%","height":"90vh", "align-items": "center", "justify-content": "center", "display": "flex"} 
    )

# 전체에 대한 CSS
], className="mainpage")


if __name__ == '__main__':
    app.run_server(debug=True)