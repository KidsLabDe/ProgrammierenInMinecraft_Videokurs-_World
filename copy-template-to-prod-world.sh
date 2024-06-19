#!/usr/bin/env bash
rm -r /opt/mscs/worlds/Redstonekurs/redstone-kurs-welt/
cp -r /opt/mscs/worlds/Redstonekurs-Template/redstone-kurs-welt/ /opt/mscs/worlds/Redstonekurs/
chown -R minecraft:minecraft /opt/mscs/worlds/*
