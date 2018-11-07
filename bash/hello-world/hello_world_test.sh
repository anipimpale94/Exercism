@test "Say Hi!" {
  run bash hello_world.sh

  [ "$status" -eq 0 ]
  [ "$output" = "Hello, World!" ]
}

@test "argument name" {
  run bash hello_world.sh Ani

  [ "$status" -eq 0 ]
  [ "$output" = "Hello, Ani!" ]
}
