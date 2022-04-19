from flask import Flask
import ghhops_server as hs

#we also import random library to generate some randomness 
import random as r

#finally we bring rhino3dm to create rhino geometry in python
import rhino3dm as rg

app = Flask(__name__)
hops = hs.Hops(app)


@hops.component(
    "/extrudeCurve",
    name = "Extrude a Curve",
    inputs=[
        hs.HopsCurve("Curve", "C", "closed planar curve to extrude", hs.HopsParamAccess.ITEM),
        hs.HopsNumber("Height", "H", "Height", hs.HopsParamAccess.ITEM),
    ],
    outputs=[
       hs.HopsBrep("Extrusion","E","Resulting Extrusion", hs.HopsParamAccess.LIST),
    ]
)

def extrudeCurve(curve: rg.Curve, height: float):

    extrusion = rg.Extrusion.Create(curve, height, cap = True)
    return extrusion

if __name__== "__main__":
    app.run(debug=True)