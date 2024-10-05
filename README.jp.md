[![ビルドステータス](https://travis-ci.org/tongtybj/jsk_uav_forest.svg?branch=master)](https://travis-ci.org/tongtybj/jsk_uav_forest)


## はじめに


これは、森林でのUAVチャレンジのためのリポジトリです。
[森のドローン・ロボット競技会](http://www.lsse.kyutech.ac.jp/~sociorobo/ja/forestdrone17)


![](jsk_uav_forest_common/images/demo.gif)




## コンパイル方法


```

mkdir <catkin_ws>
cd <catkin_ws>
wstool init src
wstool set -t src jsk_uav_forest http://github.com/JSKAerialRobot/jsk_uav_forest --git
wstool merge -t src https://raw.githubusercontent.com/JSKAerialRobot/jsk_uav_forest/master/jsk_uav_forest.rosinstall
wstool update -t src
rosdep install -y -r --from-paths src --ignore-src --rosdistro $ROS_DISTRO
catkin build
```



## シミュレーションでプログラムを実行する方法


- 自律的な認識と動作によってGazeboで実行する
1. task1 
```

$ roslaunch jsk_uav_forest_simulation forest_simulation.launch task_kind:=1
```

2. task2
```

roslaunch jsk_uav_forest_simulation forest_simulation.launch task_kind:=2 circle_motion_times:=2
```

3. task3
```

roslaunch jsk_uav_forest_simulation forest_simulation.launch task_kind:=3 target_num:=3
```



RVIZの左下隅にある「Send Topic」ボタンをクリックして開始します。


- 手動操作でGazeboを実行する
```

$ roslaunch jsk_uav_forest_simulation forest_simulation.launch manual:=true
```



端末を使用してクアッドローターを操作する




## 森林チャレンジ (DJI M100 + DJI Guidance + Pointgrey Chameleon3 + Hokuyo UST20LXを使用)
1. UAVでの統合ローンチファイル
```

$ roslaunch jsk_uav_forest_common challenge.launch (異なるタスクに応じて、上記のケースと同じオプション)
```



2. UAVでのリモート通信
```

$ roslaunch jsk_uav_forest_common communication2ground_station.launch UAV_IP:=10.42.0.1 GROUND_STATION_IP:=10.42.0.XXX
```

10.42.0.XXXは、リモートPCのIPアドレスです。


3. リモートPCでのリモート通信
```

roslaunch jsk_uav_forest_common ground_station.launch UAV_IP:=10.42.0.1 GROUND_STATION_IP:=10.42.0.XXX
```

10.42.0.XXXは、リモートPCのIPアドレスです。


4. タスクを開始する
```

$ rostopic pub /task_start std_msgs/Empty "{}"
```



## 結果を見る
```

$ roslaunch jsk_uav_forest_common result.launch
```



デフォルトのデータはGazeboからの結果です。


## このmdファイルは、このアクションスクリプトの機能とは関係ありません（テスト用です）。