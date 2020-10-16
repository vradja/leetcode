#!/usr/bin/env python
# coding: utf-8

# In[247]:


import os
from collections import Counter

import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image
from sklearn.cluster import KMeans

# In[248]:


size1 = int(input("Please enter the number of parent category, eg. 7 :"))

# In[249]:


size2 = int(input("Please enter the number of subcategory, eg. 5 :"))

# In[277]:


path = input("Please enter the path to image, eg.poppies_full 1886.jpg : ")

# In[278]:


# This is where file, folder/directory & merge of images are performed:
cumulative_data = list()

# This is for file input:
if os.path.isfile(path):
    im = Image.open(path)
    data = im.getcolors(im.size[0] * im.size[1])
    for d in data:
        cumulative_data += [d[1]] * d[0]


# In[279]:


def kmeans_func(size, data):
    km = KMeans(n_clusters=size).fit(data)
    centroids = km.cluster_centers_
    cluster_colors = [(int(a[0]), int(a[1]), int(a[2])) for a in centroids]
    cluster_hex_colors = ['#%02x%02x%02x' % i for i in cluster_colors]
    sizes = [x[1] for x in sorted(Counter(km.labels_).items(), key=lambda x: x[0])]
    return cluster_colors, cluster_hex_colors, sizes, km


# In[280]:


mydf = pd.DataFrame(columns=['RGB', 'class1_id', 'class2_id', 'class2_count', 'class1name', 'class2name'])

# In[281]:


cluster_colors1, cluster_hex_colors1, sizes1, km1 = kmeans_func(size1, cumulative_data)

# In[282]:


# Plot Histogram from clusters:
plt.bar(cluster_hex_colors1, sizes1, color=cluster_hex_colors1)
plt.xticks(rotation='vertical')
plt.show()

# In[283]:


mydf["RGB"] = cumulative_data
mydf["class1"] = km1.labels_

# In[284]:


mydf['class1name'] = mydf['class1'].apply(lambda x: cluster_hex_colors1[x])


# In[285]:


def get_kmeans_pred(df, km, class_name, sizes, cluster_hex_colors):
    if df["class1"] == class_name:
        label_id = km.predict([df["RGB"]])[0]
        df["class2name"] = cluster_hex_colors[label_id]
        df["class2"] = int(label_id)
        df["class2_count"] = sizes[label_id]
        return df
    else:
        return df


# In[ ]:


mydf.shape

# In[ ]:


for class_name in range(size1):
    temp_df = mydf[mydf["class1"] == class_name].reset_index()
    temp_data = temp_df["RGB"].to_list()
    cluster_colors2, cluster_hex_colors2, sizes2, km2 = kmeans_func(size2, temp_data)
    mydf = mydf.apply(lambda x: get_kmeans_pred(x, km2, class_name, sizes2, cluster_hex_colors2), axis=1)
    mydf.loc[mydf["class1"] == class_name, "class2_rgb"] = mydf.loc[mydf["class1"] == class_name]["class2"].apply(
        lambda x: cluster_colors2[int(x)])
    cluster_colors2, cluster_hex_colors2, sizes2, km2 = None, None, None, None

# In[262]:


# mydf.to_csv("mydf.csv",index=False)


# In[ ]:


mynew = mydf[["class1name", "class2name", "class2_count", "class2_rgb"]]

# In[ ]:


mynew.groupby(["class1name", "class2name"]).ngroups

# In[ ]:


mynew = mynew.drop_duplicates(keep="first")

# In[ ]:


mynew["class1name"].nunique()

# In[ ]:


mynew

# In[ ]:


# mynew.to_csv("Tanvi.csv",index = False)


# In[ ]:


labels = mynew["class2name"].to_list() + list(mynew["class1name"].unique())
parents = mynew["class1name"].to_list() + [""] * int(mynew["class1name"].nunique())
values = mynew["class2_count"].to_list() + [0] * int(mynew["class1name"].nunique())
marker_colors = mynew["class2name"].to_list() + list(mynew["class1name"].unique())

# In[ ]:


assert len(labels) == len(parents) == len(values) == len(marker_colors)

# In[ ]:


import plotly.graph_objs as go

trace1 = go.Treemap(
    labels=labels,
    values=values,
    parents=parents,
    marker_colors=marker_colors,
    pathbar={"visible": False},
    insidetextfont={"size": 1, "color": marker_colors},
)

data = [trace1]

layout = go.Layout(
    margin={"b": 0, "l": 0, "r": 0, "pad": 0, "t": 0},
    autosize=False,
    width=500,
    height=500,
    xaxis=dict(
        autorange=True,
        showgrid=False,
        ticks='',
        showticklabels=False
    ),
    yaxis=dict(
        autorange=True,
        showgrid=False,
        ticks='',
        showticklabels=False
    )
)

fig = go.Figure(data=data, layout=layout)
fig.show()

# In[ ]:


fig = go.Figure()
RGBs = mynew["class2_rgb"].to_list()
fig.add_trace(go.Scatter(
    y=[x[0] for x in RGBs], x=[x[1] for x in RGBs],
    mode='markers',
    marker_color=mynew["class2name"].to_list()
))

# Set options common to all traces with fig.update_traces
fig.update_traces(mode='markers', marker_line_width=2, marker_size=10)
fig.update_layout(

    plot_bgcolor='rgb(255,255,255)',
    yaxis_zeroline=False, xaxis_zeroline=False,
    autosize=False,
    width=500,
    height=500,
    xaxis=dict(
        title="Green Value",
        autorange=True,
        showgrid=True,
        ticks='',
        showticklabels=True
    ),

    yaxis=dict(
        title="Red Value",
        autorange=True,
        showgrid=True,
        ticks='',
        showticklabels=True
    )

)

fig.update_xaxes(showgrid=True, gridwidth=2, gridcolor='LightGrey')
fig.update_yaxes(showgrid=True, gridwidth=2, gridcolor='LightGrey')
fig.show()

# In[ ]:


trace3d = go.Scatter3d(x=[x[0] for x in RGBs],
                       y=[x[1] for x in RGBs],
                       z=[x[2] for x in RGBs],
                       mode='markers',
                       marker=dict(size=5,
                                   color=['rgb({},{},{})'.format(r, g, b) for r, g, b in RGBs],
                                   opacity=0.9, ))

# In[ ]:


data3d = [trace3d]

# In[ ]:


layout = go.Layout(margin=dict(l=0,
                               r=0,
                               b=0,
                               t=0))

fig3d = go.Figure(data=data3d, layout=layout)

# In[ ]:


fig3d.update_layout(scene=dict(
    xaxis_title='Red Value',
    yaxis_title='Green Value',
    zaxis_title='Blue Value',
    xaxis=dict(
        backgroundcolor="rgb(239, 238, 237)",
        gridcolor="lightgrey",
        showbackground=True,
        zerolinecolor="white",
        title_font_color="red"),
    yaxis=dict(
        backgroundcolor="rgb(239, 238, 237)",
        gridcolor="lightgrey",
        showbackground=True,
        zerolinecolor="white",
        title_font_color="green"),
    zaxis=dict(
        backgroundcolor="rgb(239, 238, 237)",
        gridcolor="lightgrey",
        showbackground=True,
        zerolinecolor="white",
        title_font_color="blue"),
),
    width=700,
    margin=dict(
        r=10, l=10,
        b=10, t=10)
)
fig3d.show()

# In[ ]:


# In[ ]:
