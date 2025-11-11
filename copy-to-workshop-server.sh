#!/usr/bin/env bash
rm -r /opt/mscs/worlds/StreamingKurs/streamingkurs/
cp -r streamingkurs /opt/mscs/worlds/StreamingKurs/
chown -R minecraft:minecraft /opt/mscs/worlds/*
