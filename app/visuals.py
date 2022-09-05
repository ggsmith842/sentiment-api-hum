import plotly.graph_objects as go
from plotly.offline import plot
#pip install kaleido?

def plot_sentiment(score):
        
    fig = go.Figure(go.Indicator(
        mode = "gauge+number",
        value = score,
        domain = {'x': [0, 1], 'y': [0, 1]},
        title = {'text': "Sentiment"},
        gauge = {
            'axis': {'range': [-1, 1], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "#5E81AC"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "gray",
            'steps': [
                {'range': [-1, -0.20], 'color': '#BF616A'},
                {'range': [-.20, 0.20], 'color': 'lightgrey'},
                {'range': [0.20, 1], 'color': '#A3BE8C'}],
            'threshold': {
                'line': {'color': "#5E81AC", 'width': 4},
                'thickness': 0.75,
                'value': score}}))

    fig.update_layout(
        margin=dict(l=20, r=20, t=0, b=0),
        paper_bgcolor="#D8DEE9"
    )
   
    config_dict = {'displayModeBar': False}
    fig.write_html("app/templates/gauge.html",
                full_html=False,
                include_plotlyjs='cdn',
                config = config_dict)

    return fig