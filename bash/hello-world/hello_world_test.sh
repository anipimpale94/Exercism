@test "Say Hi!" {
  run bash hello_world.sh

  [ "$status" -eq 0 ]
  [ "$output" = "Hello, World!" ]
}
<<<<<<< HEAD

@test "argument name" {
  run bash hello_world.sh Ani

  [ "$status" -eq 0 ]
  [ "$output" = "Hello, Ani!" ]
}
=======
>>>>>>> cb05a54edeffc8b7c3a1973340f6f254ba7d099d
