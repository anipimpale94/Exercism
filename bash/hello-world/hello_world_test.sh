#!/usr/bin/env bash

@test "Say Hi!" {
  bash hello_world.sh

  [ "$status" -eq 0 ]
  [ "$output" = "Hello, World!" ]
}