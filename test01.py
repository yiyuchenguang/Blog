

ss = '''
    lv_StaticObjectPoints[*][0] = getSignal(isStaticObjectPoints#isConnectedToNext);
    lv_StaticObjectPoints[*][1] = getSignal(isStaticObjectPoints#PointClassType);
    lv_StaticObjectPoints[*][2] = getSignal(isStaticObjectPoints#ClassificationHistory);
    lv_StaticObjectPoints[*][3] = getSignal(isStaticObjectPoints#isFirstInPolygon);
    lv_StaticObjectPoints[*][4] = getSignal(isStaticObjectPoints#ClassificationConfidence);  
    lv_StaticObjectPoints[*][5] = getSignal(isStaticObjectPoints#TiStamp);
    lv_StaticObjectPoints[*][6] = getSignal(isStaticObjectPoints#DetectionHistory);
    lv_StaticObjectPoints[*][7] = getSignal(isStaticObjectPoints#HeightPoint);
    lv_StaticObjectPoints[*][8] = getSignal(isStaticObjectPoints#VertPosPoint);
    lv_StaticObjectPoints[*][9] = getSignal(isStaticObjectPoints#TrackingStatusPoints);     
    lv_StaticObjectPoints[*][10] = getSignal(isStaticObjectPoints#LatPosPoint);
    lv_StaticObjectPoints[*][11] = getSignal(isStaticObjectPoints#LongPosPoint);
    lv_StaticObjectPoints[*][12] = getSignal(isStaticObjectPoints#ObjectAssociationId);
    lv_StaticObjectPoints[*][13] = getSignal(isStaticObjectPoints#isVerified);
    lv_StaticObjectPoints[*][14] = getSignal(isStaticObjectPoints#DetectionConfidence);      
    lv_StaticObjectPoints[*][15] = getSignal(isStaticObjectPoints#PolygonId);
    lv_StaticObjectPoints[*][16] = getSignal(isStaticObjectPoints#StdDevLatPos);
    lv_StaticObjectPoints[*][17] = getSignal(isStaticObjectPoints#StdDevLongPos);
    lv_StaticObjectPoints[*][18] = getSignal(isStaticObjectPoints#LatLongPosCorr);
'''

dd = ''''''

for i in range(100):
    dd = dd + "\n" + "        /***************StaticObjectPoints%d*****************/"%(i+1) + ss.replace("*",str(i)).replace("#",str(i+1))
print(dd)
