#!/usr/bin/env bats

@test "jupyter-notebook works" {
  run jupyter-notebook --version &>> test.log
  [ "$status" -eq 0 ]
}

@test "boundry data exists" {
  run ls work-flow/06_Europe_Cities_Boundaries_with_Labels_Population.geo.json  &>> test.log
  [ "$status" -eq 0 ]
}

@test "jar files data exists" {
  run ls /usr/local/lib/jts-1.13.jar /usr/local/lib/spatial-spark_2.10-1.1.1-beta-SNAPSHOT.jar  &>> test.log
  [ "$status" -eq 0 ]
}

@test "pois data exists" {
  run  ls work-flow/pois.json &>> test.log
  [ "$status" -eq 0 ]
}
