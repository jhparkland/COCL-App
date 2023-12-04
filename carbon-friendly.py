from dash import Dash, dcc, html # Dash components
from module.App.callback import CallbackManager # callback functions
from module.App.layout import LayoutManager # layout functions
import dash_bootstrap_components as dbc # bootstrap components

app = Dash(__name__, 
           external_stylesheets=[dbc.themes.BOOTSTRAP], 
)

app.title = 'Carbon friendly' # app title
app._favicon = 'assets/favicon/favicon.ico' # app favicon
server = app.server #  server connection

# create layout
layout = LayoutManager(app) 
app.layout = layout.create_layout()

# create callback
callback = CallbackManager(app, server)

callback.create_join_callback() # 회원가입 콜백
callback.create_login_callback() # 로그인 콜백
callback.refresh_token_callback() # 토큰 갱신 콜백
callback.create_logout_callback() # 로그아웃 콜백
callback.resources_callback() # 사용자 정보 갱신 콜백



if __name__ == "__main__":
    # app.run(debug=True)
    app.run_server(debug=True)

