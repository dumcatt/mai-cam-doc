#!/bin/sh

# MovieCamアプリケーション起動スクリプト
# '11.11.1 FSI 岩瀬

startup ()
{
        #--------------------------------------------------------------------------------
        # 電源断検地用ドライバをインストール
        major=`grep pdmonitor /proc/devices  | awk '{FS=" "; print $1}'`
        mknod /dev/pdmonitor c ${major} 0

        #--------------------------------------------------------------------------------
        apdir="/sega/application"
        apname="moviecam"

        # TEMPフォルダ配下のデータを削除
        \rm -rf /sega/temp/*

        # RAMディスク配下のディレクトリを起動毎に自動で作る
        mkdir -p /sega/temp/sound
        mkdir -p /sega/temp/movie

        #
        # IPCリソースを初期化
        for var in `ipcs  | \grep "root"  | \awk '{FS=" "; print $2}'`; do
                ipcrm -q $var
                ipcrm -s $var
                ipcrm -m $var
        done
        for var in `ipcs | \grep "root"  | \awk '{FS=" "; print $1}'`; do
                ipcrm -Q $var
                ipcrm -S $var
                ipcrm -M $var
        done
        ipcs

        cd $apdir
        ./$apname

        if [ $? != "0" ]; then
        # 起動失敗
                echo "fail to start the application. try with backup."
                filename=`readlink $apname`
                fnamelen=`expr length $filename`
                appno=`expr substr $filename $fnamelen 1`
                if [ $appno = "0" ]; then
                        appno=1
                else
                        appno=0
                fi

                if [ -e ${apname}_${appno} ]; then
                # 予備から起動
                        rm -f $apname
                        ln -s ${apname}_${appno} $apname

                        ./$apname

                        if [ $? != "0" ]; then
                                echo "backup also cannot be started by some reason."
                        fi

                else
                # 予備がないのであきらめる
                        echo "there is no backup."

                fi
        fi
}

case "$1" in
    start)
                startup
        ;;
    *)
        echo "$0 <start>"
        ;;
esac