#!/usr/bin/env bats

@test "jupyter-notebook works" {
  run jupyter-notebook --version &>> test.log
  [ "$status" -eq 0 ]
}

@test "boundry data exists" {
  run ls work-flow/06_Europe_Cities_Boundries_with_Labels_Population.geo.json  &>> test.log
  [ "$status" -eq 0 ]
}

@test "pois data exists" {
  run  ls work-flow/pois.json &>> test.log
  [ "$status" -eq 0 ]
}
