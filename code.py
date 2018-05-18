from graphviz import Digraph
import os
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
from graphviz import Graph
h = Graph('html_table', format='jpg', engine='circo')
f = open('order.txt', 'r')
n = int(f.readline())
for i in range(1, n + 1):
    j = int(f.readline())
    t = 'tab' + str(j)
    t1 = 'img/' + str(j) + '.jpg'
    b = str(f.readline())
    h.node(t, label='''<<TABLE border = "0" fixedsize = "false" height = "10" width = "100" cellpadding = "0" color = "black">
      <TR>
        <TD><img src = "''' + t1 + '''"/></TD>
      </TR>
      <TR>
        <TD>''' + b + '''</TD>
      </TR>
     </TABLE>>''', shape="box")
    if i > 1:
        h.edge('tab' + str(k), t)
    k = j
h.render('graph', view=True)
