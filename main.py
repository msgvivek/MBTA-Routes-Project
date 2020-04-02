import requests
import longnamedata
import stopdata
import bluestop, redstop, orangestop, mattapanstop
import greenbstop, greencstop, greendstop, greenestop

long= longnamedata.b.get('data')
def long_name():
  for element in long:
  # finding long_name
    if 'attributes' in element.keys():
      print(element.get('attributes').get('long_name'))
print("Listing all long names:")
long_name()
print("\n")

bst=bluestop.bstop.get('data')
rst=redstop.rstop.get('data')
orst=orangestop.orstop.get('data')
mst=mattapanstop.mastop.get('data')
grbst=greenbstop.grbstop.get('data')
grcst=greencstop.grcstop.get('data')
grdst=greendstop.grdstop.get('data')
grest=greenestop.grestop.get('data')

def stops():
  blueList = []
  redList = []
  orangeList = []
  mattapanList = []
  greenbList = []
  greencList = []
  greendList = []
  greeneList = []
  
  for bnode in bst:
    if 'attributes' in bnode.keys():
      b1= bnode.get('attributes').get('name')
      blueList.append(b1)
  blue_length = (len(blueList))
  subway = {"Blue": blue_length}

  for rnode in rst:
    if 'attributes' in rnode.keys():
      r1= rnode.get('attributes').get('name')
      redList.append(r1)
  red_length = (len(redList))
  subway['Red'] = red_length

  for ornode in orst:
    if 'attributes' in ornode.keys():
      o1= ornode.get('attributes').get('name')
      orangeList.append(o1)
  orange_length = (len(orangeList))
  subway['Orange'] = orange_length

  for manode in mst:
    if 'attributes' in manode.keys():
      ma1= manode.get('attributes').get('name')
      mattapanList.append(ma1)
  mattapan_length = (len(mattapanList))
  subway['Mattapan'] = mattapan_length

  for grbnode in grbst:
    if 'attributes' in grbnode.keys():
      grb1= grbnode.get('attributes').get('name')
      greenbList.append(grb1)
  greenb_length = (len(greenbList))
  subway['Green-B'] = greenb_length

  for grcnode in grcst:
    if 'attributes' in grcnode.keys():
      grc1= grcnode.get('attributes').get('name')
      greencList.append(grc1)
  greenc_length = (len(greencList))
  subway['Green-C'] = greenc_length

  for grdnode in grdst:
    if 'attributes' in grdnode.keys():
      grd1= grdnode.get('attributes').get('name')
      greendList.append(grd1)
  greend_length = (len(greendList))
  subway['Green-D'] = greend_length

  for grenode in grest:
    if 'attributes' in grenode.keys():
      gre1= grenode.get('attributes').get('name')
      greeneList.append(gre1)
  greene_length = (len(greeneList))
  subway['Green-E'] = greene_length
  return[subway, greenbList, greencList, greendList, greeneList, mattapanList, redList, blueList, orangeList]
stops()
st = {"Green-B":stops()[1], "Green-C":stops()[2], "Green-D":stops()[3], "Green-E":stops()[4], "Mattapan":stops()[5], "Red":stops()[6], "Blue":stops()[7], "Orange":stops()[8]}

sorted_dict = sorted(stops()[0].items(), key=lambda k: k[1])
lowest_stops_name = sorted_dict[:1][0][0]
lowest_stops_number = sorted_dict[:1][0][1]
highest_stops_name = sorted_dict[-1:][0][0]
highest_stops_number = sorted_dict[-1:][0][1]
print(f"Subway Line {highest_stops_name} has the most stops with {highest_stops_number}")
print(f"Subway Line {lowest_stops_name} has the least stops with {lowest_stops_number}")
print("\n")

route_stop = input("Enter any two comma separated stops: ")
two_stops = [i.strip() for i in route_stop.split(",")]
print(f"The two stops are {two_stops[0]} and {two_stops[1]}")

for key1,value1 in st.items():
  line1 = []
  if two_stops[0] in value1:
    print (key1)
print("\n")

for key2,value2 in st.items():
  line2 = []
  if two_stops[1] in value2:
    print (key2)
