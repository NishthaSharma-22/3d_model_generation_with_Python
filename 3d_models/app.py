import plotly.graph_objects as go
import numpy as np
from PIL import Image

img = Image.open('encrypted_medical_info_qr.png').convert('L')
img_array = np.array(img)

x = np.linspace(0, img_array.shape[1], img_array.shape[1])
y = np.linspace(0, img_array.shape[0], img_array.shape[0])

x_scale = 4.0
y_scale = 4.0
z_scale = 0.01

x = np.linspace(0, img_array.shape[1], img_array.shape[1]) * x_scale
y = np.linspace(0, img_array.shape[0], img_array.shape[0]) * y_scale
x, y = np.meshgrid(x, y)

z = img_array * z_scale

fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])


fig.update_layout(title='3D Surface from Image', scene=dict(
    zaxis_title='Pixel Intensity',
    xaxis_title='X Axis',
    yaxis_title='Y Axis'),
    autosize=False,
    width=700,
    height=700
)
fig.show()
