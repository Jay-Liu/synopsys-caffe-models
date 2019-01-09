## Generated by graphCompress tool automatically ##
## Compress configuration and fine tuning goal ##
compressConfig = {
  'InceptionV1__InceptionV1__Conv2d_2c_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [48, 48]},
  'InceptionV1__InceptionV1__Mixed_3b__Branch_1__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [48, 64]},
  'InceptionV1__InceptionV1__Mixed_3b__Branch_2__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [16, 16]},
  'InceptionV1__InceptionV1__Mixed_3c__Branch_1__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [64, 64]},
  'InceptionV1__InceptionV1__Mixed_3c__Branch_2__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [28, 24]},
  'InceptionV1__InceptionV1__Mixed_4b__Branch_1__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [48, 48]},
  'InceptionV1__InceptionV1__Mixed_4b__Branch_2__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [16, 16]},
  'InceptionV1__InceptionV1__Mixed_4c__Branch_1__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [48, 56]},
  'InceptionV1__InceptionV1__Mixed_4c__Branch_2__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [24, 24]},
  'InceptionV1__InceptionV1__Mixed_4d__Branch_1__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [48, 48]},
  'InceptionV1__InceptionV1__Mixed_4d__Branch_2__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [24, 24]},
  'InceptionV1__InceptionV1__Mixed_4e__Branch_1__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [72, 72]},
  'InceptionV1__InceptionV1__Mixed_4e__Branch_2__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [24, 24]},
  'InceptionV1__InceptionV1__Mixed_4f__Branch_1__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [80, 84]},
  'InceptionV1__InceptionV1__Mixed_4f__Branch_2__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [32, 48]},
  'InceptionV1__InceptionV1__Mixed_5b__Branch_1__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [84, 84]},
  'InceptionV1__InceptionV1__Mixed_5b__Branch_2__Conv2d_0a_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [32, 32]},
  'InceptionV1__InceptionV1__Mixed_5c__Branch_1__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [92, 92]},
  'InceptionV1__InceptionV1__Mixed_5c__Branch_2__Conv2d_0b_3x3__Conv2D'  : {'algorithm': 'Tucker-2', 'rank': [40, 40]},
}
tuningGoal = [{'accuracy@5': 0.9, 'loss': 1.2, 'accuracy@1': 0.71}]

## Compress factor and layer factors of this config##
desiredCompressFactor = None
realCompressFactor = 1.97657779846
layerCompressFactor = {
  'InceptionV1__InceptionV1__Conv2d_1a_7x7__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Conv2d_2b_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Conv2d_2c_3x3__Conv2D'  : 3.3488372093,
  'InceptionV1__InceptionV1__Mixed_3b__Branch_0__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_3b__Branch_1__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_3b__Branch_2__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_3b__Branch_3__Conv2d_0b_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_3b__Branch_1__Conv2d_0b_3x3__Conv2D'  : 2.73417721519,
  'InceptionV1__InceptionV1__Mixed_3b__Branch_2__Conv2d_0b_3x3__Conv2D'  : 1.5,
  'InceptionV1__InceptionV1__Mixed_3c__Branch_0__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_3c__Branch_1__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_3c__Branch_2__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_3c__Branch_3__Conv2d_0b_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_3c__Branch_1__Conv2d_0b_3x3__Conv2D'  : 3.85714285714,
  'InceptionV1__InceptionV1__Mixed_3c__Branch_2__Conv2d_0b_3x3__Conv2D'  : 2.98961937716,
  'InceptionV1__InceptionV1__Mixed_4b__Branch_0__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4b__Branch_1__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4b__Branch_2__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4b__Branch_3__Conv2d_0b_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4b__Branch_1__Conv2d_0b_3x3__Conv2D'  : 5.08695652174,
  'InceptionV1__InceptionV1__Mixed_4b__Branch_2__Conv2d_0b_3x3__Conv2D'  : 2.07692307692,
  'InceptionV1__InceptionV1__Mixed_4c__Branch_0__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4c__Branch_1__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4c__Branch_2__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4c__Branch_3__Conv2d_0b_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4c__Branch_1__Conv2d_0b_3x3__Conv2D'  : 5.36170212766,
  'InceptionV1__InceptionV1__Mixed_4c__Branch_2__Conv2d_0b_3x3__Conv2D'  : 1.89473684211,
  'InceptionV1__InceptionV1__Mixed_4d__Branch_0__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4d__Branch_1__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4d__Branch_2__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4d__Branch_3__Conv2d_0b_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4d__Branch_1__Conv2d_0b_3x3__Conv2D'  : 7.52941176471,
  'InceptionV1__InceptionV1__Mixed_4d__Branch_2__Conv2d_0b_3x3__Conv2D'  : 1.89473684211,
  'InceptionV1__InceptionV1__Mixed_4e__Branch_0__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4e__Branch_1__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4e__Branch_2__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4e__Branch_3__Conv2d_0b_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4e__Branch_1__Conv2d_0b_3x3__Conv2D'  : 4.8,
  'InceptionV1__InceptionV1__Mixed_4e__Branch_2__Conv2d_0b_3x3__Conv2D'  : 2.46153846154,
  'InceptionV1__InceptionV1__Mixed_4f__Branch_0__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4f__Branch_1__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4f__Branch_2__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4f__Branch_3__Conv2d_0b_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_4f__Branch_1__Conv2d_0b_3x3__Conv2D'  : 4.60063897764,
  'InceptionV1__InceptionV1__Mixed_4f__Branch_2__Conv2d_0b_3x3__Conv2D'  : 1.75609756098,
  'InceptionV1__InceptionV1__Mixed_5b__Branch_0__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_5b__Branch_1__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_5b__Branch_2__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_5b__Branch_3__Conv2d_0b_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_5b__Branch_1__Conv2d_0b_3x3__Conv2D'  : 4.43828016644,
  'InceptionV1__InceptionV1__Mixed_5b__Branch_2__Conv2d_0a_3x3__Conv2D'  : 2.57142857143,
  'InceptionV1__InceptionV1__Mixed_5c__Branch_0__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_5c__Branch_1__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_5c__Branch_2__Conv2d_0a_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_5c__Branch_3__Conv2d_0b_1x1__Conv2D'  : 1.0,
  'InceptionV1__InceptionV1__Mixed_5c__Branch_1__Conv2d_0b_3x3__Conv2D'  : 5.13712374582,
  'InceptionV1__InceptionV1__Mixed_5c__Branch_2__Conv2d_0b_3x3__Conv2D'  : 2.57910447761,
  'InceptionV1__Logits__Conv2d_0c_1x1__Conv2D'  : 1.0,
}