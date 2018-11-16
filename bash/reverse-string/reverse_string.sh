#!/bin/bash
main() {
 echo "$1"|rev
 exit 0
}
main "$@"
