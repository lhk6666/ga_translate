[![Build Status](https://travis-ci.org/tongtybj/jsk_uav_forest.svg?branch=master)](https://travis-ci.org/tongtybj/jsk_uav_forest)


## はじめに


これは森林におけるUAVチャレンジのためのリポジトリです。
[Forest Drone Robot Competition](http://www.lsse.kyutech.ac.jp/~sociorobo/ja/forestdrone17)


![](jsk_uav_forest_common/images/demo.gif)




## コンパイル方法


The text you provided is empty. Please provide the text you would like to have translated.
mkdir <catkin_ws>
cd <catkin_ws>
wstool init src
wstool set -t src jsk_uav_forest http://github.com/JSKAerialRobot/jsk_uav_forest --git
wstool merge -t src https://raw.githubusercontent.com/JSKAerialRobot/jsk_uav_forest/master/jsk_uav_forest.rosinstall
wstool update -t src
rosdep install -y -r --from-paths src --ignore-src --rosdistro $ROS_DISTRO
catkin build
The text you provided is empty. Please provide the text you would like to have translated.


## シミュレーションでプログラムを実行する方法


- 自律的な認識と動作によるGazeboでの実行
1. タスク1
The text you provided is empty. Please provide the text you would like to have translated.
$ roslaunch jsk_uav_forest_simulation forest_simulation.launch task_kind:=1
The text you provided is empty. Please provide the text you would like to have translated.
2. タスク2
The text you provided is empty. Please provide the text you would like to have translated.
roslaunch jsk_uav_forest_simulation forest_simulation.launch task_kind:=2 circle_motion_times:=2
The text you provided is empty. Please provide the text you would like to have translated.
3. タスク3
The text you provided is empty. Please provide the text you would like to have translated.
roslaunch jsk_uav_forest_simulation forest_simulation.launch task_kind:=3 target_num:=3
The text you provided is empty. Please provide the text you would like to have translated.


RVIZの左下隅にある`Send Topic`ボタンをクリックして開始します。


- 手動操作によるGazeboでの実行
The text you provided is empty. Please provide the text you would like to have translated.
$ roslaunch jsk_uav_forest_simulation forest_simulation.launch manual:=true
The text you provided is empty. Please provide the text you would like to have translated.


クアドローターを操作するにはターミナルを使用します。




## 森林チャレンジ（DJI M100 + DJI Guidance + Pointgrey Chameleon3 + Hokuyo UST20LXを使用）
1. UAVにおける統合ランチファイル
The text you provided is empty. Please provide the text you would like to have translated.
$ roslaunch jsk_uav_forest_common challenge.launch （異なるタスクに応じて上記のケースと同じオプション）
The text you provided is empty. Please provide the text you would like to have translated.


2. UAVにおけるリモート通信
The text you provided is empty. Please provide the text you would like to have translated.
$ roslaunch jsk_uav_forest_common communication2ground_station.launch UAV_IP:=10.42.0.1 GROUND_STATION_IP:=10.42.0.XXX
The text you provided is empty. Please provide the text you would like to have translated.
10.42.0.XXXは、あなたのリモートPCのIPアドレスです。


3. リモートPCにおけるリモート通信
The text you provided is empty. Please provide the text you would like to have translated.
roslaunch jsk_uav_forest_common ground_station.launch UAV_IP:=10.42.0.1 GROUND_STATION_IP:=10.42.0.XXX
The text you provided is empty. Please provide the text you would like to have translated.
10.42.0.XXXは、あなたのリモートPCのIPアドレスです。


4. タスクを開始する
The text you provided is empty. Please provide the text you would like to have translated.
$ rostopic pub /task_start std_msgs/Empty "{}"
The text you provided is empty. Please provide the text you would like to have translated.


## 結果を見る
The text you provided is empty. Please provide the text you would like to have translated.
$ roslaunch jsk_uav_forest_common result.launch
The text you provided is empty. Please provide the text you would like to have translated.


デフォルトデータはGazeboからの結果です。


## このmdファイルはこのアクションスクリプトの機能とは関係ありません（テスト用です）。