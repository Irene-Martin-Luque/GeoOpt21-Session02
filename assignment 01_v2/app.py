#AIA Module at MaCAD, IaaC, directed by David Andrés León
#Session 02, Assinment 01 - GH to Python through Hops
#Excercise by Irene Martín Luque based on template

#importing flask and hops to create a workflow
from flask import Flask
import ghhops_server as hs

#importing rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)

#creating the hops component
@hops.component(
    "/Cylinder",
    name = "Create a Cylinder",
    inputs=[
        hs.HopsCurve("Circle", "C", "closed circle to extrude", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Height", "H", "Height", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
       hs.HopsBrep("Cylinder","C","Resulting Cylinder", hs.HopsParamAccess.LIST),
    ]
)

def Cylinder(baseCircle: rg.Circle, height: float):

    cyl = rg.Cylinder(baseCircle, height)
    return cyl.ToBrep(True, True)

if __name__== "__main__":
    app.run(debug=True)