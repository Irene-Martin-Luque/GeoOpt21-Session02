#AIA Module at MaCAD, IaaC, directed by David Andrés León
#Session 02, Assinment 02 - GH to Python through Hops
#Excercise by Irene Martín Luque based on template

#importing libraries and 'geometry' file
from flask import Flask
import ghhops_server as hs
import rhino3dm as rg
import geometry as geo

app = Flask(__name__)
hops = hs.Hops(app)

#creating the Hops component
@hops.component(
    "/createStarGraph",
    name = "Create a Star Graph",
    inputs=[
    ],
    outputs=[
       hs.HopsPoint("Nodes","N","List of Nodes ", hs.HopsParamAccess.LIST),
       hs.HopsCurve("Edges","E","List of Edges ", hs.HopsParamAccess.LIST)

    ]
)
def createStarGraph():

    G = geo.createGridGraph()
    GW = geo.addRandomWeigths(G)

    nodes = geo.getNodes(GW)
    edges = geo.getEdges(GW) 

    return nodes, edges





if __name__== "__main__":
    app.run(debug=True)