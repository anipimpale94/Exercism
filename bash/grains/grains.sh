#!/bin/bash
main() {
 if [ -z "$1" ]; then
  echo Error: invalid input
  exit 1
 else
  if [ "$1" -gt 0 ] && [ "$1" -lt 65 ]; then
   echo $(( 1<< $(( $1 - 1 )) ))
   exit 0
  else
   if [ "$1" == "total" ]; then
    echo $(( $(( 1<<$1  )) - 1 ))
    exit 0
   fi
   echo Error: invalid input
   exit 1
  fi
 fi
}

main "$@"
