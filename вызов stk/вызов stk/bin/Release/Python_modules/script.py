
from comtypes.client import CreateObject, GetActiveObject

uiApplication = GetActiveObject('STK11.Application')
uiApplication.Visible = False
root = uiApplication.Personality2

from comtypes.gen import STKUtil
from comtypes.gen import STKObjects
from comtypes.gen import AgSTKVgtLib
#root.NewScenario('Example_Scenario')
scenario = root.CurrentScenario
scenario2 = scenario.QueryInterface(STKObjects.IAgScenario)
#scenario2.SetTimePeriod('Today','+24hr')

#root.Rewind();

satellite = root.CurrentScenario.Children.New(18, 'MySatellite')
satellite2 = satellite.QueryInterface(STKObjects.IAgSatellite)
satellite2.SetPropagatorType(STKObjects.ePropagatorTwoBody)
propogator = satellite2.Propagator.QueryInterface(STKObjects.IAgVePropagatorTwoBody)
    
keplerian = propogator.InitialState.Representation.ConvertTo(1)
keplerian = keplerian.QueryInterface(STKObjects.IAgOrbitStateClassical)

keplerian.SizeShapeType = 0
keplerian.LocationType = 5
keplerian.Orientation.AscNodeType = 0

sizeShape = keplerian.SizeShape.QueryInterface(STKObjects.IAgClassicalSizeShapeAltitude)
sizeShape.PerigeeAltitude = 500
sizeShape.ApogeeAltitude = 600

keplerian.Orientation.Inclination = 90
keplerian.Orientation.ArgOfPerigee = 12
keplerian.Orientation.AscNode.Value = 24
keplerian.Location.Value = 180
propogator.InitialState.Representation.Assign(keplerian)
propogator.Propagate()
#input()
#uiApplication.Quit()