proc add*(a, b: cint): cint {.importc, dynlib: "./libsum.so"}

when isMainModule:
  echo add(4, 5)
